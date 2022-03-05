# /html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[1]
import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall(
    '//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
datetime = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/time')
# создаём цикл? в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find(
        'a')
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст — это и будет нашим названием
