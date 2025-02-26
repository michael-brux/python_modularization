""" Hello Module"""
from hello_utils import print_module_info
from pathlib import Path
import time
import datetime

print("\nHello, World! - from Module")

print_module_info(__file__, __name__)
#print()
#print("filename of __file__ is      :", Path(__file__).name)
#print("__name__ is                  :", __name__)
#print("current working directory is :", Path.cwd())
#print("directory of __file__ is     :", Path(__file__).parent)

def get_greet():
    match time.localtime().tm_hour:
        case hour if hour < 6:
            return "Good Night!"
        case hour if hour < 12:
            return "Good Morning!"
        case hour if hour < 18:
            return "Good Afternoon!"
        case hour if hour < 22:
            return "Good Evening!"
        case _:
            return "Good Night!"


def get_filetime(file_path=__file__, time_type="created"):
    def as_datetime(timestamp):
        return datetime.datetime.fromtimestamp(timestamp)
    stat = Path(file_path).stat()
    match time_type:
        case "modified":
            return as_datetime(stat.st_mtime)
        case "accessed":
            return as_datetime(stat.st_atime)
        case _:
            return as_datetime(stat.st_ctime)
