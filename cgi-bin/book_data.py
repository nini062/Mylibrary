import requests
import json
import csv
import sqlite3

books_dic = {'title':'なし',
              'authors':'なし',
                'publisher':'なし',
                  'publishedDate':'なし',
                    'description':'なし',
                      'imageLinks':"../img/no_img.png",
                        'industryIdentifiers':'なし',
                        'id':'なし'}

books_dic_keys = ['title',
              'authors',
                'publisher',
                  'publishedDate',
                    'description',
                      'imageLinks',
                        'industryIdentifiers',
                        'id']

def isbn_data(v):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + str(v)
    data = requests.get(url)

    json_data = json.loads(data.text)

    # print(type(json_data))     # json_dataの型　　dict型

    # for k, v in json_data.items():
    #     print(f'{k}:{v}')      中身の確認

    # for k in json_data:
    #     print(f'{k}')　　　　　辞書型のキーだけ確認

    books_data = json_data['items'] 
    # print(type(books_data))     itemsの中身の型　list型

    # for i in books_data:
    #     print(type(i))      itemsの中身のlistの中身の型  dict型

    for i in books_data:
        for k, v in i.items():
            # print(f'{k}:{v}')
            if k == 'volumeInfo':
                for k2, v2 in v.items():
                    # print(f'{k2}:{v2}')
                    if k2 in list(books_dic.keys()):
                        # print(f'{k2}:{v2}')
                        books_dic[k2] = v2
            elif k == 'id':
                books_dic[k] = v
        if books_dic['authors'] != 'なし':
            books_dic['authors'] = (',').join(books_dic['authors'])
        if books_dic['industryIdentifiers'] != 'なし':
            for type in books_dic['industryIdentifiers']:
                if type["type"] ==  "ISBN_13":
                   books_dic['industryIdentifiers'] = type["identifier"]
        if books_dic['imageLinks'] != '../img/no_img.png':
            books_dic['imageLinks'] = books_dic['imageLinks']['thumbnail']
      
    return books_dic


def c_data(v):

    c_data_list = []

    with open('../c_code1.csv', 'r', encoding='Shift_JIS') as f:
        my_dic1 = {val[0]:val[1] for val in csv.reader(f)}
        c_data_list.append(my_dic1[v[1]])

    with open('../c_code2.csv', 'r', encoding='Shift_JIS') as f:
        my_dic2 = {val[0]:val[1] for val in csv.reader(f)}
        c_data_list.append(my_dic2[v[2]])

    with open('../c_code34.csv', 'r', encoding='Shift_JIS') as f:
        my_dic3 = {val[0]:val[1] for val in csv.reader(f)}
        c_data_list.append(my_dic3[v[3:]])

    return c_data_list


def books_list(v):
    url = 'https://www.googleapis.com/books/v1/volumes?q=' + v + '&maxResults=20&startIndex=0'
    data = requests.get(url)

    json_data = json.loads(data.text)

    books_data = json_data['items'] 

    books_list = []
    books_dic2 = {'title':'なし',
              'authors':'なし',
                'publisher':'なし',
                  'publishedDate':'なし',
                    'description':'なし',
                      'imageLinks':"../img/no_img.png",
                        'industryIdentifiers':'なし',
                        'id':'なし'}
    for i in books_data:
        for k, v in i.items():
            # print(f'{k}:{v}')
            if k == 'volumeInfo':
                for k2, v2 in v.items():
                    # print(f'{k2}:{v2}')
                    if k2 in list(books_dic_keys):
                        # print(f'{k2}:{v2}')
                        books_dic2[k2] = v2
            elif k == 'id':
                books_dic2[k] = v
        if books_dic2['authors'] != 'なし':
            books_dic2['authors'] = (',').join(books_dic2['authors'])
        if books_dic2['industryIdentifiers'] != 'なし':
            for type in books_dic2['industryIdentifiers']:
                if type["type"] ==  "ISBN_13":
                   books_dic2['industryIdentifiers'] = type["identifier"]
                elif type["type"] ==  "OTHER":
                   books_dic2['industryIdentifiers'] = 'なし'
        if books_dic2['imageLinks'] != '../img/no_img.png':
            books_dic2['imageLinks'] = books_dic2['imageLinks']['thumbnail']
        books_list.append(books_dic2)
        books_dic2 = {'title':'なし',
              'authors':'なし',
                'publisher':'なし',
                  'publishedDate':'なし',
                    'description':'なし',
                      'imageLinks':"../img/no_img.png",
                        'industryIdentifiers':'なし',
                        'id':'なし'}
    return books_list
