import sys

from rcrscore.launcher.launcher import ArgumentParser, Launcher


def main() -> None:
  """Main entry point."""
  try:
    # Parse arguments
    arg_parser = ArgumentParser()
    config = arg_parser.parse_args()

    # Launch agents
    launcher = Launcher()
    launcher.run(config)

  except KeyboardInterrupt:
    print("Launcher interrupted by user.")
    sys.exit(1)
  except Exception as e:
    print(f"Launcher failed: {e}")
    sys.exit(1)


if __name__ == "__main__":
  main()
