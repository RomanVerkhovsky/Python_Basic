# 3.30
# a) (A % 2 == 0) or (A % 3 == 0)
# b) (A % 3 != 0) and (A % 10 == 0)

# 3.32
# a) x <= -2 and y >= 1
# b) y >= -2 and y <= 1.5
# j) (x >= 1 and x <= 3) and (y >= -2 and y <= -1)
# z) (x <= 2 and (y >= 0.5 and y <= 1.5)) or (x >= 2)

# 4.8
Km1 = float(input("input km >> "))
Ft = float(input("input ft >> "))
mkm = Km1 * 1000
mft = Ft / 0.305
if mkm > mft:
    print("first larger")
else:
    if mft > mkm:
        print("second larger")
    else:
        print("the numbers are equal")

# 4.23
x = int(input("Vvedite dvuznachnoe chislo >> "))
if (x >= 10) and (x <= 99):
    first_n = x // 10
    second_n = x % 10
    if first_n > second_n:
        print("First number is larger")
    else:
        if second_n > first_n:
            print("Second number is larger")
        else:
            print("First number = second number")
else:
    print("Error")

# 4.26
x = int(input("Vvedite dvuznachnoe chislo >> "))
if (x >= 10) and (x <= 99):
    first_n = x // 10
    second_n = x % 10
    summ = first_n + second_n
    if summ % 3 == 0:
        print("Summa ego chisel kratna 3")
    else:
        print("Summa ego chisel ne kratna 3")
        a = int(input("Vvedite chislo a >> "))
        if summ % a == 0:
            print("Summa ego chisel kratna", a)
        else:
            print("Summa ego chisel ne kratna", a)
else:
    print("Error")

