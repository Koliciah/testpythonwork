# Smiley face, step 1
def convert(msg):
    return msg.replace(":)", "🙂").replace(":(", "🙁")

# Main str, step 2
def main():
    msg = input("")
    userinput = convert(msg)
    print(userinput)

main()
