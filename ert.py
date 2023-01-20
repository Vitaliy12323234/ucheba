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





