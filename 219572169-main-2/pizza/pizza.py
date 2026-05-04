import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open((sys.argv[1]), "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row = list(reader)
            if row is None:
                row = []

    except FileNotFoundError:
            sys.exit("File does not exist")

    print(tabulate(row, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()

