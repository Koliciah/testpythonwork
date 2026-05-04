galaxy = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

match galaxy.strip().lower():
    case "42":
        print("Yes")
    case "forty two":
        print("Yes")
    case "forty-two":
        print("Yes")
    case _:
        print("No")
