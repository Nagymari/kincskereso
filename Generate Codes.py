file = "codes.txt"

choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

classes = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B', '4C']


def generate_code() -> str:
    import random
    return "".join([random.choice(choices) for i in range(6)])


def write(text: str) -> None:
    open(file, "w").write(text)


save = []
codes = "admin:" + generate_code() + "\n"
l = len(classes) - 1

for n, c in enumerate(classes):
    code = generate_code()

    while code in save:
        code = generate_code()
    save.append(code)

    codes += c + ":" + generate_code()

    if n != l:
        codes += "\n"


write(codes)
