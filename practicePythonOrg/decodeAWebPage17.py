from bs4 import BeautifulSoup
import requests


class DecodeNewsPage:
    def get_all_titles (url):
        r = requests.get(url)
        r_html = r.text

        soup = BeautifulSoup(r_html, features="html.parser")
        headings = soup.find_all('h3')
        for heading in headings:
            print(heading.name + ' ' + heading.text.strip())


url = 'https://www.nytimes.com/'
DecodeNewsPage.get_all_titles(url)