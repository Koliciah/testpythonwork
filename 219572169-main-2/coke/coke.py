print("Amount Due: 50")
def main():

    amount = 50
    coin = 0
    while amount > 0:
        n = int(input("Insert Coin: "))

        if n == 25 or n == 10 or n == 5:
            amount -= n
            coin += n
        else:
            print(f"Amount Due: {amount}")
            continue

        if coin >= 50:
            print(f"Change Owed: {coin - 50}")
            break
        else:
            print(f"Amount Due: {amount}")
main()

