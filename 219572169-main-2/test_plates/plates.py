def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    middle_digit = False
    for m in s:
        if m.isdigit():
            if not middle_digit:
                if m == "0":
                    return False
                middle_digit = True
        else:
            if middle_digit:
                return False
    if not s.isalnum():
        return False

        
    return True


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        return("Valid")
    else:
        return("Invalid")

if __name__ == "__main__":
    main()
