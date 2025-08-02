from __future__ import annotations

import logging
import socket
import struct
from types import TracebackType
from typing import Callable, Optional

from rcrscore.proto.RCRSProto_pb2 import MessageProto


class ConnectionError(Exception):
  """Connection related errors."""

  pass


class MessageReadError(ConnectionError):
  """Error reading message from socket."""

  pass


class AgentCalculationError(Exception):
  """Error related to agent calculation."""

  pass


class Connection:
  """Handles network communication with the RCRS kernel."""

  # Constants
  INT32_SIZE = 4
  DEFAULT_BUFFER_SIZE = 4096

  def __init__(self, host: str, port: int):
    self.host = host
    self.port = port
    self.socket: Optional[socket.socket] = None
    self.buffer_size = self.DEFAULT_BUFFER_SIZE
    self.agent_message_handler: Optional[Callable[[MessageProto], None]] = None
    self.logger = logging.getLogger(__name__)

  def connect(self) -> None:
    """Establish connection to the kernel."""
    try:
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.connect((self.host, self.port))
      self.logger.info(f"Connected to {self.host}:{self.port}")
    except socket.error as e:
      raise ConnectionError(f"Failed to connect to {self.host}:{self.port}: {e}")

  def disconnect(self) -> None:
    """Close the connection."""
    if self.socket:
      try:
        self.socket.close()
        self.logger.info("Connection closed")
      except socket.error as e:
        self.logger.warning(f"Error closing socket: {e}")
      finally:
        self.socket = None

  def __enter__(self) -> Connection:
    """Context manager entry."""
    self.connect()
    return self

  def __exit__(self, exc_type: type, exc_val: Exception, exc_tb: TracebackType) -> None:
    """Context manager exit."""
    self.disconnect()

  def parse_message_from_kernel(self) -> None:
    """
    Continuously parse messages from kernel until connection is closed.

    Raises:
        ConnectionError: If message handler is not set or connection fails.
    """
    if not self.agent_message_handler:
      raise ConnectionError("Agent message handler not set")

    if not self.socket:
      raise ConnectionError("Not connected to kernel")

    while True:
      try:
        message = self._read_message()
      except EOFError:
        self.logger.info("Kernel closed connection")
        raise ConnectionError("Kernel closed connection")
      except MessageReadError as e:
        self.logger.error(f"Failed to read message: {e}")
        raise ConnectionError("Failed to read message")
      try:
        self.agent_message_handler(message)
      except Exception as e:
        self.logger.error(f"Error in agent calculation: {e}")
        raise AgentCalculationError(f"Agent calculation failed: {e}")

  def set_agent_message_handler(self, handler: Callable[[MessageProto], None]) -> None:
    """Set the message handler for incoming messages."""
    self.agent_message_handler = handler

  def send_message(self, message: MessageProto) -> None:
    """
    Send a message to the kernel.

    Args:
        message: The protobuf message to send

    Raises:
        ConnectionError: If not connected or send fails
    """
    if not self.socket:
      raise ConnectionError("Not connected to kernel")

    try:
      serialized = message.SerializeToString()
      self._write_int32(len(serialized))
      self.socket.sendall(serialized)

    except socket.error as e:
      raise ConnectionError(f"Failed to send message: {e}")

  def _read_message(self) -> MessageProto:
    """
    Read a complete message from the socket.

    Returns:
        Parsed MessageProto

    Raises:
        MessageReadError: If message reading fails
    """
    try:
      message_size = self._read_int32()
      message_data = self._read_n_bytes(message_size)

      message = MessageProto()
      message.ParseFromString(message_data)
      return message

    except (EOFError, struct.error, socket.error) as e:
      raise MessageReadError(f"Failed to read message: {e}")

  def _read_n_bytes(self, n: int) -> bytes:
    """
    Read exactly n bytes from the socket.

    Args:
        n: Number of bytes to read

    Returns:
        The read bytes

    Raises:
        EOFError: If connection is closed before reading all bytes
        socket.error: If socket operation fails
    """
    if not self.socket:
      raise socket.error("Socket not connected")

    buffer = b""
    remaining = n

    while remaining > 0:
      try:
        chunk = self.socket.recv(min(remaining, self.buffer_size))
        if not chunk:  # Connection closed
          raise EOFError("Connection closed while reading")

        buffer += chunk
        remaining -= len(chunk)

      except socket.error as e:
        raise socket.error(f"Socket read error: {e}")

    return buffer

  def _read_int32(self) -> int:
    """
    Read a 32-bit integer from the socket (big-endian).

    Returns:
        The integer value

    Raises:
        EOFError: If connection is closed
        struct.error: If data is invalid
    """
    data = self._read_n_bytes(self.INT32_SIZE)
    return struct.unpack(">I", data)[0]  # Big-endian unsigned int

  def _write_int32(self, value: int) -> None:
    """
    Write a 32-bit integer to the socket (big-endian).

    Args:
        value: The integer to write

    Raises:
        socket.error: If write fails
    """
    if not self.socket:
      raise socket.error("Socket not connected")

    data = struct.pack(">I", value)  # Big-endian unsigned int
    self.socket.sendall(data)
