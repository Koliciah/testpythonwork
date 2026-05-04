import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    before_file = sys.argv[1]
    after_file = sys.argv[2]

    try:
        with open(before_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                last, first = row["name"].split(",")
                students.append({"last": last.strip(), "first": first.strip(), "house": row["house"]})
    except FileNotFoundError:
                sys.exit(f"Could not read {before_file}")

    with open(after_file, "w", newline="") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=["first",  "last",  "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)



if __name__ == "__main__":
    main()
