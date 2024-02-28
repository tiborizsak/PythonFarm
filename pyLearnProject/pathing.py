from pathlib import Path
import os

print(Path('valami') / 'valamimas' / 'megintvalamimas')
print(os.path.join('folder', 'other', 'folder'))

print(os.getcwd()) # current working directory
os.listdir('.')

print(os.path.isabs('/path'))

print(os.path.relpath('/thispath', '/theotherpath'))

print(os.path.isdir('path'))

print(os.path.isfile('path'))

print(os.path.getsize('path'))

print(os.path.exists('/path'))

os.makedirs('/path/to/folder')
