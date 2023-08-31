import configparser
from pathlib import Path

# Get PATH of project
if __name__ == "__main__":
    # Set PATH for interactive sessions manually: (only for development)
    PATH = Path("/home/ur/polcyc_effect/")
else:
    PATH = Path(__file__).parent.parent

if Path.joinpath(PATH, "config.ini").is_file():
    config = configparser.ConfigParser()
    config.read(Path.joinpath(PATH, "config.ini"))
else:
    raise FileNotFoundError("config.ini not found.")
