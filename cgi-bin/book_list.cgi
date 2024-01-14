#!/usr/local/bin/python 

import cgi
import cgitb 
cgitb.enable()
import sys
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'UTF-8')
import json
import book_data
import sqlite3
import html


with open('../book_list.html', 'r', encoding='UTF-8') as f:
    book_list_html = f.readlines()
    book_list_html = ''.join(book_list_html)

with open('../book_list2.html', 'r', encoding='UTF-8') as f:
    book_list2_html = f.readlines()
    book_list2_html = ''.join(book_list2_html)

with open('../miss1.html', 'r', encoding='UTF-8') as f:
    miss1_html = f.readlines()
    miss1_html = ''.join(miss1_html)



param_data = cgi.FieldStorage()
code1 = param_data.getvalue('code1')
code2 = param_data.getvalue('code2')
code3 = param_data.getvalue('code3')

check_list = []

if code1 != None:
    code1 = html.escape(code1, quote=True)
    code1 = code1.strip()
    code1 = code1.replace(' ', '+')
    check_list.append(code1)
if code2 != None:
    code2 = html.escape(code2, quote=True)
    code2 = code2.strip()
    code2 = code2.replace(' ', '+')
    check_list.append('intitle:' + str(code2))  
if code3 != None:
    code3 = html.escape(code3, quote=True)
    code3 = code3.strip()
    code3 = code3.replace(' ', '+')
    check_list.append('inauthor:' + str(code3))
codes = ('+').join(check_list)
if len(codes) == 0:
    print('Content-type: text/html')
    print('')
    print(miss1_html.format('検索する値を入力してください'))
    exit()
else:
    try:
        isbn_dic = book_data.books_list(codes)
    except KeyError:
            print('Content-type: text/html')
            print('')
            print(miss1_html.format('該当する書籍がありません'))
            exit()
    
    book_list = []
    for i in range(len(isbn_dic)):
        list_data = book_list2_html.format(isbn_dic[i]['imageLinks'],
                            isbn_dic[i]['title'],
                            isbn_dic[i]['authors'],
                            isbn_dic[i]['publisher'],
                            isbn_dic[i]['publishedDate'],
                            isbn_dic[i]['description'][:150],
                            isbn_dic[i]['id'])
        book_list.append(list_data)
    book_list = ''.join(book_list)

    # print('Content-type: text/html')
    print('')
    print(book_list_html.format(book_list))

