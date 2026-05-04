import inflect
import sys
from datetime import date


def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = map(int, birthday.split("-"))
        birth = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    print(birthdate(birth))

def birthdate(birth):
    present = date.today()
    difference = present - birth
    minutes = difference.days * 24 * 60

    convert = inflect.engine()
    x = convert.number_to_words(minutes, andword=" ").capitalize()
    return(f"{x} minutes")

if __name__ == "__main__":
    main()









...


if __name__ == "__main__":
    main()
