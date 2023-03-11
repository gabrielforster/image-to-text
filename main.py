from PIL import Image
import pytesseract
import numpy as np

filename = "images/sample.bmp"
image = np.array(Image.open(filename))
text = pytesseract.image_to_string(image)

print(text)
