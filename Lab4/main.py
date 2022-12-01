from random import randint
import time

igrok1 = input('Введите имя 1-го играющего: ')
igrok2 = input('Введите имя 2-го играющего: ')
rounds = input('Введите количество раундов: ')
score1 = 0
score2 = 0
res = []

for i in range(int(rounds)):
    print('Кубик бросает ' + igrok1 + '... ', end='')
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    score1 += n1

    print('Кубик бросает ' + igrok2 + '... ', end='')
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    score2 += n2

    if n1 > n2:
        print(igrok1 + ' выиграл раунд ' + str(i+1))
        res.append(igrok1)
    elif n2 > n1:
        print(igrok2 + ' выиграл раунд ' + str(i+1))
        res.append(igrok2)
    else:
        print('Ничья в раунде ' + str(i+1))
        res.append(0)

wins1 = res.count(igrok1)
wins2 = res.count(igrok2)

print('Счёт ' + igrok1 + ': ' + str(score1) + 'очков, выиграно ' + str(wins1) + 'раундов')
print('Счёт ' + igrok2 + ': ' + str(score2) + 'очков, выиграно ' + str(wins2) + 'раундов')

if score1 > score2:
    print(igrok1 + ' выиграл по количеству очков')
elif score2 > score1:
    print(igrok2 + ' выиграл по количеству очков')
else:
    print('Ничья по количеству очков')

if wins1 > wins2:
    print(igrok1 + ' выиграл большее количество раундов')
elif wins2 > wins1:
    print(igrok2 + ' выиграл большее количество раундов')
else:
    print('Оба игрока выиграли одинаковое количество раундов')
