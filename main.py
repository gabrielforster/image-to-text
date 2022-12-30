from PIL import Image
import pytesseract as pt
import re

def main():
    img3 = Image.open("nota-fiscal.jpeg")
    text3 = pt.image_to_string(img3, lang='por')

    pattern = re.compile("VALOR: (\d+),(\d+)")
    match = pattern.findall(text3)

    print(",".join(match[0]))

if __name__ == "__main__":
    main()
