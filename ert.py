# циклы
for i in range(1, 11 ,3):
# range - функция работает с числами(начальна позиция, конечная , шаг)
    print(i, end=' ')
# выыод в строчку

lang = ['c','c++']
for x in lang:
    print(x)
#работа со значениями


#break - прерывание поиска
eda = ['отбивные', 'пельмени', 'яйца']

for food in eda:
    if food == 'пельмени':
        print('я не ем пельмени')
        break
    print('вкусно')
# вместо break можно использовать continue

mas = ['c', 'a', 'w']
for masss in mas:
    print(masss, end= ' ')



# переменная while
i = 0
while i < 11:
    print(i)
    i = i + 1


a = 5
b = 2
while(a>5):
    a-=1
    b+=a
print(b)


# добавление в таблицу значений
num = int(input('введите число:'))
dats = []
while num != 0:
    dats.append(num)
    num = int(input('введите число:'))
dats.sort()
print(dats)

# добавление в таблицу что бы не повторялись значения
word = input()
spis = []
while word != '':
    if word not in spis:
        spis.append(word)
    word = input()
for w in spis:
    print(w)

# определение класса
class Person:
# объявлении функции
    def say_hello(self, message):
# определяет текущий объект сам себя
        print(message)
tom = Person()
tom.say_hello('hello')

#значения
a = 2
print(a)

a = 2 * 2
print(a)

b = a + 2
print(b)

c = b + a
print(c)

c = c + c + 3
print(c)

print(a + b + c)


#запись типа переменной
z = type(c)
print(z)

#присваивание
a = 11
a += 2
print(a)
#синтаксический сахар сокращение строк
# 2 + a = a  тоже самое  a += 2



#упровляющие символы в строчках
# /n - перненос строки
# / - табуляция
# //n - экранирование


print('abs' + 'dfg')
# сложение строк - Конкатенация

a = 1
print(str(a) + '2')
#преобразование в строку


a = 1
print(int(a) + 1)
#преобразование в число

print('sos' * 3)
#дублирование

print(len('hgfghfgjghghfjghfjhgfghjf'))
#длина строки

a = "простро_строка"
print(a[::-1])
# перевернуть слово

a = 'privet'
b = 'poka'
print('skasal %s, skasal %s' %(a, b))
print('skasal {}, skasal {}' .format(a, b))
print(f'skasal {a}, skasal {b}' )


# множественнае сохранения
a, b = "some_string_a", "some_string_b"


temp = a # сохранили в temp старое значение a
a = b # в переменную a сохранили значение b
b = temp # а в переменную b вернули сохраненное значение a

a, b = b, a
# множественное присваивание

print("Ответ на главный вопрос жизни, вселенной и всего такого -", 42)
# Ответ на главный вопрос жизни, вселенной и всего такого - 42
# вывод текста и цифр


first_name = input("Введите ваше имя:")
last_name = input("Введите вашу фамилию:")
age = input("Введите ваш возраст:")
city = input("Введите город проживания:")

# Выводим пустую строку
print("")

# Выводим приветствие, подставляя имя и фамилию пользователя,
# которые он ввел с клавиатуры
print("Привет,", first_name, last_name, "!")

# Выводим пустую строку
print("")

# Выводим фиксированный текст для удобства просмотра
print("Ваш профиль:")

# Выводим возраст и город, которые указал пользователь
print("Возраст:", age)
print("Город:", city)


#
# Целые числа	int	73, 0
# Числа с плавающей точкой	float	3.14, -2.79
# Строки	str	"Hello, world!"
# Логические переменные	bool	True, False
# Списки	list	[1,2,3,4]
# Кортежи	tuple	(‘a’,’b’,’c’)
# Словари	dict	{‘a’ : 1, ‘b’ : 2}
# Множества	set	{‘a’, 1, ‘b’, 2}


a = 3.14
b = '3.14'

print(type(a))
# <class 'float'>
print(type(b))
# <class 'str'>


#
# две группы: изменяемые и неизменяемые типы данных.
#
# Неизменяемые типы         	    Изменяемые типы
# Целые числа (int)	                  Списки (list)
# Числа с плавающей точкой (float)	 Словари (dict)
# Строки (str)	                     Множества (set)
# Логические переменные (bool)
# Кортежи (tuple)


s = "python"
print(s[0])
# p
print(s[1:4])
# yth


# картеж
date = (1, 'january', 2020)

print(date[0])
# 1
print(date[1])
# january
print(date[2])
# 2020


print(3.14/2)
# 1.57
print(round(3.14/2, 1)) # второй аргумент - желаемое количество знаков
# 1.6


#Можно извлекать не только одиночные элементы, но и целые
# подстроки, также используя индексацию:
print(s[1:4])
# ell


#Встроенная функция len() позволяет узнать длину строки:
print(len(s))
# 6



