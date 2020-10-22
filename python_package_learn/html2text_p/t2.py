import requests, os
import base64

def download_pics(url):
    img = requests.get(url)
    img_data = img.content

    with open("a" + ".jpg", "wb")as f:
        f.write(img_data)
    b = base64.encodebytes(img_data)
    s = b.decode()
    img_base64 = 'data:image/jpeg;base64,%s'%s
    return img_base64


if __name__ == '__main__':
    # img_url = "https://img-blog.csdn.net/20170112103344762?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMzM0NTU0NDc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"
    # download_pics(img_url)
    a = "qweasd"
    b = a.replace("qw","zhagn")
    print(b)
    print(a)