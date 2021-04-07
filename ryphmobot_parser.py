from tkinter import *

import requests
from bs4 import BeautifulSoup



def proverka():
    word_dict = []
    results = []
    space = ' '
    global Text_paste
    first_url = 'http://rifme.net/r/'
    #TODO Сделать приём слова из текстового поля в TKINTER
    last_url = Entry1.get()
    slash_url = '/'
    url = first_url + last_url + slash_url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' }
    response = requests.get(url, headers=headers)
    html = response.content
    counter = 0
    soup = BeautifulSoup(html, 'lxml')
    words_with_tags = soup.findAll('li', class_='riLi')
    for item in words_with_tags:
        results.append(item.text)
    Text_paste.delete("1.0","end")
    Text_paste.insert(END, results)


root = Tk()

root.geometry('500x500')
root.title('Project by R1T1CK')

Label1 = Label(root, text="Введи сюда рифму -->", font="Calibri 17")
Label1.place(relx=.03,rely=.07)

Entry1 = Entry(root, width=20)
Entry1.place(relx=.5, rely=.09)

Button1 = Button(root ,text="Найти рифмы!" , width=13, command=proverka)
Button1.place(relx=.77, rely=.084)

Label2 = Label(root, text="А вот и твои рифмы:", font="Calibri 17")
Label2.place(relx=.26,rely=.2)

Text_paste = Text(root, width=40, height=12)
Text_paste.grid(padx=10, pady=150)
Text_paste.config(font="Calibri 17")



root.mainloop()



