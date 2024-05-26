from django.shortcuts import render, redirect
from read_in_codes import codes
import os
from unlocked import get_unlocked, test_
from datetime import datetime

path = os.path.dirname(__file__)


answers = {1: "igen",
           2: "figyelj",
           3: "01001000",
           # Keresési ág
           4: "biblioteca",
           8: "ugrás rómából az attika-félszigetig",
           12: "aki keres az talál",
           16: "petőfi sándor: anyám tyúkja",
           # Logikai ág
           5: "rubídium",
           9: "józsef attila: tiszta szívvel",
           13: "zw",
           17: "hajrávámbéry",
           # Művészeti ág
           6: "olajfesték",
           10: ["summer", "nyár"],
           14: "defaced chef",
           18: "kartográfia",
           # Irodalmi ág
           7: "9",
           11: "the riddle",
           15: "kronosz",
           19: "264",
           # Utolsó két feladat
           20: "042",
           21: "mi vagyunk a kulcs"}


def login(request):
    return render(request, "login.html")


def main_page(request, id=None, password=None):
    """The main page."""

    if id is None or password is None:
        # Get the ID and the password that the user typed in
        password = request.POST.get("password")
        id = request.POST.get("id")

    if id is None or password is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    # Get the IDs and the codes
    data = codes("codes.txt")

    # Test if the given information is correct
    if id in data and data.get(id) == password:
        # Get the path to the folder of this team
        p = path + "\\answers\\" + id + "\\"

        # Get the list of unlocked buttons
        unlocked = get_unlocked(p + "completed.txt")

        # Return the loaded in main web page
        return render(request, "main.html", {"ID": id, "buttons": unlocked})
    # Return the login page
    return render(request, "login.html")


