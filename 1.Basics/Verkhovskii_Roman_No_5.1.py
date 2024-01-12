# 5.6
# a)
for i in range(21, 36, 1):
    x = i - 0.6
    print(i, x)

print("________")
# b)
for i in range(16, 25, 1):
    x = i - 0.5
    y = i + 0.8
    print(i, x, y)

# 5.10
print("Tabliza perevoda USD (ot 1 do 20) v RUB po tekush'emu kursu:")
x = float(input("Vvedite cenu odnogo dollara v rublyakh (po tekushemu kursu) >> "))
if x > 0:
    for i in range(1, 21, 1):
        k = i * x
        print("USD", i, "=", "RUB", round(k, 3))
else:
    print("Znachenie kursa ne mozhet bit' raven 0 ili bit' otricatel'nim")

# 5.15
print("Tabliza umnozheniya zadannogo chisla:")
n = float(input("Vvedite chislo [1;9] chtobi sostavit' tablicu umnozheniya s nim >> "))
if n >= 1 and n <= 9:
    for i in range(1, 11, 1):
        t = i * n
        print(n, "*", i, "=", t)
else:
    print("Error: Vvedite chislo iz zadannogo intervala")

# 5.30
# a)
summ = 0
for i in range(20, 41, 1):
    summ = summ + (i ** 3)
print("summa kubov vsekh celikh chisel:", summ)

# b)
a = int(input("Vvedite znachenie dlya a [0;50] >> "))
if a >= 0 and a <= 50:
    summ = 0
    for i in range(a, 51, 1):
        summ = summ + (i ** 2)
    print(f"Summa kvadratov vsekh celikh chisel ot {a} do 50:", summ)
else:
    print("Error: Vy vveli chislo ne iz zadannogo intervala")

# v)
n = int(input("Vvedite znachenie dlya n [1;100] >> "))
if n >= 1 and n <= 100:
    summ = 0
    for i in range(1, (n + 1), 1):
        summ = summ + (i ** 2)
    print(f"Summa kvadratov vsekh chisel ot 1 do {n}:", summ)
else:
    print("Error: Vy vveli chislo ne iz zadannogo intervala")

# g)
a = int(input("Vvedite znachenie dlya a >> "))
b = int(input("Vvedite znachenie dlya b (b >= a) >> "))
if b >= a:
    summ = 0
    for i in range(a, (b + 1), 1):
        summ = summ + (i ** 2)
    print(f"Summa kvadratov vsekh chisel ot {a} do {b}:", summ)
else:
    print("Error: Vy vveli chislo ne iz zadannogo intervala")

# 5.63
print("Raschet kol-va pshenizi sobrannoi po oblasti i sredn. urozhaainosti po obl.:")
m_obl = 0
s_obl = 0
for i in range(10):
    s = float(input(f"Vvedite S (v gektarakh) dlya raiona No{i + 1} >> "))
    u = float(input(f"Vvedite sredn. urozhainost (centner/ga) dlya raiona No{i + 1} >> "))
    if s >= 0 and u >= 0:
        m_raion = s * u
        m_obl = m_raion + m_obl
        s_obl = s_obl + s
    else:
        print("Error: Vy vveli ne korrektnoe chislo")
u_obl = m_obl / s_obl
print("Vsego pshenici sobrano po oblasti:", round(m_obl, 2), "centner")
print("Sredn. urozhainost' po oblasti:", round(u_obl, 2), "centner")

# 7.2
a = int(input("Vvedite celoe chislo a >> "))
b = int(input("Vvedite celoe chislo b >> "))
c = int(input("Vvedite celoe chislo c >> "))
if a <= b:
    print(f"Celye chisla ot {a} do {b} kratnye {c}:")
    for i in range(a, b + 1, 1):
        if i % c == 0:
            print(i, end=" ")
else:
    if a >= b:
        print(f"Celye chisla ot {a} do {b} kratnye {c}:")
        for i in range(a, b - 1, -1):
            if i % c == 0:
                print(i, end=" ")

# 7.12
summ = 0
for i in range(30, 101, 1):
    if i % 3 == 0 and (i % 10 == 2 or i % 10 == 4 or i % 10 == 8):
        summ = i + summ
print("Summa celikh polozhitel'nikh chisel [30;100] kratnikh 3 i okanchivaush'ikhsya na 2, 4, 8:", summ)

# 7.86
summ = 0
for i in range(10):
    a = float(input(f"Vvedite cjislo dlya 'a{i+1}' >> "))
    summ = summ + a
if summ > 100.78:
    print("Summa chisel a1, a2,...a10 previshaet 100.78")
else:
    print(f"Summa chisel a1, a2,...a10 = {summ} ne previshaet 100.78")