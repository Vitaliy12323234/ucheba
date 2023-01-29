per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
stavka = per_cent.values()
summa = float(input('Введите сумму:'))
for procent in stavka:
    deposit = (round(procent / 100 * summa))
    print('Вы заработаете:', deposit)
for max_stavka in stavka:
    max_stav = max(stavka)
    max_deposit = (round(max_stav / 100 * summa))
    print('Максимальная сумма', max_deposit)