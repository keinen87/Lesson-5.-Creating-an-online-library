import os
import json
import jinja2
import urllib.parse
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_processed_json_file(name_file):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + '/' + name_file, 'r', encoding='utf-8') as my_file:
        file_information_json = my_file.read()

    file_information = json.loads(file_information_json)
    return file_information


def get_rendered_page(books_information):
    env = Environment(
        loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        books_information=books_information,
        )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    name_file = 'book_page_information.json'
    books_information = get_processed_json_file(name_file)
    get_rendered_page(books_information)
    os.startfile(r'C:\Users\icecr\Documents\GitHub\Lesson-5.-Creating-an-online-library\main.py')#сделать путь гибким
