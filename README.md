# pdmafiaboldparser

Скачать [clone and download] -> [download zip]

Пишет в консоль и в лог

## Как использовать

### Если есть python
> python parser.py %topic_url% %topic_page%

то есть например 

> python parser.py https://prodota.ru/forum/index.php?showtopic=214983 1 

топик будет отпарсен с 1 страницы

### Если нет питона :(

идем в папку dist/parser, вызываем там консоль (shift + правой кнопкой мыши) -> open command window / открыть окно команд, вводим

> parser %topic_url% %topic_page% 

то есть например

> parser https://prodota.ru/forum/index.php?showtopic=214983 1 

## TODO (сделать):
страницу можно не вводить, если нет переменной читать с первой

иногда парсится "Изменено тогда-то тогда-то", иногда не парсится, надо пофиксить, незначительно
