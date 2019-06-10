# mini_readability
Программа написана как тестовое задание на позицию Разработчик Python в компанию "Тензор"

ОПИСАНИЕ АЛГОРИТМА

Извлечение необходимой информации из статьи происходит с помощью библиотеки BeautifulSoup4. 
Создан класс PrintFile с переменными indent = 0 (отступ) и line_len = 80 (длина строки). 
Данные могут быть введены в отдельном файле settings.txt

1) Функция get_path 
(возвращает путь по введенной url как показано в примере 
http://lenta.ru/news/2013/03/dtp/index.html => [CUR_DIR]/lenta.ru/news/2013/03/dtp/index.txt)

2) функция article_parser
Алгоритм был протестирован на двух новостных сайтах:
        url1 = 'https://lenta.ru/news/2019/06/04/peredumal/'
        url2 = 'https://www.gazeta.ru/science/2019/06/04_a_12394465.shtml'
Для большинства сайтов заголовок статьи находится в теге h1,
а тело статьи в теге p, поэтому для дальнейшей работы были выбраны
именно эти теги. Возвращает article элемент bs4 с найденными тегами p и h1,
если ответ от запроса к URL равен 200, иначе -1.
 
3) функция print_file
Происходит обработка статьи по техническому заданию и сохранение в файл.

Программа будет запрашивать URL, до тех пор пока не будет введен символ "q".
Если URL задан некорректно или без http://, программа напишет "Please input
correct URL". Если статьи уже не существует, программа сообщит об этом.
