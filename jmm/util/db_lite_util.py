# import sqlite3
# con = sqlite3.connect('example.db')
from jmm.util.util_ import get_script_path
from os import path

folder = path.dirname(get_script_path())
print(folder)