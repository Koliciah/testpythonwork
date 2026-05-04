import inflect

def main():
    p = inflect.engine()

    names = []

    while True:
        try:
            x = input("").strip()
            if x:
                names.append(x)
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(names)}")


main()
