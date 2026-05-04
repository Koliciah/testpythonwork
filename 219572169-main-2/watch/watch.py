import re
import sys


def parse(s):
    match = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"', s)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


def main():
    html = input("HTML: ").strip()
    url = parse(html)
    if url:
        print(url)
    else:
        print("None")



if __name__ == "__main__":
    main()
