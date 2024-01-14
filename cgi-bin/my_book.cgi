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

with open('../my_book_data.html', 'r', encoding='UTF-8') as f:
    my_book_data_html = f.readlines()
    my_book_data_html = ''.join(my_book_data_html)

with open('../../../csv/book_list.csv', 'r', encoding='UTF-8') as f:
    my_list = [val for val in csv.reader(f)]

param_data = cgi.FieldStorage()
id_num = param_data.getvalue('id')
id_num = html.escape(id_num, quote=True)

for i in my_list:
    if i[0] == id_num:
        print('')
        print(my_book_data_html.format(i[1],
                                i[2],
                                i[3],
                                i[4],
                                i[5],
                                i[6],
                                i[7],
                                i[8],
                                i[9],
                                i[10],
                                i[11],
                                i[12]))
        exit()