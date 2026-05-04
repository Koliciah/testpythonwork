import re
import sys

def validate(ip):
    return re.fullmatch(r"^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$", ip) is not None


def main():
    try:
        ip = input("IPv4 Address: ").strip()
    except EOFError:
        sys.exit(1)

    print(validate(ip))



if __name__ == "__main__":
    main()
