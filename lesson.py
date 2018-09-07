
#num_1 = int (input ("Введите первое число:" )) # создание переменной num_1, указание значения переменной: int, float, str
#num_2 = int (input ("Введите второе число:" ))
#res = int (input ( num_1 + num_2 )) #Сложение первой переменной и второй, результат записывается в переменную res
#знак *= обозначает что результат можео умножить, прибавить, разделить и тд на число указанное после знака. Также работает не только с числами но и со словами # Вывод результата умножения
#print("Результат: ", res)
# ------------------------------------------------------------------------------
#num = int (input ("Введите число: "))
#if num > 0:
#    print ("Вы ввели число больше чем 0\n ")
#elif num < 0:
#    print("вы ввели число меньше чем 0")
#elif num == 0:
#    print("Вы ввели число ранвое 0")
#else:
#    print ("Вы неизвестное число")
# Другой способ
# ------------------------------------------------------------------------------
#i = 1000
#while i > 100:
#    print (i)
#    i /= 2

# for j in 'hello world':
#    if j == 'a':
    ##   continue
    ##     break
#    print (j * 2, end = '')
# else:
#    print(" Буквы а нету в слове")
# ------------------------------------------------------------------------------
# l = []
# lis = [1, 56, 'x', 34, 2.34, ['s', 't', 'r', 'o']]
# print (lis)
# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print (a)
# l.append (23)
# l.append (34)
# b = [23, 67]
# l.extend (b)
# l.insert (1, 56) Вставить
# l.remove (34)    Удалить
# l.pop (0)
# print(l.count (34))
# print(l.index (56))
# l.sort ()
# l.reverse ()
# l.clear ()
# print (l)
# ------------------------------------------------------------------------------
# l = [34, 'sd', 56, 34.34]
# print (l[0])
# i = 0
# while i < 4:
#    print(l[i])
#    i += 1
# input ()
## item (START:STOP:STEP)
# ------------------------------------------------------------------------------
# a = (43, 56, 'sda', 23.45)
# b = [43, 56, 'sda', 23.45]
# print (a.__sizeof__())
# print (b.__sizeof__())
# a = tuple ("Hello world")
## d =  {'test' : 1}
# d = dict (short='dict', longer='dictoinary')
# d['short'] = 234
# print (d)
# d = dict ([(23, 34), (56, 87)])
# d = dict.fromkeys (['a', 'b', 'c'], 1)
# print (d)
# d = {a : a ** 2 for a in range(7)}
# print(d)
# person = {'name' : {'last_name' : 'Ivan' , 'last_name' : 'Ivanov', 'middle_name' : 'Ivanovich'}, 'adress' : ['г. Андрюшки', 'ул. Васильковская' 'д. 236, кв.12'], 'phone' : {'home.phone' : '34,67,12', 'mobile_phone' :  '8-800-800-8000'}}
# print (person)
# input()
# ------------------------------------------------------------------------------
## a = set ("hello")
## a = {'23', 32}
## a = {i ** 2 for i in range (10)}
# print (type(a))
# print (a)
# a = set ('hello')
# b = frozenset ("Qwerty")
# a.add (1)
# print (a)
# a = ['r', 's', 'w', '' 's', 'w']
# print (a)
# print (set (a))
# a = {32, 45, 43.23, 76}
## x = 45
# print (len (a)
# print (x in a)
# a = {32, 45, 43.23, 76}
# x = {67, 12, 90}
# print (a.isdisjoint (x))
# print (a == x)
# a.difference_upldae(x)
# a.update (x)
# a.intersecrion_update (x)
# a.symmetric_defference_update (x)
# a.add(23)
# a.remove(23)
# a.discard (32)
# a.pop ()
# a.clear ()
# ------------------------------------------------------------------------------
# def func (x, a) :
#    res = x + a
#    return res
 ## print (func(23, 12))
 ## print (func('Hello ', 'world'))
# def func (x):

#    def add (a):

##         return x + a
##    return add

# test = func (100)
# print (test(200))

# def func ():
#    pass
# print (func())

# def func (r, w, y = 2):
# def func (r, w, y = 2):
#    res = r + w
#    res *= y
#    return res

