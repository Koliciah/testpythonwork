def main():
    grocery_list = {}
    while True:
            try:
                x = input().strip().lower()
                if x in grocery_list:
                    grocery_list[x] += 1
                else:
                    grocery_list[x] = 1
            except EOFError:
                print()
                break
    for x in sorted(grocery_list):
        print(grocery_list[x], x.upper())




main()
