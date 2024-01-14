#!/usr/local/bin/python 

import cgi
import cgitb 
cgitb.enable()
import sys
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'UTF-8')
import json
import book_data
import csv
import html

havecheck_dic = {"hc1":'持ってる', "hc2":'持ってない'}
readcheck_dic = {"rc1":'未読', "rc2":'途中', "rc3":'既読'}

param_data = cgi.FieldStorage()
code5 = param_data.getvalue('code5')
if code5 != None:
    code5 = html.escape(code5, quote=True)
havecheck = param_data.getvalue('havecheck')
havecheck = html.escape(havecheck, quote=True)
readcheck = param_data.getvalue('readcheck')
readcheck = html.escape(readcheck, quote=True)
thoughts = param_data.getvalue('thoughts')
if thoughts != None:
    thoughts = html.escape(thoughts, quote=True)

id_num = param_data.getvalue('hidden')
id_num = html.escape(id_num, quote=True)

id_num_dic = book_data.books_list(id_num)

for i in range(len(id_num_dic)):
    if id_num_dic[i]['id'] == id_num:
        isbn_dic = id_num_dic[i]

if code5 == None:
    c_list = ['入力なし', '入力なし', '入力なし']

else:
    c_list = book_data.c_data(code5)

library_list = [id_num,                      # ISBMも後で足す
                isbn_dic['imageLinks'],
                isbn_dic['title'],
                isbn_dic['authors'],
                isbn_dic['publisher'],
                isbn_dic['publishedDate'],
                isbn_dic['description'],
                c_list[0],
                c_list[1],
                c_list[2],
                havecheck_dic[havecheck],
                readcheck_dic[readcheck],
                thoughts]

with open('../../../csv/book_list.csv', 'a', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(library_list)


with open('../book_library.html', 'r', encoding='UTF-8') as f:
    book_library_html = f.readlines()
    book_library_html = ''.join(book_library_html)

print('Content-type: text/html')
print('')
print(book_library_html.format(isbn_dic['title']))