import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python','пластиковое','обеспечить']
URL = 'https://habr.com'
HEADERS = {
    'authority': 'log.strm.yandex.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://habr.com',
    'referer': 'https://habr.com/ru/all/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
def parser():
    response = requests.get(URL, headers=HEADERS)
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        preview_ = article.find(class_='tm-article-body tm-article-snippet__lead')
        preview_ = [preview.text.strip() for preview in preview_]
        datetime = article.find(class_='tm-article-snippet__datetime-published')
        href = article.find(class_='tm-article-snippet__title-link')
        link = article.find(class_='tm-article-snippet__title-link').attrs['href']
        for preview in preview_:
            for i in preview.split():
                if i in KEYWORDS:
                    return f'{datetime.text} - {href.text} - {URL}{link}'


if __name__=='__main__':                    
    print(parser())            