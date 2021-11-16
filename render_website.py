import os
import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_rendered_page():
    name_file = 'book_page_information.json'

    with open(name_file, 'r', encoding='utf-8') as my_file:
        books_information = json.load(my_file)

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
    os.startfile(r'C:\Users\icecr\Documents\GitHub\Lesson-5.-Creating-an-online-library\main.py')#сделать путь гибким
