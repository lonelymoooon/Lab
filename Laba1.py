#1 
x = [1, 3, 5, 6, 7, 4]
print (x[0], x[2], x[-2])

#2
a = [1, 2, 3, 4, 5, 6]
n = 28

def stepen (a, n):
    if n > len(a):
        return ('все плохо')
    else:
        return a[n]**n

print (stepen (a, n))

#3
f = 'сбербанк'
symbol = 'б'
def puk(symbol, f):
    count = 0
    for i in range (len(f)):
        if f[i] == symbol:
            count += 1
        if count >= 2:
            break
    if count == 2:
        return i
    else:
        return ('Не понел')
print (puk(symbol, f))

# 4
g = '100011100111000000000'
k = 0
rev = g[::-1]
for i in rev:
    if i == '0':
        k += 1
    elif i == '1':
        break
print(k)

#5
stroka = 'вжух и ты петух'
print (stroka[::-1])

# 6
a = [1, 1, 1, 1]
def odi(a):
    count = 0
    for i in range (0, len(a)-1):
        if a[i] == a[i + 1]:
            count += 1
        else:
            return False
    if count == len(a) and len(a) != 0:
        return True
    elif len(a) == 0:
        return 'Недостаточно элементов в списке'
    else:
        return True
print(odi(a))

#7
password = input()

def uppercase(password):
    for a in password:
        if a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
    return False

def lowercase(password):
    for a in password:
        if a in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False


def digit(password):
    for a in password:
        if a in '1234567890':
            return True
    return False


def norm_password(password):
    if len(password) < 16:
        return False

    if not uppercase(password):
        return False

    if not lowercase(password):
        return False

    if not digit(password):
        return False
    return True
print(norm_password(password))


#8
l = [7, 4, 8, 2, [3, 1, 3, [7, 2]], 3, 9, [1, 2]]
def flatten(x):
    a = []
    for i in x:
        if isinstance(i, list): #если встречается вложенный список, в наш пустой список а попадают элементы из вложенного списка
            a.extend(flatten(i))
        else:
            a.append(i) #иначе просто добавляется элемент из списка исправить
    return a
print (flatten(l))

#9
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
def max_key(x):
    count = 0
    k = 0
    for i in x:
        if x[i] > count: #если значение в словаре больше счетчика, то оно записывается в этот счетчик
            count = x[i]
            k = i # переменная к записывает в себя ключ этого значения
    return k, count
print (max_key(d))

#10
s = [1, 2, 3, 4, 1, 2, 3, 5]

def meme(x):
    d = {} #создали пустой словарик
    for i in x:
        if i in d.keys(): #если i уже есть в этом словарике, т.е. встречалось раньше
            d[i] += 1 
        else:
            d[i] = 1
    return [z for z in x if d[z] > 1] #если элемент не уникальный и встречался раньше, выводим (z пробегается по словарику)
print(meme(s))
