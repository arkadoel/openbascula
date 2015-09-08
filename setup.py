__author__ = 'https://github.com/arkadoel'
"""
Compilar en linux
sudo /opt/miniconda3/bin/python3 ./setup.py build

"""
import sys
from cx_Freeze import setup, Executable
import core.Constantes as const

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ['', 'gui', 'core', 'core.manzana', 'directORM'],
    "excludes": ["tkinter"]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = const.APP_NAME,
        version = const.APP_VERSION,
        description = const.APP_NAME + ' ' + const.APP_VERSION,
        options = {"build_exe": build_exe_options},
        executables = [Executable("__init__.py", base=base)])
