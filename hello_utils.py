#!/usr/bin/env python3
""" Hello Utilities """
from pathlib import Path

def print_module_info(file, name):
	print()
	print("filename of __file__ is      :", Path(file).name)
	print("__name__ is                  :", name)
	print("current working directory is :", Path.cwd())
	print("directory of __file__ is     :", Path(file).parent)





