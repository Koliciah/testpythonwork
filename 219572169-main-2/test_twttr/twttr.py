def shorten(word):
    output = ""
    for c in word:
        if c.lower() not in "aeiou":
            output += c
    return output

def main():
    i = input("Input: ")
    print ("Output:", shorten(i))




if __name__ == "__main__":

    main()
