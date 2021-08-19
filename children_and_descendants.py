from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def main():
    url = "http://pythonscraping.com/pages/page3.html"
    http = urlopen(url)
    obj = BeautifulSoup(http.read(), "lxml")

    for child in obj.find("table", {"id": "giftList"}).children:
        print(child)

    print("\n#############################################################\n")

    for descendant in obj.find("table", {"id": "giftList"}).descendants:
        print(descendant)

    return None


if __name__ == "__main__":
    main()
