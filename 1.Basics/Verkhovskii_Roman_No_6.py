# 6.5
number = int(input("Vvedite chislo dlya a1 i a2(oni ravni) >> "))
number_1 = number
count = 2
count_ravn = 2
while count < 18 and number == number_1:
    number = int(input(f"Vvedite chislo a{count + 1} >> "))
    count += 1
    if number == number_1:
        count_ravn += 1
print("Kol-vo ravnikh elementov:", count_ravn)

# 6.9
number = int(input("Vvedite chislo n >> "))
first_number = 1
step = 1
while first_number < number:
    step += 2
    first_number += step
print("V posledovatel'nosti 1, 4, 9, 16, 25...pervoe chislo, bol'shee", number, ":", first_number)

# 6.27 a), b), v)
number = int(input("Vvedite natural'noe chislo >> "))
max_number = number % 10
min_number = number % 10
while number != 0:
    last_number = number % 10
    number = number // 10
    if last_number > max_number:
        max_number = last_number
    else:
        if last_number < min_number:
            min_number = last_number
razniza = max_number - min_number
summa = max_number + min_number
print("Maksimal'naya cifra chisla:", max_number)
print("Minimal'naya cifra chisla:", min_number)
print("Maksimal'naya cifra previshaet minimal'nuu na", razniza)
print("Summa maksimal'noi i minimal'noi:", summa)

# 6.32
number = int(input("Vvedite natural'noe chislo >> "))
number_test = number
min_number = 9
count = 0
while number_test != 0:
    last_number = number_test % 10
    number_test = number_test // 10
    if last_number < min_number:
        min_number = last_number
while number != 0:
    last_number = number % 10
    number = number // 10
    if last_number == min_number:
        count += 1
print(f"Minimal'naya cifra v chisle: {min_number}, ona vstrechaetsya:", count, "raz(a)")

# 6.46
# a), b), v), g), d), e), j)
number = int(input("Vvedite natural'noe chislo >> "))
last_number_original = number % 10
summ = 0
pro = 1
count = 0
first_number = 0
while number != 0:
    last_number = number % 10
    number = number // 10
    count += 1
    summ += last_number
    pro *= last_number
    first_number = last_number
if summ > 10:
    print("Summa ego cifr bol'she 10")
else:
    print("Summa ego cifr ne bol'she 10")
if pro < 50:
    print("Proizvedenie ego cifr men'she 50")
else:
    print("Proizvedenie ego cifr bol'she 50")
if count % 2 == 0:
    print("Kol-vo ego cifr est' chetnoe chislo")
else:
    print("Kol-vo ego cifr est' nechetnoe chislo")
if count == 4:
    print("Eto chislo chetirekhznachnoe")
else:
    print("Eto chislo ne chetirekhznachnoe")
if first_number <= 6:
    print("Ego pervaya cifra ne previshaet 6")
else:
    print("Ego pervaya cifra previshaet 6")
if first_number == last_number_original:
    print("Cislo nachinaetsya i zakanchivaetsya odinakovoi cifroi")
else:
    print("Cislo nachinaetsya i zakanchivaetsya raznimi ciframi")
if first_number > last_number_original:
    print("Pervaya cifra chisla bol'she poslednei")
elif last_number_original > first_number:
    print("Poslednyaya cifra bol'she pervoi")
else:
    print("Pervaya i poslednyaya cifra ravni")

# 6.53
print("Yavlyaet'sya li posledovatel'nost' cifr v chisle pri prochtenii sprava nalevo uporyadochennoi v chisle:")
number_original = int(input("Vvedite natural'noe chislo >> "))
number = number_original
last_number = -1
past_number = -2
while number != 0 and last_number > past_number:
    past_number = last_number
    last_number = number % 10
    number = number // 10
if number == 0:
    print(f"Dlya chisla {number_original} otvet polozhitel'nii")
else:
    print(f"Dlya chisla {number_original} otvet otrizatel'nii")

# 6.80
number = int(input("Vvedite natural'noe chislo >> "))
count_zero = 0
count_nine = 0
while number != 0:
    last_number = number % 10
    number = number // 10
    if last_number == 9:
        count_nine += 1
    if last_number == 0:
        count_zero += 1
if count_zero > count_nine:
    print("Cifra 0 v chisle vstrechaetsya chashe")
elif count_nine > count_zero:
    print("Cifra 9 v chisle vstrechaetsya chashe")
elif count_nine == count_zero and (count_nine != 0 and count_zero != 0):
    print("Cifri 9 i 0 vstrechautsya odinakovoe kol-vo raz")
elif count_nine == 0 and count_zero == 0:
    print("Cifru 9 i 0 ne vstrechautsya v chisle")

# 7.96
number = int(input("Vvedite celoe chislo b1 >> "))
summ = 0
count = 1
while count < 10:
    count += 1
    if number > 20:
        summ += number
    number = int(input(f"Vvedite celoe chislo b{count} >> "))
if summ > 100:
    print("Summa chisel bol'she 20 previshaet 100")
elif summ > 0 and summ < 100:
    print("Summa chisel bol'she 20 ne previshaet 100")
elif summ == 0:
    print("V zadannikh chislakh net chisel bol'she 20")

# 5.65
kol_vo = int(input("Vvedite chislo zhitelei raiona No_1(v tisichakh) >> "))
plotn = int(input("Vvedite plotnost' naseleniya v raione No_1(t.chel/km**2) >> "))
if kol_vo >= 0 and plotn >= 0:
    count = 1
    S_obl = kol_vo / plotn
    while count < 12 and kol_vo >= 0 and plotn >= 0:
        kol_vo = int(input(f"Vvedite chislo zhitelei raiona No_{count + 1} (v tisichakh) >> "))
        plotn = int(input(f"Vvedite plotnost' naseleniya v raione No_{count + 1} (t.chel/km**2) >> "))
        S_obl += kol_vo / plotn
        count += 1
    if kol_vo >= 0 and plotn >= 0:
        print("Ploshad' oblasti =", S_obl, "km")
    else:
        print("Kol-vo chelovek i plotnost' ne mogut bit' otrizatel'nimi")
else:
    print("Kol-vo chelovek i plotnost' ne mogut bit' otrizatel'nimi")
