import math
# 4.23
x = int(input("Vvedite dvuznachnoe chislo >> "))
if (x > -100 and x < -9) or (x > 9 and x < 100):
    first_n = abs(x) // 10
    second_n = abs(x) % 10
    if first_n > second_n:
        print("Pervaya cifra bol'she vtoroi")
    else:
        if second_n > first_n:
            print("Vtoraya cifra bol'she pervoi")
        else:
            print("Cifry ravny")
else:
    print("Error: Vy vveli ne dvuznachnoe chislo")

# 4.24
print("Raven li x**2,uchetverennoi summe kubov ego cifr")
x = int(input("Vvedite dvuznachnoe chislo >> "))
if (x > -100 and x < -9) or (x > 9 and x < 100):
    number_kv = x**2
    first_n = abs(x) // 10
    second_n = abs(x) % 10
    Summ_kub = 4 * (first_n ** 3 + second_n ** 3)
    if number_kv == Summ_kub:
        print("Dlya chisla", x, "otvet polozhitel'nyi")
    else:
        print("Dlya chisla", x, "otvet otricatel'nyi")
else:
    print("Error: Vy vveli ne dvukhznachnoe chislo")

# 4.31
x = int(input("Vvedite trekhznachnoe chislo >> "))
if (x > -1000 and x < -99) or (x > 99 and x < 1000):
    first_n = abs(x) // 100
    second_n = (abs(x) // 10) % 10
    third_n = abs(x) % 10
    if first_n == second_n and second_n == third_n and first_n == third_n:
        print("Vse ego cifry odinakovye")
    else:
        print("Vse cifry ne odinakovye")

    if (first_n == second_n) or (second_n == third_n) or (first_n == third_n):
        print("Sredi cifr est' odinakovye")
    else:
        print("Sredi cifr net odinakovykh")
else:
    print("Error, vy vveli ne trekhznachnoe chislo")

# 4.37
print("Prinadlezhit li chislo intervalu (-5,3)")
x = float(input("Vvedite chislo >> "))
if x > -5 and x < 3:
    print("Chislo prinadlezhit intervalu")
else:
    print("Chislo ne prinadlezhit intervalu")

# 4.41
print("Vychislit' f(x) esli f=sinx pri 0,2<=x<=0,9; ili '1' v protivnom sluchae")
x = float(input("Vvedite chislo x >> "))
if x <= 0.9 and x >= 0.2:
    f = math.sin(x)
else:
    f = 1
    print("f = ", f)

# 4.57
x = int(input("Vvedite trekhznachnoe chislo >> "))
if (x > -1000 and x < -99) or (x > 99 and x < 1000):
    first_n = abs(x // 100)
    second_n = abs((x // 10) % 10)
    third_n = abs(x % 10)
    n = int(input("Vvedite cifru n, chtoby opredelit' vkhodit li ona v chislo >> "))
    if n > -10 or n < 10:
        n = abs(n)
        if (first_n == n) or (second_n == n) or (third_n == n):
            print("Cifra", n, "vkhodit v chislo", x)
        else:
            print("Cifra", n, "ne vkhodit v chislo", x)
    else:
        print("Error: Vy vveli ne cifru")
else:
    print("Error: Vy vveli ne trekhznachnoe chislo")

# 4.71
# a)
print("Chtoby opredelit' naibol'shee i men'shee chislo vvedite 2 lubykh razlichnykh chisla")
first_n = float(input("Vvedite pervoe chislo >> "))
second_n = float(input("Vvedite vtoroe, otlichnoe ot pervogo chisla chislo >> "))
if first_n != second_n:
    if first_n > second_n:
        print("Pervoe > vtorogo")

    if second_n > first_n:
        print("Vtoroe > pervogo")
else:
    print("Error: Vvedite chislo otlichnoe ot pervogo")

# b)
print("Chtoby opredelit' naibol'shee i men'shee chislo vvedite 2 lubykh razlichnykh chisla")
first_n = float(input("Vvedite pervoe chislo >> "))
second_n = float(input("Vvedite vtoroe, otlichnoe ot pervogo chisla chislo >> "))
if first_n != second_n:
    if first_n < second_n:
        time = first_n
        first_n = second_n
        second_n = time
    print("Bol'shee:", first_n)
    print("Men'shee:", second_n)
else:
    print("Error: Vvedite chislo otlichnoe ot pervogo")

# 4.88
print("Chtoby vychislit': f = 2, pri y>2; 0 pri 0<y<=2; -3y v ostl. sluchayakh")
y = float(input("Vvedite znachenie y >> "))
if y > 2:
    f = 2
else:
    if y > 0 and y <= 2:
        f = 0
    else:
        f = -3 * y
print("f =", f)

# 4.95
# pri uslovii chto boxer tochno podkhodit pod 1 iz zadannykh kategorii
x = float(input("Vvedite ves boksera v predelakh ot 60 (vkl 60) lo 69 (vkl 69) >> "))
if x >= 60 and x <= 69:
    if x == 60:
        print("Bokser legkogo vesa")
    elif x > 60 and x <= 64:
        print("Bokser 1go polusrednego vesa")
    elif x > 64 and x <= 69:
        print("Bokser polusrednego vesa")
else:
    print("Error: Vy veli ves vykhodyashii za ramki zadannykh vesovykh kategorii")

# 4.108
# 1 - piki 2 - trefy 3 - bubny 4 - chervy
m_1 = "Piki"
m_2 = "Trefy"
m_3 = "Bubny"
m_4 = "Chervy"
x = int(input("Vyberite chislo ot 1 do 4 (vkluchitel'no) chtoby uznat' mast' >> "))
if x > 0 and x < 5:
    if x == 1:
        print(m_1)
    elif x == 2:
        print(m_2)
    elif x == 3:
        print(m_3)
    elif x == 4:
        print(m_4)
else:
    print("Vy vybrali chislo ne iz zadannogo intervala")
