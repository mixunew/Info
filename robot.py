import requests
import time
import urllib.robotparser

url = "https://example.com"

# check robots.txt
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://example.com/robots.txt")
rp.read()

if rp.can_fetch("*", url):

    print("Crawling allowed")

    # delay to avoid server overload
    time.sleep(2)

    response = requests.get(url)

    print("Page fetched successfully")
    print("Page length:", len(response.text))

else:
    print("Crawling not allowed by robots.txt")