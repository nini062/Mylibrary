#!/usr/local/bin/python 

import csv
import cgi
import cgitb 
cgitb.enable()
import sys
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'UTF-8')
import json
import requests
import book_data

with open('book_list.csv', 'r', encoding='UTF-8') as f:
    my_list = [val for val in csv.reader(f)]

with open('../book_list.html', 'r', encoding='UTF-8') as f:
    book_list_html = f.readlines()
    book_list_html = ''.join(book_list_html)

with open('../my_book_list.html', 'r', encoding='UTF-8') as f:
    my_book_list_html = f.readlines()
    my_book_list_html = ''.join(my_book_list_html)

books_list = []
for i in my_list:
    list_data = my_book_list_html.format(i[1],
                        i[2],
                        i[3],
                        i[4],
                        i[5],
                        i[6][:150],
                        i[7],
                        i[8],
                        i[9],
                        i[10],
                        i[11],
                        i[0],)
    books_list.append(list_data)
books_list = ''.join(books_list)

print('Content-type: text/html')
print('')
print(book_list_html.format(books_list))

