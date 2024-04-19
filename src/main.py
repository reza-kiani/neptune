import requests

file_path = r"C:\Users\mysel\Desktop\Python Projects\neptune\src\urls.txt"


def get_urls():
    with open(file_path, 'r') as f:
        while True:
            line = f.read()
            return line


try:
    for url in get_urls().split("\n"):
        r = requests.get(url)
        print("{:s} = ".format(url), r.status_code)
except Exception as ex:
    print(ex)
