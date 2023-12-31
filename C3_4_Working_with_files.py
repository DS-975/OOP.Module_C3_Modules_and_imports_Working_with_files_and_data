﻿C3.4. Работа с файлами

В данном юните мы с вами поговорим об основных принципах работы с 
файлами в языке Python. Какие встроенные методы используются для 
открытия, закрытия, чтения, построчного чтения и т. д.

Путь к файлу

Путь (англ. path) — набор символов, показывающий расположение файла 
                                или каталога в файловой системе.

В операционных системах UNIX разделительным знаком при записи пути 
является «/», в Windows — «\». Эти знаки служат для разделения названия 
каталогов, составляющих путь к файлу. Все вы видели, например, такой 
путь на ОС Windows: C:\Program Files. Это и есть путь до папки Program Files.

Существует два типа пути:

 * абсолютный,

 * относительный.

Абсолютный путь всегда считается от «корня», той папки, откуда потом
 вырастают все остальные папки. Для Windows это диск С:, D: и т. д., 
для Unix это “/” (слеш). Абсолютный путь всегда уникальный.

Абсолютный путь — это путь, который указывает на одно и то же место 
                                   в файловой системе, вне зависимости от текущего 
                                   рабочего каталога или других обстоятельств. 
                                   Его ещё называют полным.

Относительный путь — это путь по отношению к текущему рабочему 
                                        каталогу пользователя.

Чтобы поработать с путями есть модуль os. Функция os.chdir() позволяет 
нам изменить директорию, которую мы в данный момент используем. 
Если вам нужно знать, какой путь вы в данный момент используете, 
для этого нужно вызвать os.getcwd().

ПРИМЕЧАНИЕ: Все дальнейшие пути указаны для конкретной машины на 
ОС Linux. У вас эти результаты будут отличаться.

# получить текущий путь
start_path = os.getcwd()
print(start_path)  # /home/nbuser/library

# Далее попробуем подняться на директорию выше:

os.chdir("..")  # подняться на один уровень выше
os.getcwd()  # '/home/nbuser'

# Теперь вернемся в ту директорию, из которой стартовали. 
# Изначально мы сохраняли её в переменной start_path.

os.chdir(start_path)
os.getcwd()  # '/home/nbuser/library'

# С помощью функции os.listdir() можно получить весь список файлов, 
# находящихся в директории. Если не указать никаких аргументов, 
# то будет взята текущая директория.

# список файлов и директорий в папке
import os
 
print(os.listdir())  # ['SnapchatLoader', 'FBLoader', 'tmp.py', '.gitignore', 'venv', '.git']
 
if 'tmp.py' not in os.listdir():
   print("Файл отсутствует в данной директории")

Для того, чтобы склеивать пути с учётом особенностей ОС, 
следует использовать функцию os.path.join(). Это связано с тем, что 
в разных операционных системах могут быть разные разделители каталогов, 
например, в ОС Windows этим разделителем является «\», а в Linux «/», 
как мы и говорили в начале юнита. Поэтому чтобы поиск файла 
проходил гладко на обоих системах (ведь ваш скрипт могут запускать 
на любой системе в связи с кросс-платформенностью Python), лучше 
всё-таки использовать join.

# соединяет пути с учётом особенностей операционной системы
print(start_path)
print(os.path.join(start_path, 'test'))

3.4.1

 * Путь, который указывает на одно и то же место в файловой системе, 
    вне зависимости от текущего рабочего каталога или других обстоятельств, 
    называется:
                       Ответ: абсолютный путь 

 * Путь по отношению к текущему рабочему каталогу пользователя, 
    называется:
                       Ответ: относительный путь 


3.4.2

Соотнесите абсолютные и относительные пути.
---------------------------------------------------------------------------------------------------------------
|                    Абсолютный путь                   |               Относительный путь               | 
|---------------------------------------------------------|-----------------------------------------------------|
|     C:\PychermProjects\airflow_simpleapp     |                   test/packA/a1.py                   | 
|---------------------------------------------------------|-----------------------------------------------------|
|                    /packB/__init__.py                    |                       tmp_fale.txt                       |
|---------------------------------------------------------|-----------------------------------------------------|
| D:\Documents\Newslettest\Summer2018.pdf |    2020\skillfactory_python\module_13     | 
---------------------------------------------------------------------------------------------------------------



3.4.3

Задание на самопроверку.

Сделайте функцию, которая принимает от пользователя путь и выводит всю 
информацию о содержимом этой папки. Для реализации используйте 
функцию встроенного модуля os.walk(). Если путь не указан, то 
сравнение начинается с текущей директории.

