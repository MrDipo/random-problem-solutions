from bs4 import BeautifulSoup
import requests


class DecodeNewsPage:
    def get_all_titles (url):
        r = requests.get(url)
        r_html = r.text

        soup = BeautifulSoup(r_html, features="html.parser")
        titles = soup.find_all('h3')
        titles_data = titles.text
        return titles_data


url = 'https://www.nytimes.com/'
print(DecodeNewsPage.get_all_titles(url))