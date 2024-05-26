def codes(txt: str) -> dict[str, str]:
    lines = [item.strip("\n") for item in open(txt, "r").readlines()]

    dictionary = {}

    for line in lines:
        id, password = line.split(":")
        dictionary.update({id: password})

    return dictionary


if __name__ == "__main__":
    file = "codes.txt"
    main = codes(file)
    print(main)