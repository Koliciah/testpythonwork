import emoji

def main():
    n = input("Input: ")
    print(emoji.emojize(f"Output: {n}", language='alias'))


main()
