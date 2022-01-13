url = 'https://zjk.bbjh.org.cn/MyCheckHandler.ashx'
import requests
import pytesseract
from PIL import Image
from io import BytesIO
r = requests.get(url)
# image = Image.open(r.content)
image = Image.open(BytesIO(r.content))
image.show()
# 转化到灰度图
imgry = image.convert('L')
# 保存图像
# imgry.save('g' + name)
# 二值化，采用阈值分割法，threshold为分割点
# out = imgry.point(table, '1')
# out.save('b' + name)
# image = r.content
# tessedit_char_whitelist识别范围
# code = pytesseract.image_to_string(image, lang="eng", config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
code = pytesseract.image_to_string(image, lang="eng", config='--oem 3 --psm 6 outputbase digits -c tessedit_char_whitelist=0123456789 tessedit_char_blacklist=ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz')
print(code)
