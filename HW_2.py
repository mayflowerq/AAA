from collections import Counter
import csv


with open('zxc.csv', 'r', encoding="utf-8") as f:
    data = f.readlines()
data = data[1:]
data = [i.strip().split(';') for i in data]


def hierarchy():
    '''иерархия'''
    a = []  #МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ
    b = []  #МАССИВ ВСЕХ КОМАНД
    c = []  #МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ И ВСЕХ КОМАНД
    d = []  #МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ И УНИКАЛЬНЫХ КОМАНД\
    for i in data:
        if i[1] not in a:
            a.append(i[1])
    for i in data:
        b.append(i[2])
    for i in a:
        for q in data:
            if q[1] == i:
                c.append(i)
                c.append(q[2])
    for i in a:
        d.append(i)
        for q in range(len(c)-1):
            if i == c[q]:
                if c[q+1] not in d:
                    d.append(c[q+1])
    for q in d:
        if q in a:
            print('Департамент', q, 'содержит следующие команды:')
        if q not in a:
            print('    ', q)
    return


def report():
    '''репорт'''
    a = []  # МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ
    b = []  # МАССИВ ВСЕХ КОМАНД
    c = []  # МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ И ВСЕХ ЗП
    d = []  # МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ И ВСЕХ ЗП (ИЗМЕНЕННЫЙ ВИД)
    e = []  # МАССИВ ВСЕХ ДЕПАРТАМЕНТОВ
    r = []  # МАССИВ ВСЕХ ДЕПАРТАМЕНТОВ И МАКСИМАЛЬНЫХ, МИНИМАЛЬНЫХ, СРЕДНИХ ЗНАЧЕНИЙ
    k = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ В ДЕПАРТАМЕНТЕ
    n = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ В ДЕПАРТАМЕНТЕ (TUPLE ЗАМЕНЕНЫ НА LIST)
    h = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ И ВСЕМИ ПОКАЗАТЕЛЯМИ ЗП
    max = 0
    min = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    sum = 0
    count = 0
    for i in data:
        if i[1] not in a:
            a.append(i[1])
    for i in data:
        e.append(i[1])
    for i in data:
        b.append(i[2])
    for i in a:
        for q in data:
            if q[1] == i:
                c.append(i)
                c.append(q[5])
    for i in a:
        d.append(i)
        for q in range(len(c)-1):
            if i == c[q]:
                d.append(c[q+1])
    for i in reversed(d):
        if i in a:
            r.append(i)
            r.append(min)
            r.append(max)
            r.append(round((sum/count), 2))
            min = 99999999999999999999999999999999
            max = 0
            sum = 0
            count = 0
        if i not in a:
            if int(i) <= min:
                min = int(i)
            if int(i) >= max:
                max = int(i)
            sum = sum + int(i)
            count = count+1
    l = dict(Counter(e))
    k = list(l.items())
    for i in k:
        i = list(i)
        n.append(i)
    for i in range(len(r)):
        if r[i] in a:
            h.append(r[i])
            h.append(r[i+1])
            h.append(r[i+2])
            h.append(r[i+3])
            for q in range(len(n)):
                if r[i] == n[q][0]:
                    h.append(n[q][1])
    print('ОТЧЕТ ПО ДЕПАРТАМЕНТАМ:')
    for i in range(len(h)):
        if h[i] in a:
            print('    Департамент '+h[i]+':')
            print('        Численность -', h[i+4], 'чел., МИН. З/П -', h[i+1], 'руб., МАКС. З/П -', h[i+2], 'руб., СРЕДН. З/П -', h[i+3], 'руб.')
    return


def writing():
    '''запись в csv'''
    a = []  # МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ
    b = []  # МАССИВ ВСЕХ КОМАНД
    c = []  # МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ И ВСЕХ ЗП
    d = []  # МАССИВ УНИКАЛЬНЫХ ДЕПАРТАМЕНТОВ И ВСЕХ ЗП (ИЗМЕНЕННЫЙ ВИД)
    e = []  # МАССИВ ВСЕХ ДЕПАРТАМЕНТОВ
    r = []  # МАССИВ ВСЕХ ДЕПАРТАМЕНТОВ И МАКСИМАЛЬНЫХ, МИНИМАЛЬНЫХ, СРЕДНИХ ЗНАЧЕНИЙ
    k = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ В ДЕПАРТАМЕНТЕ
    n = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ В ДЕПАРТАМЕНТЕ (TUPLE ЗАМЕНЕНЫ НА LIST)
    h = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ И ВСЕМИ ПОКАЗАТЕЛЯМИ ЗП
    s = []  # МАССИВ С КОЛИЧЕСТВОМ РАБОТНИКОВ И ВСЕМИ ПОКАЗАТЕЛЯМИ ЗП ДЛЯ ЗАПИСИ В ЦСВ
    max = 0
    min = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    sum = 0
    count = 0
    for i in data:
        if i[1] not in a:
            a.append(i[1])
    for i in data:
        e.append(i[1])
    for i in data:
        b.append(i[2])
    for i in a:
        for q in data:
            if q[1] == i:
                c.append(i)
                c.append(q[5])
    for i in a:
        d.append(i)
        for q in range(len(c) - 1):
            if i == c[q]:
                d.append(c[q + 1])
    for i in reversed(d):
        if i in a:
            r.append(i)
            r.append(min)
            r.append(max)
            r.append(round((sum / count), 2))
            min = 99999999999999999999999999999999
            max = 0
            sum = 0
            count = 0
        if i not in a:
            if int(i) <= min:
                min = int(i)
            if int(i) >= max:
                max = int(i)
            sum = sum + int(i)
            count = count + 1
    l = dict(Counter(e))
    k = list(l.items())
    for i in k:
        i = list(i)
        n.append(i)
    for i in range(len(r)):
        if r[i] in a:
            h.append(r[i])
            h.append(r[i + 1])
            h.append(r[i + 2])
            h.append(r[i + 3])
            for q in range(len(n)):
                if r[i] == n[q][0]:
                    h.append(n[q][1])
    myData = [["Department", "Численность", "МИН. З/П", "МАКС. З/П", "СРЕДН. З/П"]]
    for z in range(len(h)):
        if h[z] in a:
            s.append(h[z])
            s.append(h[z+4])
            s.append(h[z+1])
            s.append(h[z+2])
            s.append(h[z+3])
            myData.append(s)
            s=[]
    myFile = open('HW_2.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)


def vvod():
    a=input()
    if a=='1':
        hierarchy()
    if a=='2':
        report()
    if a=='3':
        writing()


vvod()
