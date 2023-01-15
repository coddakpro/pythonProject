import pathlib

path1 = pathlib.path.cwd()
folder_a = path1 / "folder_a"
folder_a.mkdir(exist_ok=True)

file_path = [folder_a / "private.img",
             folder_a / "lyrics.txt",
             folder_a / "alone.vid",
             folder_a / "inside.csv",
             folder_a / "bible.txt",
             folder_a / "looks.jnp"]

for path in file_paths:
    path.touch()

    for files in path1.glob("*/*.txt"):
        print(files.name)

        for file in folder_a.iterdir():
            print(file)
source = path1 / "files_cohort_14.py"
print(source.exists())
source = path1 / "files_cohort_14.py"
destination = path1 / "folder_a" / "files_cohort_14.py"
source.replace(destination)



