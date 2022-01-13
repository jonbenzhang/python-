import pytesseract
from PIL import Image

image = Image.open("./ddd.png")
# tessedit_char_whitelist识别范围
code = pytesseract.image_to_string(image, lang="eng", config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(code)

