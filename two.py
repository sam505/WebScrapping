from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def main():
    try:
        html = urlopen("http://pythonscraping.com/pages/page1.html")
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        print("Everything is okay!")
    return None


if __name__ == "__main__":
    main()
