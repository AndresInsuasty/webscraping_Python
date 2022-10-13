import requests
import re

URL = "http://econpy.pythonanywhere.com/ex/001.html"

if __name__ == '__main__':
    with open('econpy.html','r') as file:
        content = file.read()
        regex = '<div title="buyer-name">(.+?)</div>'
        matches = re.findall(regex, content)
        for title in matches:
            print(title)