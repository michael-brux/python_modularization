#!/usr/bin/env python3
""" Hello Script"""
from pathlib import Path
from hello_utils import print_module_info
from hello_module import get_greet, get_filetime

print("\nHello, World! - from script")

print_module_info(__file__, __name__)
#print()
#print("filename of __file__ is      :", Path(__file__).name)
#print("__name__ is                  :", __name__)
#print("current working directory is :", Path.cwd())
#print("directory of __file__ is     :", Path(__file__).parent)

print()
print("with help of imported module :", get_greet())
print("file created time is         :", get_filetime(__file__))




