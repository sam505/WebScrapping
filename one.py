from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")


def main():
    """
    Strating out with BeautifulSoup
    :return:
    """
    obj = BeautifulSoup(html.read(), "lxml")
    print(obj.h1)

    return None


if __name__ == "__main__":
    main()
