import configparser
from pathlib import Path

PATH = Path(__file__).parent.parent

config = configparser.ConfigParser()
config.read(Path.joinpath(PATH, "config.ini"))
