import re
import sys

def convert(s):
    match = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s?(AM|PM)$", s)
    if not match:
        raise ValueError

    h1, m1, ap1, h2, m2, ap2 = match.groups()
    return f"{time(h1, m1, ap1)} to {time(h2, m2, ap2)}"



def time(hour, minutes, meridiem):
    hour = int(hour)
    minutes = int(minutes) if minutes else 0
    if hour > 12 or minutes >= 60:
        raise ValueError
    if meridiem.upper() == "AM" and hour == 12:
        hour = 0
    if meridiem.upper() == "PM" and hour != 12:
        hour += 12
    return f"{hour:02}:{minutes:02}"


def main():
    print(convert(input("Hours: ")))




if __name__ == "__main__":
    main()
