#!/usr/local/bin/python 

import cgi
import cgitb 
cgitb.enable()
import sys
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'UTF-8')
import json
import book_data
import html

with open('../book_data.html', 'r', encoding='UTF-8') as f:
    book_data_html = f.readlines()
    book_data_html = ''.join(book_data_html)

with open('../miss1.html', 'r', encoding='UTF-8') as f:
    miss1_html = f.readlines()
    miss1_html = ''.join(miss1_html)

param_data = cgi.FieldStorage()
code4 = param_data.getvalue('code4')

if code4 is None:
    id_num = param_data.getvalue('id')
    id_num = html.escape(id_num, quote=True)

    id_num_dic = book_data.books_list(id_num)

    for i in range(len(id_num_dic)):
        if id_num_dic[i]['id'] == id_num:
            isbn_dic = id_num_dic[i]

else:
    code4 = html.escape(code4, quote=True)
    if code4.isdecimal()==False:
        print('Content-type: text/html')
        print('')
        print(miss1_html.format('ISBNには１３桁の数値を入力してください'))
        exit()

    else:
        try:
            isbn_dic = book_data.isbn_data(code4)
        except KeyError:
            print('Content-type: text/html')
            print('')
            print(miss1_html.format('入力されたISBNは登録がありません'))
            exit()

# print('Content-type: text/html')
print('')
print(book_data_html.format(isbn_dic['imageLinks'],
                            isbn_dic['title'],
                            isbn_dic['authors'],
                            isbn_dic['publisher'],
                            isbn_dic['publishedDate'],
                            isbn_dic['description'],
                            isbn_dic['id']
                            ))