Ответ:

import os

def walk_desc(path=None):
   start_path = path if path is not None else os.getcwd()

   for root, dirs, files in os.walk(start_path):
       print("Текущая директория", root)
       print("---")
      
       if dirs:
           print("Список папок", dirs)
       else:
           print("Папок нет")
       print("---")
      
       if files:
           print("Список файлов", files)
       else:
           print("Файлов нет")
       print("---")
      
       if files and dirs:
           print("Все пути:")
       for f in files:
           print("Файл ", os.path.join(root, f))
       for d in dirs:
           print("Папка ", os.path.join(root, d))
       print("===")

walk_desc()

Работа с файлами

Python «из коробки» располагает достаточно широким набором инструментов
для работы с файлами. Для того чтобы начать работать с файлом, 
надо его открыть с помощью команды специальной функции open.

f = open('path/to/file', 'filemode', encoding='utf8')

Результатом этой операции будет файл, в котором указатель текущей 
позиции поставлен на начало или конец файла.

Перед тем как начнём разбирать аргументы, хотелось бы заранее отметить, 
что указателем называется скорее метка, которая указывает на определённое 
место в файле. Указателей в классическом понимании программиста, 
как например, в C или C++ в Python нет!

Давайте по порядку разберем все аргументы:

1. path/to/file — путь к файлу может быть относительным или абсолютным. 
    Можно указывать в Unix-стиле (path/to/file) или в Windows-стиле (path\to\file).

2. filemode — режим, в котором файл нужно открывать.

Записывается в виде строки, состоит из следующих букв:

 * r — открыть на чтение (по умолчанию);

 * w — перезаписать и открыть на запись (если файла нет, то он создастся);

 * x — создать и открыть на запись (если уже есть — исключение);

 * a — открыть на дозапись (указатель будет поставлен в конец);

 * t — открыть в текстовом виде (по умолчанию);

 * b — открыть в бинарном виде.

3. encoding — указание, в какой кодировке файл записан (utf8, cp1251 и т. д.) 
    По умолчанию стоит utf-8.

Открытие файла на запись является блокирующей операцией, то есть она 
останавливает работу нашей программы до того, пока файл не откроется.

Теперь давайте поговорим про то, как записывать какую-либо информацию 
в файл.

При открытии файла внутри него ставится указатель текущей позиции 
для чтения. При открытии в режиме чтения или записи указатель ставится 
на начало, в режиме a (добавление новых записей в конец файла) — в конец.

Откроем файл на запись и с помощью метода write запишем в него строку. 
В качестве результата метод write возвращает количество записанных символов.

f = open('test.txt', 'w', encoding='utf8')
 
# Запишем в файл строку
f.write("This is a test string\n")
f.write("This is a new string\n")

После вызова команды write ваши данные не сразу попадут и сохранятся 
в файл. Связанно это с особенностями внутренней работы операционных
систем. Если для вас критично своевременно попадание информации на 
жесткий диск компьютера, то после записи вызывайте f.flush() или 
закрывайте файл. Закрыть файл, можно с помощью метода close().

# обязательно нужно закрыть файл иначе он будет заблокирован ОС
f.close()

# Теперь давайте посмотрим как читать данные из файла.

# Откроем файл для чтения, в который только что записали две строки:

f = open('test.txt', 'r', encoding='utf8')
Вот его содержимое на жестком диске:

This is a test string
This is a new string

# После того, как файл открыт для чтения, мы можем читать из него данные.

# f.read(n) — операция, читающая с текущего места n символов, если файл 
# открыт в t режиме, или n байт, если файл открыт в b режиме, и 
# возвращающая прочитанную информацию.

print(f.read(10))  # This is a 

# После прочтения указатель на содержимое остается на той позиции, 
# где чтение закончилось. Если n не указать, будет прочитано «от печки»,
# т. е. от текущего места указателя и до самого конца файла.

# считали остаток файла
f.read()  # test string\nThis is a new string\n

# После работы обязательно закрываем файл:

# обязательно закрываем файл
f.close()

Чтение и запись построчно

Зачастую с файлами удобнее работать построчно, поэтому для этого есть 
отдельные методы:

 * writelines — записывает список строк в файл;

 * readline — считывает из файла одну строку и возвращает её;

 * readlines — считывает из файла все строки в список и возвращает их.

Метод f.writelines(sequence) не будет сам за вас дописывать символ конца 
строки (‘\n’). Поэтому при необходимости его нужно прописать вручную.

f = open('test.txt', 'a', encoding='utf8')  # открываем файл на дозапись
 
sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence) # берет строки из sequence и записывает в файл (без переносов)
 
f.close()

# Попробуем теперь построчно считать файл с помощью readlines:

f = open('test.txt', 'r', encoding='utf8')
 
print(f.readlines())  # считывает все строки в список и возвращает список
 
f.close()

# Метод f.readline() возвращает строку (символы от текущей позиции до 
# символа переноса строки):

f = open('test.txt', 'r', encoding='utf8')
 
print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  #  is a new string
 
f.close()

Подробный материал с разбором работы с файловой системой 
представлен в скринкасте.


Файл как итератор

Объект файл является итератором, поэтому его можно использовать в цикле for.

Для чего это нужно?

Итераторы представляют собой такой объект, который вычисляет какие-то 
действия на каждом шаге, а не все сразу. На примере файла это выглядит, 
примерно, так. Предположим, у вас есть огромный текстовый файл, 
который весит несколько гигабайт. Если попытаться разом считать его 
полностью с помощью f.readlines(), то он будет загружен в вашу программу, 
в то время как переменная, в которую будет записан файл, станет весить так 
же, как и объём считанного файла.

В большинстве задач с обработкой текста весь он разом не нужен, 
поэтому мы можем, например, считывать его построчно, обрабатывать 
строку и забывать из нашей программы, чтобы считать новую. 
Тогда весь файл огромного объема не будет попросту висеть в памяти 
компьютера.

Не стоит считывать файл полностью, в большинстве задач с обработкой 
текста весь файл разом читать не требуется. В таком случае с файлом 
работают построчно.

f = open('test.txt')  # можно перечислять строки в файле
for line in f:
    print(line, end='')
    
# This is a test string
# This is a new string
# other string
# 123
# test test
 
f.close()

Цикл for, как мы помним, это цикл который перебирает по очереди.

Менеджер контекста with

После работы с файлом его нужно закрыть с помощью метода close(). 
Обработчик данного файла освобождается для операционной системы 
(если файл был открыт для записи), и другие приложения могут получать 
к нему доступ. Если не закрыть файл явно, то информация, записываемая 
в него, может быть утеряна, или же сам файл может повредиться.

Для явного указания места работы с файлом, а также чтобы не забывать 
закрывать файл после обработки, существует менеджер контекста with.

# В блоке менеджера контекста открытый файл «жив» и с ним можно работать, при выходе из блока - файл закрывается.
with open("test.txt", 'rb') as f:
    a = f.read(10)
    b = f.read(23)
 
f.read(3)  # Error!

Тело менеджера контекста определяется одним отступом вправо 
относительно отступов ключевого слова with. Менеджер контекста 
неявно вызывает закрытие файла после работы, что освобождает 
вас от забот о том, закрыли ли вы файл или нет. Закрытие файла 
происходит при любом стечении обстоятельств, даже если внутри 
with будет ошибка. В дальнейшем мы научимся писать собственные 
структуры, работающие похожим образом.

3.4.4

Задание на самопроверку.

Создайте любой файл на операционной системе под название input.txt и 
построчно перепишите его в файл output.txt.

Решение:

with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in input_file:
           output_file.write(line)

3.4.5

Задание на самопроверку.

Дан файл numbers.txt, компоненты которого являются действительными 
числами (файл создайте самостоятельно и заполните любыми числам, 
в одной строке одно число). Найдите сумму наибольшего и наименьшего 
из значений и запишите результат в файл output.txt.

Решение:

filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
   min_ = max_ = float(f.readline())  # считали первое число
   for line in f:
       num =  float(line)
       if num > max_:
           max_ = num
       elif num < min_:
           min_ = num

   sum_ = min_ + max_

with open(output, 'w') as f:
   f.write(str(sum_))
   f.write('\n')

3.4.6

В текстовый файл построчно записаны фамилии и имена учащихся класса 
и их оценки за контрольную. Выведите на экран всех учащихся, чья оценка 
меньше 3 баллов. Cодержание файла:

Иванов О. 4
Петров И. 3
Дмитриев Н. 2
Смирнова О. 4
Керченских В. 5
Котов Д. 2
Бирюкова Н. 1
Данилов П. 3
Аранских В. 5
Лемонов Ю. 2
Олегова К. 4

Решение:

with open('input.txt', encoding="utf8") as file:
    for line in file:
        points = int(line.split()[-1])
        if points < 3:
            name = " ".join(line.split()[:-1])
            print(name)


3.4.7
Задание на самопроверку.

Выполните реверсирование строк файла (перестановка строк файла в 
обратном порядке).

Решение:

with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)

