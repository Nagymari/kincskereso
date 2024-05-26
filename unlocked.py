def get_unlocked(file: str) -> list[int]:
    numbers = [n.strip("\n") for n in open(file, "r", encoding="utf-8").readlines() if n != "\n"]
    numbers = [int(n.split(" ")[0]) for n in numbers]

    unlocked = [1]

    if 1 in numbers:
        unlocked.append(2)
    if 2 in numbers:
        unlocked.append(3)
    if 3 in numbers:
        unlocked += [4, 5, 6, 7]

    if 4 in numbers:
        unlocked.append(8)
    if 8 in numbers:
        unlocked.append(12)
    if 12 in numbers:
        unlocked.append(16)

    if 5 in numbers:
        unlocked.append(9)
    if 9 in numbers:
        unlocked.append(13)
    if 13 in numbers:
        unlocked.append(17)

    if 6 in numbers:
        unlocked.append(10)
    if 10 in numbers:
        unlocked.append(14)
    if 14 in numbers:
        unlocked.append(18)

    if 7 in numbers:
        unlocked.append(11)
    if 11 in numbers:
        unlocked.append(15)
    if 15 in numbers:
        unlocked.append(19)

    if 16 in numbers and 17 in numbers and 18 in numbers and 19 in numbers:
        unlocked.append(20)

    if 20 in numbers:
        unlocked.append(21)

    return unlocked


def test_(file: str, x: int) -> bool:
    lines = [item.strip("\n") for item in open(file, "r").readlines() if item != "\n"]
    lines = [int(item.split(" ")[0]) for item in lines]

    for line in lines:
        if x == line:
            return True
    return False
