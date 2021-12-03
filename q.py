import os
import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


name_file = 'book_page_information.json'

with open(name_file, 'r', encoding='utf-8') as my_file:
    books_information = json.load(my_file)

q = (list(chunked(books_information, 2)))
for i in q:
    print('--')
    print('--')
    print(i)