import os

main_path = "login\\answers\\"

quests = 21
classes = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B', '4C']
files = [str(i + 1) + ".txt" for i in range(quests)] + ["completed.txt"]


def dirs() -> list[str]:
    for c in classes:
        os.mkdir(main_path + c)
    os.mkdir(main_path + "teachers")
    os.mkdir(main_path + "tibor")

    return [main_path + c for c in classes] + [main_path + "teachers"] + [main_path + "tibor"]


def create_files(path: str) -> None:
    for file in files:
        open(path + "\\" + file, "w").close()


for item in dirs():
    create_files(item)