def one(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(1):
        file = p + "completed.txt"

        if not test_(file, 1):
            open(file, "a").write("\n1 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        return render(request, "main.html", {"ID": id, "buttons": unlocked})
    else:
        file = p + "1.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task1.html", {"ID": id})


def two(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(2):
        file = p + "completed.txt"

        if not test_(file, 2):
            open(file, "a").write("\n2 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        return render(request, "main.html", {"ID": id, "buttons": unlocked})
    else:
        file = p + "2.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task2.html", {"ID": id})


def three(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(3):
        file = p + "completed.txt"

        if not test_(file, 3):
            open(file, "a").write("\n3 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        return render(request, "main.html", {"ID": id, "buttons": unlocked})
    else:
        file = p + "3.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task3.html", {"ID": id})


def search(request):
    id = request.POST.get("id")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"
    unlocked = get_unlocked(p + "completed.txt")

    new = []
    if 4 in unlocked:
        new.append(1)
    if 8 in unlocked:
        new.append(2)
    if 12 in unlocked:
        new.append(3)
    if 16 in unlocked:
        new.append(4)

    return render(request, "search.html", {"ID": id, "buttons": new})


def solar(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(4):
        file = p + "completed.txt"

        if not test_(file, 4):
            open(file, "a").write("\n4 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 8 in unlocked:
            new_unlocked.append(2)
        if 12 in unlocked:
            new_unlocked.append(3)
        if 16 in unlocked:
            new_unlocked.append(4)

        return render(request, "search.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "4.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task4.html", {"ID": id})


def code(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(8):
        file = p + "completed.txt"

        if not test_(file, 8):
            open(file, "a").write("\n8 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 8 in unlocked:
            new_unlocked.append(2)
        if 12 in unlocked:
            new_unlocked.append(3)
        if 16 in unlocked:
            new_unlocked.append(4)

        return render(request, "search.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "8.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task8.html", {"ID": id})


def glory(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(12):
        file = p + "completed.txt"

        if not test_(file, 12):
            open(file, "a").write("\n12 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 8 in unlocked:
            new_unlocked.append(2)
        if 12 in unlocked:
            new_unlocked.append(3)
        if 16 in unlocked:
            new_unlocked.append(4)

        return render(request, "search.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "12.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task12.html", {"ID": id})


def twin(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(16):
        file = p + "completed.txt"

        if not test_(file, 16):
            open(file, "a").write("\n16 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1, 2, 3, 4, 5, 6, 7]

        if 20 in unlocked:
            new_unlocked.append(8)
        if 21 in unlocked:
            new_unlocked.append(9)

        return render(request, "main.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "16.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task16.html", {"ID": id})


def art(request):
    id = request.POST.get("id")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"
    unlocked = get_unlocked(p + "completed.txt")

    new = []
    if 6 in unlocked:
        new.append(1)
    if 10 in unlocked:
        new.append(2)
    if 14 in unlocked:
        new.append(3)
    if 18 in unlocked:
        new.append(4)

    return render(request, "art.html", {"ID": id, "buttons": new})


def market(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(6):
        file = p + "completed.txt"

        if not test_(file, 6):
            open(file, "a").write("\n6 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 10 in unlocked:
            new_unlocked.append(2)
        if 14 in unlocked:
            new_unlocked.append(3)
        if 18 in unlocked:
            new_unlocked.append(4)

        return render(request, "art.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "6.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task6.html", {"ID": id})


def painting(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() in answers.get(10):
        file = p + "completed.txt"

        if not test_(file, 10):
            open(file, "a").write("\n10 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 10 in unlocked:
            new_unlocked.append(2)
        if 14 in unlocked:
            new_unlocked.append(3)
        if 18 in unlocked:
            new_unlocked.append(4)

        return render(request, "art.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "10.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task10.html", {"ID": id})


def piece(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(14):
        file = p + "completed.txt"

        if not test_(file, 14):
            open(file, "a").write("\n14 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 10 in unlocked:
            new_unlocked.append(2)
        if 14 in unlocked:
            new_unlocked.append(3)
        if 18 in unlocked:
            new_unlocked.append(4)

        return render(request, "art.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "14.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task14.html", {"ID": id})


def rhythm(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(18):
        file = p + "completed.txt"

        if not test_(file, 18):
            open(file, "a").write("\n18 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1, 2, 3, 4, 5, 6, 7]

        if 20 in unlocked:
            new_unlocked.append(8)
        if 21 in unlocked:
            new_unlocked.append(9)

        return render(request, "main.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "18.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task18.html", {"ID": id})


def logic(request):
    id = request.POST.get("id")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"
    unlocked = get_unlocked(p + "completed.txt")

    new = []
    if 5 in unlocked:
        new.append(1)
    if 9 in unlocked:
        new.append(2)
    if 13 in unlocked:
        new.append(3)
    if 17 in unlocked:
        new.append(4)

    return render(request, "logic.html", {"ID": id, "buttons": new})


def game(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(5):
        file = p + "completed.txt"

        if not test_(file, 5):
            open(file, "a").write("\n5 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 9 in unlocked:
            new_unlocked.append(2)
        if 13 in unlocked:
            new_unlocked.append(3)
        if 17 in unlocked:
            new_unlocked.append(4)

        return render(request, "logic.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "5.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task5.html", {"ID": id})


def twin2(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() in answers.get(9):
        file = p + "completed.txt"

        if not test_(file, 9):
            open(file, "a").write("\n9 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 9 in unlocked:
            new_unlocked.append(2)
        if 13 in unlocked:
            new_unlocked.append(3)
        if 17 in unlocked:
            new_unlocked.append(4)

        return render(request, "logic.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "9.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task9.html", {"ID": id})


def perspective(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(13):
        file = p + "completed.txt"

        if not test_(file, 13):
            open(file, "a").write("\n13 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 9 in unlocked:
            new_unlocked.append(2)
        if 13 in unlocked:
            new_unlocked.append(3)
        if 17 in unlocked:
            new_unlocked.append(4)

        return render(request, "logic.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "13.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task13.html", {"ID": id})


def sea(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(17):
        file = p + "completed.txt"

        if not test_(file, 17):
            open(file, "a").write("\n17 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1, 2, 3, 4, 5, 6, 7]

        if 20 in unlocked:
            new_unlocked.append(8)
        if 21 in unlocked:
            new_unlocked.append(9)

        return render(request, "main.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "17.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task17.html", {"ID": id})


def literature(request):
    id = request.POST.get("id")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"
    unlocked = get_unlocked(p + "completed.txt")

    new = []
    if 7 in unlocked:
        new.append(1)
    if 11 in unlocked:
        new.append(2)
    if 15 in unlocked:
        new.append(3)
    if 19 in unlocked:
        new.append(4)

    return render(request, "literature.html", {"ID": id, "buttons": new})


def dictatoroftragedies(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(19):
        file = p + "completed.txt"

        if not test_(file, 19):
            open(file, "a").write("\n19 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1, 2, 3, 4, 5, 6, 7]

        if 20 in unlocked:
            new_unlocked.append(8)
        if 21 in unlocked:
            new_unlocked.append(9)
        print(new_unlocked, unlocked)
        return render(request, "main.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "19.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task19.html", {"ID": id})


def work(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() in answers.get(7):
        file = p + "completed.txt"

        if not test_(file, 7):
            open(file, "a").write("\n7 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 11 in unlocked:
            new_unlocked.append(2)
        if 15 in unlocked:
            new_unlocked.append(3)
        if 19 in unlocked:
            new_unlocked.append(4)

        return render(request, "literature.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "7.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task7.html", {"ID": id})


def genius(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(11):
        file = p + "completed.txt"

        if not test_(file, 11):
            open(file, "a").write("\n11 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 11 in unlocked:
            new_unlocked.append(2)
        if 15 in unlocked:
            new_unlocked.append(3)
        if 19 in unlocked:
            new_unlocked.append(4)

        return render(request, "literature.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "11.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task11.html", {"ID": id})


def same(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(15):
        file = p + "completed.txt"

        if not test_(file, 15):
            open(file, "a").write("\n15 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1]

        if 11 in unlocked:
            new_unlocked.append(2)
        if 15 in unlocked:
            new_unlocked.append(3)
        if 19 in unlocked:
            new_unlocked.append(4)

        return render(request, "literature.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "15.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task15.html", {"ID": id})


def twenty(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(20):
        file = p + "completed.txt"

        if not test_(file, 20):
            open(file, "a").write("\n20 " + str(datetime.now()))

        unlocked = get_unlocked(file)

        new_unlocked = [1, 2, 3, 4, 5, 6, 7, 8]

        if 21 in unlocked:
            new_unlocked.append(9)

        return render(request, "main.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "20.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task20.html", {"ID": id})


def twentyone(request):
    id = request.POST.get("id")
    answer = request.POST.get("answer")

    if id is None:
        url = request.resolver_match.url_name
        url = url.split("/")[0]
        return redirect(url)

    p = path + "\\answers\\" + id + "\\"

    if answer is None:
        answer = "None"

    if answer.lower() == answers.get(21):
        file = p + "completed.txt"

        if not test_(file, 21):
            open(file, "a").write("\n21 " + str(datetime.now()))

        new_unlocked = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        return render(request, "end.html", {"ID": id, "buttons": new_unlocked})
    else:
        file = p + "21.txt"
        open(file, "a").write("\n" + answer)
    return render(request, "task21.html", {"ID": id})


def end(request):
    return render(request, "end.html")
