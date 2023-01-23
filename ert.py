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











