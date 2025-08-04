from logging import DEBUG, Formatter, Logger, StreamHandler

# from logging.handlers import RotatingFileHandler


def get_logger(name: str, agent_id: int) -> Logger:
  logger = Logger(name)
  # file_handler = RotatingFileHandler(filename=f"logs/{name}.log", mode="a")
  console_handler = StreamHandler()
  formatter = Formatter(f"%(levelname)-3s %(name)s({agent_id}): %(message)s")
  # file_handler.setFormatter(formatter)
  console_handler.setFormatter(formatter)
  # logger.addHandler(file_handler)
  logger.addHandler(console_handler)
  logger.setLevel(DEBUG)
  return logger


class ClientLoggerSingleton:
  _instance = None

  @classmethod
  def get_instance(cls) -> Logger:
    if cls._instance is None:
      cls._instance = Logger("client")
      formatter = Formatter("%(levelname)-3s %(name)s: %(message)s")
      handler = StreamHandler()
      handler.setFormatter(formatter)
      cls._instance.addHandler(handler)
      cls._instance.setLevel(DEBUG)

    return cls._instance
