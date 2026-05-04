import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line arguement")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line arguement is not a number")

    headers = {"Authorization": "Bearer c551bcf20ea825a6c044b1d1d3f48bcd25727536111250c2e94a2287117932a5"}
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("RequestException")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = price * amount

    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
