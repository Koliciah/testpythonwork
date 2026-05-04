def main():
    while True:
        try:
            x = input("Date: ").strip()
            if "," in x:
                month, day, year = x.replace(",", "").split()
                months = {
                    "January": 1,
                    "February": 2,
                    "March": 3,
                    "April": 4,
                    "May": 5,
                    "June": 6,
                    "July": 7,
                    "August": 8,
                    "September": 9,
                    "October": 10,
                    "November": 11,
                    "December": 12
                }
                if month not in months:
                    raise ValueError
                month = months[month]
                day = int(day)
                year = int(year)
            else:
                month, day, year = x.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                raise ValueError
        except ValueError:
            pass



main()
