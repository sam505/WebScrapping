from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def main():
    """
    Prints out the siblings in the table rows except the title row.
    :return:
    """
    url = "http://pythonscraping.com/pages/page3.html"
    http = urlopen(url)
    obj = BeautifulSoup(http.read(), "lxml")

    for sibling in obj.find("table", {"id": "giftList"}).tr.next_siblings:
        print(sibling)

    return None


if __name__ == "__main__":
    main()
