import html2text as ht  # pip install html2text
import requests
import re
import bs4
import base64


def download_pics(url):
    img = ""
    try:
        img = requests.get(url)
    except:
        return url
    img_data = img.content

    with open("a" + ".jpg", "wb")as f:
        f.write(img_data)
    b = base64.encodebytes(img_data)
    s = b.decode()
    img_base64 = 'data:image/jpeg;base64,%s' % s
    return img_base64


npurl = "https://www.cnblogs.com/wupeiqi/articles/6229292.html"
text_maker = ht.HTML2Text()
text_maker.bypass_tables = False
htmlfile = requests.get(npurl)  # 网页网址
htmlfile.encoding = 'utf-8'
title = re.findall('<title>(.+)</title>', htmlfile.text)
htmlpage = htmlfile.text
# 转base64内嵌到markdown
# soup = bs4.BeautifulSoup(htmlfile.text, "lxml")
# imgs = soup.find_all("img")
# for i in imgs:
#     img_url = i.get("src")
#     htmlpage = htmlpage.replace(img_url, download_pics(img_url))
if title:
    title = title[0]
else:
    title = "没有title"
text = text_maker.handle(htmlpage)
# print(text)
# md = text.split('#')
with open(title + ".md", "w")as f:
    f.write(text)