# print (func(5, 6, 3))
## def func (*args):
# def func (**args):
#    return args
## print (func(2.1, 'w',333))
## print (func(a=23,n=56,o=90))
# print (func (short='dict', loner='dictionary'))
# add = lambda x, y: x + y
# print(add(12,43))
# ------------------------------------------------------------------------------
# x = int (input ())
# y = int (input ())
# try:
#    res = x / y
# except ZeroDivisionError:
#    res = 0
# print (res)
# ------------------------------------------------------------------------------
# f = open ('text.txt', 'a') # Варианты работы с файлами: r - открытие на чтение, w - открытие на запись, если файла не существует, то создаётся новый, x - открытие на запись, если файла не существует, иначе исключение, a - открытие на дозапись, информация добавляется в конец файла, b - открытие в двоичном режиме,  t - открыте в текстовом режиме, + - открытие на чтение и запись.
# Форматы можно совмещать. Напирмер (rt, r+,rb)
#print(f.write('1')) # f.write, f.read
# f.write('dwd')
# f.close()
# ------------------------------------------------------------------------------
# with open('test.txt', 'wt', encoding='utf-8') as inFile:
#    num = int(input())
#    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
#    print(line)
#    inFile.write (line)
# ------------------------------------------------------------------------------
# import math  // Импортирует модуль math, отвечающий за математические функции
# print (math.e)  // Выводит на экран число 'е', обозначающее 2.718281828459045
# print (math.cos(1)) // Функция выводит косинус числа. В данном случае 1
# ----------------Функции модуля math--------------------
# math.ceil(X) – округление до ближайшего большего числа.
# math.copysign(X, Y) - возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.
# math.fabs(X) - модуль X.
# math.factorial(X) - факториал числа X.
# math.floor(X) - округление вниз.
# math.fmod(X, Y) - остаток от деления X на Y.
# math.frexp(X) - возвращает мантиссу и экспоненту числа.
# math.ldexp(X, I) - X * 2i. Функция, обратная функции math.frexp().
# math.fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.
# math.isfinite(X) - является ли X числом.
# math.isinf(X) - является ли X бесконечностью.
# math.isnan(X) - является ли X NaN (Not a Number - не число).
# math.modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.
# math.trunc(X) - усекает значение X до целого.
# math.exp(X) - eX.
# math.expm1(X) - eX - 1. При X → 0 точнее, чем math.exp(X)-1.
# math.log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.
# math.log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).
# math.log10(X) - логарифм X по основанию 10.
# math.log2(X) - логарифм X по основанию 2. Новое в Python 3.3.
# math.pow(X, Y) - XY.
# math.sqrt(X) - квадратный корень из X.
# math.acos(X) - арккосинус X. В радианах.
# math.asin(X) - арксинус X. В радианах.
# math.atan(X) - арктангенс X. В радианах.
# math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).
# math.cos(X) - косинус X (X указывается в радианах).
# math.sin(X) - синус X (X указывается в радианах).
# math.tan(X) - тангенс X (X указывается в радианах).
# math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).
# math.degrees(X) - конвертирует радианы в градусы.
# math.radians(X) - конвертирует градусы в радианы.
# math.cosh(X) - вычисляет гиперболический косинус.
# math.sinh(X) - вычисляет гиперболический синус.
# math.tanh(X) - вычисляет гиперболический тангенс.
# math.acosh(X) - вычисляет обратный гиперболический косинус.
# math.asinh(X) - вычисляет обратный гиперболический синус.
# math.atanh(X) - вычисляет обратный гиперболический тангенс.
# math.erf(X) - функция ошибок.
# math.erfc(X) - дополнительная функция ошибок (1 - math.erf(X)).
# math.gamma(X) - гамма-функция X.
# math.lgamma(X) - натуральный логарифм гамма-функции X.
# math.pi - pi = 3,1415926...
# math.e - e = 2,718281...
# ------------------------------------------------------------------------------
# import time, os, math
# import random as r
# import asdfgh
# from asdfgh import add as a , hi as h
# asdfgh.hi ()
# print (asdfgh.add (45, 15))
# -------------------------------ООП--------------------------------------------
# class Person:
#    name = 'Ivan'
#    age = 10
#
#    def set (self, name):
#
# vlad = Person ()
# vlad.name = 'Vlad'
# print (vlad.name)
#
# ivan = Person ()
# ivan.age = 45
# print (ivan.age)
# ------------------------------------------------------------------------------
# class Person:
#	name = "Ivan"
#	age = 10
#
#	def __set(self, name, age):
#		self.name = name
#		self.age = age
#
# class Student (Person):
#	course = 1
#
# igor = Student ()
# igor._Person__set ("Igor", 19)
# igor.course = 2
# print (igor.course)

# vlad = Person ()
# vlad._Person__set ("Влад", 25)
# print (vlad.name + " " + str(vlad.age))
#
# ivan = Person ()
# ivan._Person__set ("Иван", 56)
# print (ivan.age)
#
# ------------------------------------------------------------------------------
# class Person:
#	name = "Ivan"
#	age = 10
#
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#	def __set(self, name, age):
#		self.name = name
#		self.age = age
#
# class Student (Person):
#	course = 1
#	def __set(self, name, age, course):
#		self.name = name
#		self.age = age
#        self.course = course
#
# igor = Student ("19", 'Igor')
# igor._Person__set ("Igor", 19)
# igor.course = 2
# print (igor.course)
#
# vlad = Person ()
# vlad._Person__set ("Влад", 25)
# print (vlad.name + " " + str(vlad.age))
#
# ivan = Person ()
# ivan._Person__set ("Иван", 56)
# print (ivan.age)

# ------------------------------------------------------------------------------
# def decorator (func):
#    def wrapper ():
#        print('Код до выполнения функции')
#        func()
#        print ('код, который сработал после фунции')
#    return wrapper
#
# @decorator
# def show ():
#    print('Функция')
# show ()
# dec = decorator (show)
# dec ()
# input ()
input ()
