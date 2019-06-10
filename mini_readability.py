import bs4
from urllib.request import *
import os
import  urllib.parse


class PrintInFile():
    indent = 0
    line_len = 80


    def get_path(self, url):
# получение пути файла по ссылке
        if url[-1] == '/':
            url = url[:-1]
        if '://' in url:
            url = url[url.index('://')+3:]
        return os.path.join(os.path.dirname(url), os.path.basename(url).split('.')[0]+'.txt')

    def article_parser(self, url):
        # парсим страницу статьи
        url1 = 'https://lenta.ru/news/2019/06/04/peredumal/'
        url2 = 'https://www.gazeta.ru/science/2019/06/04_a_12394465.shtml'

        opener = FancyURLopener({})
        response = opener.open(url)
        if response.code == 200:
            content = response.read()

            a = bs4.BeautifulSoup(content, 'lxml')
            article = a.find_all(['h1', 'p'])

            return article
        else:
            return -1

    def print_file(self, filedir, article, url):
        # Печатаем в файл статью
        try:
            with open(filedir, 'w') as file:
                for tag_p in article:                   # перебираем все теги <p> в статье
                    to_print = ' ' * self.indent
                    words = []
                    for i in range(len(tag_p)):        # перебор содержимого тега <p>
                        if type(tag_p.contents[i]) == bs4.element.NavigableString:

                            words.extend(str(tag_p.contents[i]).split(' '))
                        elif tag_p.contents[i].name == 'a':
                            # добавление ссылки в квадратных скобках
                            words.extend(str(tag_p.contents[i].text).split(' '))
                            if '://' in str(tag_p.contents[i].attrs['href']):
                                words.append('[' + str(tag_p.contents[i].attrs['href']) + ']')
                            else:
                                words.append('[' + url.split('/')[0] + '//' + url.split('/')[2] +
                                             str(tag_p.contents[i].attrs['href']) + ']')

                        else:
                            words.extend(str(tag_p.contents[i].text).split(' '))

                    while len(words) > 0:
                        to_print += words[0] + ' '
                        if len(words) == 1 or len(to_print + words[1]) > self.line_len:
                            # если длина слов выходит за пределы заданного значения, то печатаем строку
                            print(to_print)
                            file.write(to_print + '\n')
                            to_print = ' ' * self.indent
                        words = words[1:]
                    print(to_print)
                    file.write('\n')
        except IOError:
            print('IOError')


printer = PrintInFile()

# Настройки шаблона страницы из файла
if os.path.isfile('settings.txt'):
    with open('settings.txt', 'r') as fset:
        sett = {}
        for line in fset:
            sett.update([line.split(' ')])
    printer.indent = int(sett.get('indent'))
    printer.line_len = int(sett.get('length'))


while True:
    url = input('Input url or "q" for exit: ')
    if url == 'q':
        break
    if urllib.parse.urlparse(url).hostname != None:
        urllib.parse.urlparse(url)
        article = printer.article_parser(url)
        if article == -1:
            print('Article does not exist')
        else:
            filedir = printer.get_path(url.strip())

            if not os.path.exists(os.path.dirname(filedir)):
                os.makedirs(os.path.dirname(filedir))           # создаем папки

            printer.print_file(filedir, article, url)
    else:
        print('Please input correct URL')

