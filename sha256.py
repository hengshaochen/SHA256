# encoding: utf-8

import hashlib
import requests
from bs4 import BeautifulSoup


def sha256(url):
    # use request package to get the content information from URL
    r = requests.get(url)
    # use Beautiful Soup help me to parse the body of the HTTP response for the URL
    soup = BeautifulSoup(r.text, "lxml")
    # combine the body of URL and my_email_address
    combine = str(soup.body) + ' henrychen070@gmail.com'
    # use sha256 to encode the input string
    return hashlib.sha256(combine.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    print(sha256('https://truveris.github.io/jobs/'))