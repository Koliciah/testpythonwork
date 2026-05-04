import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            print(line_count(file))
    except FileNotFoundError:
            sys.exit("File does not exist")


def line_count(file):
    count = 0
    for line in file:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        count += 1
    return count



if __name__ == "__main__":
    main()
