"""
Задание:
1) Запросить у пользователя название книги (Оно может быть не полным) и найти по нему все книги которые есть в Google Books.
2) Добавить в программу возможность фильтровать результат по
  * Автору (Не полное имя автора)
  * Заголовку (Не полный заголовок)
  * Описанию (Не полное описание)
  * Цене (Промежуток от и до)
Пользователя может несколько раз фильтровать один результат поиска в Google Books.
3) Добавить в программу возможность сохранять понравившиеся книги в файл.
5) Удалять книги из файла
6) Помечать как прочитанные книги
7) Отображать книги из файла
"""


import requests
import json

base_url = 'https://www.googleapis.com/books/v1/volumes?q=%s'


def get_google_books(search):
    resp = requests.get(base_url % search)
    json_resp = json.loads(resp.content)
    if 200 <= resp.status_code <= 299:
        return json_resp
    raise Exception(json_resp['error']['message'])


def book_to_dict(book):
    base_book = {
        'author': '',
        'title': book['volumeInfo']['title'],
        'description': '',
        'price': 0.0,
        'buy_link': None
    }
    if book['saleInfo']['saleability'] != 'NOT_FOR_SALE':
        base_book['buy_link'] = book['saleInfo']['buyLink']
        base_book['price'] = book['saleInfo']['listPrice']['amount']
        base_book['description'] = book['volumeInfo']['description']
        base_book['author'] = book['volumeInfo']['authors']
    return base_book


if __name__ == '__main__':
    json_resp = get_google_books('Алиса')
    books = [book_to_dict(x) for x in json_resp['items']]