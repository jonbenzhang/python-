import requests


def down_file(url_file):
    r = requests.get(url_file, stream=True)
    f = open("file_path", "wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
