import time
from random import randint


def start():
    i1 = input('Введите имя 1-го играющего: ')
    i2 = input('Введите имя 2-го играющего: ')
    r = input('Введите количество раундов: ')
    rs = []
    return i1, i2, r


def game(igrok1, igrok2, rounds):
    s1 = 0
    s2 = 0
    res = []
    for i in range(int(rounds)):
        print('Кубик бросает ' + igrok1 + '... ', end='')
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        s1 += n1

        print('Кубик бросает ' + igrok2 + '... ', end='')
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        s2 += n2

        if n1 > n2:
            print(igrok1 + ' выиграл раунд ' + str(i + 1))
            res.append(igrok1)
        elif n2 > n1:
            print(igrok2 + ' выиграл раунд ' + str(i + 1))
            res.append(igrok2)
        else:
            print('Ничья в раунде ' + str(i + 1))
            res.append(0)

    w1 = res.count(igrok1)
    w2 = res.count(igrok2)
    return s1, s2, w1, w2


def winners(score1, score2, wins1, wins2, igrok1, igrok2):
    print('Счёт ' + igrok1 + ': ' + str(score1) + ', ракндов выиграно ' + str(wins1))
    print('Счёт ' + igrok2 + ': ' + str(score2) + ', ракндов выиграно ' + str(wins2))

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
    return
