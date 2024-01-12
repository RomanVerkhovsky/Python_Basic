import math
# 1.24
# a)
a = float(input("Дана функция x = sqrt((2a + sin|3a|) / 3,56), что бы вычислить ее введите значение a >> "))
x = math.sqrt(((2*a) + math.sin(math.fabs(3*a))) / 3.56)
print("При a =", a, ",", "x =", x)

# b)
x = float(input("Дана функция y = sin((3.2 + sqrt(1 + x)) / |5x|), что бы вычислить ее введите значение x >> "))
y = math.sin((3.2 + math.sqrt(1 + x)) / math.fabs(5 * x))
print("При x =", x, ",", "y =", y)

# 1.30
print("Дана функция z = x**3 - 2.5xy + 1.78x**2 - 2.5y + 1, что бы вычислить ее:")
x = float(input("Введите значение x >> "))
y = float(input("Введите значение y >> "))
z = math.pow(x, 3) - (2.5 * x * y) + (1.78 * math.pow(x, 2)) - (2.5 * y) + 1
print("При x =", x, ",", "y =", y, ",", "z =", z)

# 1.31
# z - число чисел
x = int(input("Задайте первое целое число >> "))
y = int(input("Задайте второе целое число >> "))
z = 2
a = (x + y) / z
g = math.pow((x * y), (1 / z))
print("Среднее арифметическое =", a)
print("Среднее геометрическое =", g)

# 2.12
x = int(input("Введите трехзначное число >> "))
first = x // 100
second = (x // 10) % 10
third = x % 10
a = first + second + third
b = first * second * third
print("Число единиц в нем:", third)
print("Число десятков в нем:", second)
print("Сумма его цифр:", a)
print("Произведение его цифр", b)

# 2.17
x = int(input("Введите трехзначное число >> "))
first = x // 100
second = (x // 10) % 10
third = x % 10
time = second
second = third
third = time
number_str = str(first) + str(second) + str(third)
number = int(number_str)
print("Число полученное при перестановке второй и третьей цифр заданного числа:", number)

# 3.9
# а)true; б)true; в)true

# 3.12
# а) true
x = 1
y = -1
z = (x**2) - (y**2) <= 0
print("При x = 1, y = -1, выражение x**2 - y**2 <= 0 :", z)

# б) true
x = 2
y = - 2
q = (x >= 2) or (y**2 != 4)
print("При x = 2, y = -2, выражение (x >= 2) or (y**2 != 4):", q)

# в) false
x = 2
y = 2
w = (x >= 0) and (y**2 > 4)
print("При x = 2, y =2, (x >= 0) and (y**2 > 4):", w)

# г) true
x = 1
y = 2
e = (x * y != 4) and (y > x)
print("При x = 1, y = 2, (x * y != 4) and (y > x):", e)

# д) true
x = 2
y = 1
r = (x * y != 0) or (y < x)
print("При x = 2, y = 1, (x * y != 0) or (y < x)", r)

# е) true
x = 1
y = 2
t = (not (x * y < 1)) and (y > x)
print("При x = 1, y = 2, (not (x * y < 1)) and (y > x):", t)

# ж) true
x = 2
y = 1
u = (not (x * y < 0)) or (y > x)
print("При x = 2, y = 1, (not (x * y < 0)) or (y > x):", u)

# 3.17
# а) not A and not B or A
# 1) A = 1, B = 0: true
# 2) A = 1, B = 1: true
# 3) A = 0, B = 1: false
# 4) A = 0, B = 0: true

# b) B or not A and not B
# 1) A = 1, B = 0: false
# 2) A = 1, B = 1: true
# 3) A = 0, B = 1: true
# 4) A = 0, B = 0: true

# v) B and not (A and not B)
# 1) A = 1, B = 0: false
# 2) A = 1, B = 1: true
# 3) A = 0, B = 1: true
# 4) A = 0, B = 0: false

# 3.27
# а)
x = int(input("Введите значение x >> "))
y = int(input("Введите значение y >> "))
c = (x > 2) and (y > 3)
print("(x > 2) and (y > 3):", c)

# б)
x = int(input("Введите значение x >> "))
y = int(input("Введите значение y >> "))
b = (x > 1) or (y > -2)
print("(x > 1) or (y > -2):", b)

# в)
x = int(input("Введите значение x >> "))
y = int(input("Введите значение y >> "))
n = (x >= 0) and (y < 5)
print("(x >= 0) and (y < 5):", n)

# г)
x = int(input("Введите значение x >> "))
k = (x > 3) or (x < - 1)
print("(x > 3) or (x < - 1):", k)

# д)
x = int(input("Введите значение x >> "))
i = (x > 3) and (x < 10)
print("(x > 3) and (x < 10):", i)

# e)
x = int(input("Введите значение x >> "))
e = not (x > 2)
print("not (x > 2):", e)

# ж)
x = int(input("Введите значение x >> "))
t = not ((x > 0) and (x < 5))
print("not ((x > 0) and (x < 5)):", t)

# з)
x = int(input("Введите значение x >> "))
m = (x > 10) and (x <= 20)
print("(x > 10) and (x <= 20):", m)

# и)
x = int(input("Введите значение x >> "))
y = int(input("Введите значение y >> "))
j = ((y > 0) and (y <= 4)) and (x < 5)
print("((y > 0) and (y <= 4)) and (x < 5):", j)

# 3.28
# а) (A > 100) and (B > 100)
# б) (A % 2 == 0 and B % 2 != 0) or (A % 2 != 0 and B % 2 == 0)
# в) (A > 0) or (B > 0)
# g) (A % 3 == 0) and (B % 3 == 0) and (C % 3 == 0)
# д) (A < 50 and B >= 50 and C >= 50) or (B < 50 and C >= 50 and A >= 50) or (C < 50 and A >= 50 and B >= 50)
# е) (A < 0) or (B < 0) or (C < 0)

# 1.61
# а)
a = int(input("Введите число a для возведения в 4 степень >> "))
b = a * a
c = b * b
print("a**4 =", c)

# б)
a = int(input("Введите число a для возведения в 6 степень >> "))
b = a * a
c = b * b
d = c * b
print("a**6 =", d)

# ж)
a = int(input("Введите число a для возведения в 13 степень >> "))
b = a * a
c = b * b
d = c * b
e = d * d
f = e * a
print("a**13 =", f)

# з)
a = int(input("Введите число a для возведения в 15 степень >> "))
b = a * a
c = b * b
d = c * a
e = d * d
f = e * d
print("a**15 =", f)

# 2.36
print("Получение цифр суммы двух заданных чисел")
print("Что бы задать трехзначное число, введите:")
a3 = int(input("Число сотен >> "))
a2 = int(input("Число десятков >> "))
a1 = int(input("Число единиц >> "))
print("Что бы задать двузначное число, введите:")
b2 = int(input("Число десятков >> "))
b1 = int(input("Число единиц >> "))
first_number = int(str(a3) + str(a2) + str(a1))
second_number = int(str(b2) + str(b1))
new_number = first_number + second_number
first_x3 = new_number // 100
second_x2 = (new_number // 10) % 10
third_x1 = new_number % 10
print("Составляющии полученного числа")
print("Число сотен:", first_x3)
print("Число десятков:", second_x2)
print("Число единиц:", third_x1)
