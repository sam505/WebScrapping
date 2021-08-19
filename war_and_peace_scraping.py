from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def main():
    """
    Finding all names in the page that are in green
    :return:
    """
    url = "http://pythonscraping.com/pages/warandpeace.html"
    try:
        http = urlopen(url)
        obj = BeautifulSoup(http.read(), "lxml")
        names = obj.findAll("span", {"class": "green"})
        for name in names:
            print(name.get_text())
    except HTTPError as e:
        print(e)

    return None


if __name__ == "__main__":
    main()
