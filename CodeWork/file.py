from pathlib import Path

path = Path("C:\Kelloges\private.img")
cwd_path = Path.cwd() / "pyfile" / "private.txt"
print(cwd_path)
print("Parent -", path.parent)
print(list(cwd_path.parents))
print(path.anchor)
print("Name - ", path.name)
print("Suffix - ", path.suffix)
print("Stem - ", path.stem)
cwd_path.mkdir(exist_ok=True)

cwd_path.parent.mkdir(exist_ok=True)
new_file = cwd_path / "private.txt"
new_file.touch()

print("Exists? - ", path.exists())
print("isDir - ", cwd_path.is_dir())
