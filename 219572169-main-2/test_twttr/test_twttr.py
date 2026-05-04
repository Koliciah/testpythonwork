from twttr import shorten

def test():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TUESDAY") == "TSDY"
    assert shorten("Python") == "Pythn"
    assert shorten("1234") == "1234"
    assert shorten("python!!") == "pythn!!"

if __name__ == "__main__":
    main()

