
from pathlib import Path

file_path = Path.cwd() / "my_folder" / "my_file.txt"
print(file_path)
print("Parent -", file_path.parent)
print(list(file_path.parents))

file_path.mkdir(exist_ok=True)
file_path.touch(exist_ok=True)

print(file_path.exists())
print(file_path.name)
print(file_path.parent.name)