import sys
from PIL import Image, ImageOps

def main():
    check_args()
    try:
        overlay_shirt(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    img_ext = (".png", ".jpg", ".jpeg")

    if not sys.argv[1].endswith(img_ext):
        sys.exit("Invalid input")
    if not sys.argv[2].endswith(img_ext):
        sys.exit("Invalid output")

    if sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
        sys.exit("Input and output have different extensions")

def overlay_shirt(before, after):
    shirt = Image.open("shirt.png")
    with Image.open(before) as img:
        final = ImageOps.fit(img, shirt.size)
        final.paste(shirt, shirt)
        final.save(after)


if __name__ == "__main__":
    main()