#Ряд функций позволяет определить, состоит ли строка из цифр, букв или одновременно из букв и цифр:
print(s.isdigit()) # строка состоит из цифр?
# False
print(s.isalpha()) # строка состоит из букв?
# False
print(s.isalnum()) # строка состоит из цифр и букв?
# False



#Приведённые ниже методы позволяют привести все буквы к верхнему регистру или
#(строчным буквам).
print(s.upper())
# HELLO!
print(s.lower())
# hello!

#colors = 'red blue green'
print(colors.split())
# ['red', 'blue', 'green']

#path = '/home/user/documents/file.txt'
print(path.split('/')) # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']


my_age = "I'm " + str(age)
print(my_age)
# I'm 25

age = 25

my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
print(my_age)
# I'm 25 years old



# %d, %i	        Целое число.
# %5d, %12d   	    Выделяет пространство 5 (или любое другое число) символов под это число. Выравнивание вправо, остальное пространство остается пустым.
# %05d	            Также выделяется пространство в 5 символов, но свободное пространство слева заполняется нулями.
# %o	            Число в восьмеричной системе счисления.
# %x	            Число в шестнадцатеричной системе счисления.
# %f	            Число с плавающей точкой.
# %10.2f	        Число с плавающей точкой, для которого зарезервировано пространство из 10 символов и стоит ограничение на количество знаков после запятой — 2.
# %e	            Также число с плавающей точкой, но в экспоненциальной записи.
# %c	            Код символа.
# %s	            Другая строка.
# %%	            Знак процента, если его необходимо использовать просто как символ в строке.

#Форматированные строки очень удобны для вывода даты в определённых видах записи:
day = 14
month = 2
year = 2012
print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2

# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']

# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('e')
print(letters)
# ['a', 'b', 'c', 'd', 'e']

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters.pop() # вызов метода без аргументов удаляет последний элемент списка
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f']
# был удалён последний элемент
letters.pop(0) # или можно удалить элемент по его индексу
print(letters)
# ['b', 'c', 'd', 'e', 'f']
# был удалён нулевой элемент

#  Срез	Как работает?	                                       Пример
# [:]	    Возвращает элементы полностью.	                   [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
# [2:]	Возвращает элементы списка, начиная
#         с элемента индекса 2 и до конца списка.	           [‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
# [:3]	Возвращает элементы списка от его начала
#         до элемента с индексом 3, не включая его.	           [‘a’, ‘b’, ‘c’]
# [1:4]	Объединяя предыдущие два способа, можно получить
#         элементы из середины. В данном случае, начиная с
#         индекса 1 до индекса 4, не включительно.
#         Иными словами, элементы с индексами 1,2 и 3.	       [ ‘b’, ‘c’, ‘d’]
# [::2]	Задаёт шаг, через который извлекаются элементы.	       [‘a’, ‘c’, ‘e’, ‘g’]
# [::-1]	Используя отрицательный шаг, можно
#         развернуть массив.	                               [‘g’, ‘f’, ‘e’, ‘d’, ‘c’, ‘b’, ‘a’]
#
string = input("Введите числа через пробел:")
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

# множественного присваивания
L[0], L[-1] = L[-1], L[0]

# находим сумму и добавляем её в конец списка
L.append(sum(L))

# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
L = list(map(float, input().split()))

person = {} # с помощью фигурных скобок можно создать словарь
# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}
# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'
print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

#Можно отдельно получить список ключей:
print(person.keys())
# dict_keys(['name', 'age', 'email', 'phone'])

#Или список значений:
print(person.values())
# dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])

# Из словаря аналогично спискам можно удалить объект по его ключу. Важно
# помнить, что словарь является неупорядоченным, поэтому в функцию pop()
# всегда нужно передавать ключ удаляемого объекта:
print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
person.pop('phone')
print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}

bit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}
abits = [abit1, abit2, abit3]
print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True}, {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False}, {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}]
#Этот список, по мере поступления документов, можно пополнять:
abit4 = {"ФИО" : 'Любимчиков А.Я.', "Количество баллов" : 269, "Заявление" : True}
abits.append(abit4)
print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True}, {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False}, {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}, {'ФИО': 'Любимчиков А.Я.', 'Количество баллов': 269, 'Заявление': True}]

#Или, что нам будет более полезно, множество можно создать из списка с помощью приведения типов:


#Множества в Python аналогичны математическим множествам, поэтому для них существует несколько собственных операций.
#Операция	                          Название	                        Смысл
set.union(other)	              Объединение	             Возвращает множество, состоящее из элементов set и other.
set.intersection(other)           Пересечение	             Возвращает множество, состоящее из элементов, которые встречаются и в set, и в other.
set.difference(other)	          Разность	                 Возвращает множество элементов set, которые не встречаются в other.
set.symmetric_difference(other)	  Симметричная разность	     Возвращает множество элементов, встречающиеся в одном из множеств, но не в обоих одновременно.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
sum = int(input('Введите сумму:'))
stavka = per_cent.values()
deposit = stavka * sum
print(deposit)








