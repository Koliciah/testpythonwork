def value(greeting):
    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    n = input("How do you greet someone? ").strip().lower()
    print(f"${value(greeting)}")

if __name__ == "__main__":
    main()