# 4.30
x = int(input("Vvedite trekhznachnoe chislo >> "))
if (x >= 100) and (x <= 999):
    first_n = x // 100
    second_n = (x // 10) % 10
    third_n = 100 % 10
    summ = first_n + second_n + third_n
    if (summ >= 10) and (summ < 99):
        print("Summa ego chisel dvuznachnoe chislo")
    else:
        print("Summa ego chisel ne dvuznachnoe chislo")
    pro = first_n * second_n * third_n
    if (pro >= 100) and (pro <= 999):
        print("proizvedenie ego chisel trekhznachnoe chislo")
    else:
        print("proizvedenie ego chisel ne trekhoznachnoe chislo")
    a = int(input("Vvedite chislo a >> "))
    if pro > a:
        print("Proizvesenie ego chisel bolshe chisla", a)
    else:
        if pro < a:
            print("Proizvedenie ego chisel menshe chisla", a)
        else:
            print("proizvesenie ego chisel ravno chislu", a)
    if summ % 5 == 0:
        print("Summa ego chisel kratna 5")
    else:
        print("Summa ego chisel ne kratna 5")
    if summ % a == 0:
        print("Summa ego chisel kratna", a)
    else:
        print("Summa ego chisel ne kratna", a)
else:
    print("Error")

# 4.85
print("dlya vychisleniya funkzii y = -1 esli x < -1; y = x, esli x > -1; y = 1, esli x = -1:")
x = int(input("Vvedite znachenie dlya x >> "))
if x < -1:
    y = -1
    print("y =", y)
else:
    if x > -1:
        y = x
        print("y =", x)
    else:
        if x == -1:
            y = 1
            print("y =", y)

# 4.105
x = int(input("Vvedite nomer mesyaca >> "))
if (x >= 1) and (x <= 12):
    if x == 1:
        print("January")
    else:
        if x == 2:
            print("February")
        else:
            if x == 3:
                print("March")
            else:
                if x == 4:
                    print("April")
                else:
                    if x == 5:
                        print("May")
                    else:
                        if x == 6:
                            print("June")
                        else:
                            if x == 7:
                                print("July")
                            else:
                                if x == 8:
                                    print("August")
                                else:
                                    if x == 9:
                                        print("September")
                                    else:
                                        if x == 10:
                                            print("October")
                                        else:
                                            if x == 11:
                                                print("November")
                                            else:
                                                if x == 12:
                                                    print("December")
else:
    print("error")

# 4.4
x = int(input("Zadaite koordinatu x dlya tochki >> "))
y = int(input("Zadaite koordinatu y dlya tochki (krome 3) >> "))
if y == 3:
    print("Error")
if y > 3:
    print("Tochka nakhoditsya v oblasti 'I'")
else:
    if y < 3:
        print("Tochka nakhoditsya v oblasti 'II'")

# 4.38
# a)
# a)
x = int(input("Zadaite koordinatu x dlya tochki (krome 3) >> "))
y = int(input("Zadaite koordinatu y dlya tochki (krome 2) >> "))
if (x == 3) or (y == 2):
    print("Error")
else:
    if (x > 3) and (y > 2):
        print("Tochka popadaet v oblast' 'I'")
    else:
        print("Tochka ne popadaet v oblast' 'I'")

# b)
x = int(input("Zadaite koordinatu x dlya tochki (krome: - 2) >> "))
y = int(input("Zadaite koordinatu y dlya tochki (krome: - 4) >> "))
if (x == - 2) or (y == - 4):
    print("Error")
else:
    if (x < - 2) and (y < - 4):
        print("Tochka popadaet v oblast' 'I'")
    else:
        print("Tochka ne popadaet v oblast' 'I'")

# po zhelaniyu
# 4.5
# a)
x = float(input("Zadaite koordinatu x dlya tochki >> "))
if x <= 2:
    y = x
    print("y =", y)
else:
    if x > 2:
        y = 2
        print("y =", y)

# b)
x = float(input("Zadaite koordinatu x dlya tochki >> "))
if x <= 3:
    y = - x
    print("y =", y)
else:
    if x > 3:
        y = - 3
        print("y =", y)

# 4.91
# a)
x = float(input("Zadaite koordinatu x dlya tochki >> "))
if x <= - 1:
    y = 0
    print("y =", y)
else:
    if (x > - 1) and (x < 0):
        y = - (-1 - x)
        print("y =", y)
    else:
        if x >= 0:
            y = 1
            print("y =", y)

# b)
x = float(input("Zadaite koordinatu x dlya tochki >> "))
if x <= - 1:
    y = 1
    print("y =", y)
else:
    if (x > - 1) and (x < 1):
        y = - x
        print("y =", y)
    else:
        if x > 1:
            y = - 1
            print("y =", y)

# 4.117
a2 = int(input("Zadaite chislo desyatkov pervogo dvuznachnogo chisla ( ot 2 do 9 vkluchitel'no) >> "))
if (a2 > 9) or (a2 <= 2):
    print("Error")
else:
    a1 = int(input("Zadaite chislo edinic pervogo dvuznachnogo chisla >> "))
    if (a1 > 9) or (a1 < 0):
        print("Error")
    else:
        b2 = int(input(f"Zadaite chislo desyatkov vtorogo dvuznachnogo chisla (ot 1 (vkluch), no < {a2}): >> "))
        if (b2 >= a2) or (b2 <= 0):
            print("Error")
        else:
            if b2 == (a2 - 1):
                b1 = int(input(f"Zadaite chislo edinic vtorogo dvuznachnogo chisla ( <= {a1}) >> "))
                if b1 > a1:
                    print("Error")
                else:
                    first_number = int(str(a2) + str(a1))
                    second_number = int(str(b2) + str(b1))
                    new_number = first_number - second_number
                    first_c2 = new_number // 10
                    second_c1 = new_number % 10
                    print("chislo desyatkov poluchennogo chisla:", first_c2)
                    print("chislo edinic poluchennogo chisla:", second_c1)
            else:
                b1 = int(input("Zadaite chislo edinic vtorogo dvuznachnogo chisla >> "))
                if (b1 > 9) or (b1 < 0):
                    print("Error")
                else:
                    first_number = int(str(a2) + str(a1))
                    second_number = int(str(b2) + str(b1))
                    new_number = first_number - second_number
                    first_c2 = new_number // 10
                    second_c1 = new_number % 10
                    print("Chislo desyatkov poluchennogo chisla:", first_c2)
                    print("Chislo edinic poluchennogo chisla:", second_c1)
