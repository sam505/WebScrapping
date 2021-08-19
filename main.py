from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")


def main():
    print(html.read())

    return None


if __name__ == "__main__":
    main()
