import requests

URL = "http://econpy.pythonanywhere.com/ex/001.html"

if __name__ == '__main__':
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        regexa = '<div title="buyer-name">'
        regexb = '</div>'

        for line in content.split('\n'):
            if regexa in line:
                name = line.replace('<div title="buyer-name">','')
                name = name.replace('</div>','')
                print(name)