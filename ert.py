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













