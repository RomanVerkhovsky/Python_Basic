import math
# 1.22
# а)
x = float(input("Для вычисления функции: y=7(x*x)-3x+6, введите значение x >> "))
y = (7 * math.pow(x, 2)) - (3 * x) + 6
print("При x =", x, ",y =", y)

# б)
a = float(input("Для вычисления функции: x=12(a*a)+7a-16, введите значение a >> "))
x = (12 * math.pow(a, 2)) + (7 * a) - 16
print("При a =", a, ",x =", x)

# 1.23
a = float(input("Для вычисления функции: y=(a*a+10)/sqrt(a*a+1), введите значение a >> "))
y = (math.pow(a, 2) + 10) / math.sqrt(math.pow(a, 2) + 1)
print("При a =", a, ",y =", y)

# 1.44
print("Задайте стороны прямоугольника, что бы найти его P и диагональ")
a = int(input("Введите значение стороны a >> "))
b = int(input("Введите значение стороны b >> "))
p = 2 * (a + b)
d = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print("P =", p, "D =", d)

# 1.60
# a)
a = int(input("Введите число a >> "))
b = int(input("Введите число b >> "))
c = int(input("Введите число c >> "))
d = a
a = b
b = c
c = d
print("a =", a, "b =", b, "c =", c)

# б)
a = int(input("Введите число a >> "))
b = int(input("Введите число b >> "))
c = int(input("Введите число c >> "))
d = a
a = c
c = b
b = d
print("a =", a, "b =", b, "c =", c)

# 2.1
x = int(input("Для отображения числа полных метров,введите расстояние в сантиметрах >> "))
y = math.floor((x / 100))
print("S =", y, "м")

# 2.3
x = int(input("Для отображения числа полных тонн, введите массу в кг >> "))
y = math.floor((x / 1000))
print("m =", y, "тонн")

# 2.6
n = int(input("Укажите сколько прошло секунд с начала суток >> "))
# h - часов, m - минут осталось, s - секунд осталось,
h = n / 3600
m = (h % 1) * 60
s = (m % 1) * 60
x = math.floor(h)
y = math.floor(m)
z = math.floor(s)
print("Полных часов прошло с начала суток :", x)
print("Полных минут прошло с начала очередного часа :", y)
print("Полных секунд прошло с начала очередной минуты :", z)

# 2.10
a = int(input("Введите двузначное число >> "))
# first - число десятков(и первая цифра числа),d - сумма его цифр, e - произвединие его цифр
# second - число единиц(и вторая цифра числа)
first = a // 10
second = a % 10
d = first + second
e = first * second
print("Число десятков =", first)
print("Число единиц =", second)
print("Сумма его цифр =", d)
print("Произвединие его цифр =", e)

# 2.19
a = int(input("Введите четырехзначное число >> "))
first = a // 1000
second = (a % 1000) // 100
third = (a % 100) // 10
fourth = (a % 10)
b = first + second + third + fourth
c = first * second * third * fourth
print("Сумма его цифр =", b)
print("Произведение его цифр =", c)
