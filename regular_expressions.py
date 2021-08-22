from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://pythonscraping.com/pages/page3.html"
html = urlopen(url)
obj = BeautifulSoup(html, "lxml")


def main():
    images = obj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    print(images)
    for image in images:
        print(image["src"])
    return None


if __name__ == "__main__":
    main()
