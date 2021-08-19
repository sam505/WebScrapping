from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        obj = BeautifulSoup(html.read(), "lxml")
        title = obj.body.h1

    except AttributeError as e:
        return None

    return title


def main():
    url = "http://pythonscraping.com/pages/page1.html"
    title = get_title(url)
    if title is None:
        print("No title was found")
    else:
        print(title)


if __name__ == "__main__":
    main()
