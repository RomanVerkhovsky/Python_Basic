import os
# Работа с файлами
# 1
print("No_1")
print("The program is starting..")
while True:
    path = input("input path for reading file or 'stop' for exit >> ")
    if path == "stop":
        print("The program is stopped")
        break
    elif os.path.exists(path):
        file = open(path, "r")

        print(f"Text in file: '{file.read()}'")

        file.close()
        print("The program is stopped")
        break
    else:
        print("Error: file not found")

print("")

# 2
print("No_2")
print("Program is starting...")
while True:
    path = input("input path to file or 'stop' for a exit >> ")
    if path == "stop":
        print("The program is stopped")
        break
    elif os.path.exists(path):
        file = open(path, "r")
        text = file.read()
        file.close()
        print(f"In file: '{text}'")
        text = text[::-1]
        while True:
            path = input("input path for writing reverse text or 'stop' for a exit >> ")
            if path != 'stop':
                if not os.path.exists(path):
                    file = open(path, "w")

                    file.write(text)
                    print(f"Revers text in file {path}: {text}")

                    file.close()
                    break
                else:
                    print("The file already exists")
            else:
                print("The program is stopped")
                break
        print("The program is stopped")
        break

    else:
        print("Error: file not found")

print("")

# 3
print("No_3")
print("Program is starting...")
while True:
    path = input("Input path to file or 'stop' for exit >> ")
    if path != "stop":
        if os.path.exists(path):
            file = open(path, "r")
            text = file.read().split()
            file.close()
            count = 0
            for i in text:
                count += 1
            if count > 0:
                print(f"The text contain {count} word(s)")
                print("Program is stopped")
                break
            else:
                print("Error: The text don't contain word")
        else:
            print("Error: file not found")
    else:
        print("Program is stopped")
        break

print("")

# 4
print("No_4")
print("Program is starting...")
while True:
    path = input("Input path to file or 'stop' for exit >> ")
    if path != "stop":
        if os.path.exists(path):
            file = open(path, "r")
            text = file.read().split()
            file.close()
            count = 0
            for i in text:
                count += 1
            if count > 0:
                max_word = text[0]
                for i in text:
                    if len(i) > len(max_word):
                        max_word = i
                print(f"Max word in the text: {max_word}")
                print("Program is stopped")
                break
            else:
                print("Error: The text don't contain word")
        else:
            print("Error: file not found")
    else:
        print("Program is stopped")
        break

print("")

# 5
print("No_5")
print("Program is starting...")
while True:
    path = input("Input path to file or 'stop' for exit >> ")
    if path != "stop":
        if os.path.exists(path):
            file = open(path, "r")
            original_text = file.read()
            file.close()
            text = original_text.split()
            count = 0
            for i in text:
                count += 1

            if count > 0:
                while True:
                    find_text = input("Input the search text or 'stop' for exit >> ")
                    if find_text != "stop":
                        if original_text.find(find_text) != -1:
                            print("The text contain this text")
                        else:
                            print("The text don't contain this text")
                    print("Program шы stopped")
                    break
                break
            else:
                print("Error: The text don't contain word")
        else:
            print("Error: file not found")
    else:
        print("Program is stopped")
        break

print("")

# Работа со строками
# 6
print("No_6")
text = "функция"
text_1 = text[0:2] + "т"
text_2 = text[4:7]
print(f"{text} --> : {text_1}, {text_2}")

# 7
print("No_7")
text = "переменная"
text_1 = text[0:2] + text[7:9]
text_2 = text[2:7] + "ь"
print(f"{text} --> : {text_1}, {text_2}")

# 8
print("No_8")
text = "декларация"
text_1 = text[2] + text[4:7]
text_2 = text[0:2] + text[3]
print(f"{text} --> : {text_1}, {text_2}")

# 9
print("No_9")
text = "инкапсуляция"
text_1 = text[4] + text[6:9]
text_2 = text[0:4] + text[5]
print(f"{text} --> : {text_1}, {text_2}")

# 10
print("No_10")
text = "полиморфизм"
text_1 = text[2:6] + "н"
text_2 = text[0] + text[-5:-7:-1] + text[7:9]
print(f"{text} --> : {text_1}, {text_2}")

# 11
print("No_11")
text_1 = input("Input text >> ")
if len(text_1) != 0:
    text_2 = text_1[-1::-1]
    if text_1 == text_2:
        print("The text is palindrome")
    else:
        print("The text isn't palindrome")
else:
    print("Error: You didn't enter the text")

print("")

# Стандартная алгоритмика
# 12
print("No_12")
n = input("Input number >> ")
if n.isdigit():
    n = int(n)
    k = 0
    fact = 1
    for i in range(0, n, 1):
        k += 1
        fact *= k
    print(f"{n}! =", fact)
else:
    print("Error: You entered not a number")

# 13
print("No_13")
print("Input list of numbers. For exit input '0'")
lst = []
while True:
    numb = input("Input number >> ")
    if numb.isdigit():
        numb = int(numb)
        if numb != 0:
            lst.append(numb)
        else:
            break
    else:
        print("Error: You entered not a number")

print("The list of number: ", end="")
for i in lst:
    print(i, end=" ")
print("")

numb_max = lst[0]
numb_min = lst[0]
for i in lst:
    if i > numb_max:
        numb_max = i
    elif i < numb_min:
        numb_min = i

print("Max number in the list:", numb_max)
print("Min number in the list:", numb_min)

print("")

# Задачи на одномерные списки
# 14
print("No_14")
while True:
    n = input("Input number of elements in list No_1 >> ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Error: You entered not a number")

lst_1 = []
for i in range(n):
    elem = input("Input element >> ")
    lst_1.append(elem)

while True:
    n = input("Input number of elements in list No_1 >> ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Error: You entered not a number")

lst_2 = []
for i in range(n):
    elem = input("Input element >> ")
    lst_2.append(elem)

print("")

print("The list No_1: ", end="")
for i in lst_1:
    print(i, end=" ")
print("")

print("The list No_2: ", end="")
for i in lst_2:
    print(i, end=" ")
print("")

lst_3 = []
for i in lst_1:
    lst_3.append(i)

for i in lst_2:
    count = 0
    for j in range(len(lst_3)):
        if i != lst_3[j]:
            count += 1
    if count == len(lst_3):
        lst_3.append(i)

print("All non-repeating elements from the list No_1 and the list No_2")
print("The list No_3: ", end="")
for i in lst_3:
    print(i, end=" ")
print("")

# 11.53
print("11.53")
while True:
    n = input("Input number of elements >> ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Error: You entered not a number")

lst = []
for i in range(n):
    while True:
        elem = input("Input integer number >> ")
        if elem.isdigit():
            elem = int(elem)
            lst.append(elem)
            break
        else:
            print("Error: You entered not a integer number")

print("The list of integer numbers :", end="")
for i in lst:
    print(i, end=" ")
print("")

lst_a = []
for i in lst:
    lst_a.append(i)

for i in range(len(lst_a)):
    if lst_a[i] % 10 == 0:
        lst_a[i] = 0

print("a) The list: ", end="")
for i in lst_a:
    print(i, end=" ")
print("")

lst_b = []
for i in lst:
    lst_b.append(i)

for i in range(len(lst_b)):
    if lst_b[i] % 2 != 0:
        lst_b[i] *= 2
    else:
        lst_b[i] /= 2

print("b) The list: ", end="")
for i in lst_b:
    print(i, end=" ")
print("")

while True:
    m = input("Input number >> ")
    if m.isdigit():
        m = int(m)
        break
    else:
        print("Error: You entered not a number")

while True:
    n = input("Input number >> ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Error: You entered not a number")

lst_c = []
for i in lst:
    lst_c.append(i)

for i in range(len(lst_c)):
    if lst_c[i] % 2 != 0:
        lst_c[i] -= m
    if i % 2 != 0:
        lst_c[i] += n

print("v) The list: ", end="")
for i in lst_c:
    print(i, end=" ")
print("")

# 11.88
print("11.88")
moto = []
car = []
print("Make lists of prices (input 'stop' for exit)")
while True:
    choice = input("Input 'm' for add motorcycle, or 'c' for add car >> ")
    if choice == 'm' or choice == 'c':
        if choice == 'm':
            while True:
                elem = input("Input the coast of the motorcycle (integer only) or 'back' for new choice >> ")
                if elem != "back":
                    if elem.isdigit():
                        elem = int(elem)
                        moto.append(elem)
                        break
                    else:
                        print("Error: You entered not a number")
                else:
                    break
        elif choice == "c":
            while True:
                elem = input("Input the coast of the car (integer only) or 'back' for new choice >> ")
                if elem != "back":
                    if elem.isdigit():
                        elem = int(elem)
                        if elem > 5000:
                            car.append(elem)
                            break
                        else:
                            print("Error: There aren't cars in the assortment cheaper than $5000")
                    else:
                        print("Error: You entered not a number")
                else:
                    break
    elif choice == "stop":
        break
    else:
        print("Error: You entered invalid value")

count_moto = 0
sum_moto = 0
for i in moto:
    count_moto += 1
    sum_moto += i

count_car = 0
sum_car = 0
for i in car:
    count_car += 1
    sum_car += i

if count_moto != 0 and count_car != 0:
    print("The compilation of lists is over")
    print("The list of coast of motorcycles ($): ", end="")
    for i in moto:
        print(i, end=" ")
    print("")

    print("The list of coast of cars ($): ", end="")
    for i in car:
        print(i, end=" ")
    print("")

    ave_moto = sum_moto / count_moto
    ave_car = sum_car / count_car

    if ave_car >= ave_moto * 3:
        print("The average cost of cars exceeds the average cost of motorcycles by more than 3 times")
    else:
        print("The average cost of cars don't exceeds the average cost of motorcycles by more than 3 times")

else:
    print("The list is empty")

# 11.132
print("11.132")
n = input("Input number of elements >> ")
if n.isdigit():
    n = int(n)
    lst = []
    if n > 0:
        for i in range(n):
            while True:
                elem = input("Input integer number >> ")
                if elem[0] == "-":
                    if elem[1::].isdigit():
                        elem = - int(elem[1::])
                        lst.append(elem)
                        break
                    else:
                        print("Error: You entered not a number")
                else:
                    if elem.isdigit():
                        elem = int(elem)
                        lst.append(elem)
                        break
                    else:
                        print("Error: You entered not a number")

        print("lst: ", end="")
        for i in lst:
            print(i, end=" ")
        print("")

        if n > 1:
            max_elem = lst[0]
            for i in lst:
                if i > max_elem:
                    max_elem = i

            lst_buf = []
            for i in range(len(lst)):
                lst_buf.append(lst[i])

            lst_new = []
            count_eq = 0
            for i in range(len(lst_buf) - 1, -1, -1):
                if lst_buf[i] == max_elem:
                    count_eq += 1
                    for j in range(i, len(lst_buf)):
                        if j < len(lst_buf) - 1:
                            lst_buf[j] = lst_buf[j + 1]
                        else:
                            lst_buf[j] = 0

            for i in range(len(lst_buf) - count_eq):
                lst_new.append(lst_buf[i])

            if count_eq != len(lst_buf):
                second_max = lst_new[0]
                for i in lst_new:
                    if i > second_max:
                        second_max = i

                print(f"a)First max number: {max_elem}\n"
                      f"Second max number: {second_max}")
            else:
                print("a)All numbers are equal")

            min_elem = lst[0]
            for i in lst:
                if i < min_elem:
                    min_elem = i

            lst_buf2 = []
            for i in range(len(lst)):
                lst_buf2.append(lst[i])

            lst_new2 = []
            count_eq2 = 0
            for i in range(len(lst_buf2) - 1, -1, -1):
                if lst_buf2[i] == min_elem:
                    count_eq2 += 1
                    for j in range(i, len(lst_buf2)):
                        if j < len(lst_buf2) - 1:
                            lst_buf2[j] = lst_buf2[j] + 1
                        else:
                            lst_buf2[j] = 0

            for i in range(len(lst_buf2) - count_eq2):
                lst_new2.append(lst_buf2[i])

            if len(lst_buf2) != count_eq2:
                second_min = lst_new2[0]
                for i in lst_new2:
                    if i < second_min:
                        second_min = i

                print(f"b) First min number: {min_elem}\n"
                      f"Second min number: {second_min}")
            else:
                print("b)All numbers are equal")
        else:
            print("There is one number in the list")
    else:
        print("The list is empty")
else:
    print("Error: You entered not a number or negative number")

# 11.139
print("11.139")
n = 15
# n - number of floors
lst = []
for i in range(n):
    while True:
        elem = input(f"Input number of people on the floor No_{i + 1} >> ")
        if elem.isdigit():
            elem = int(elem)
            lst.append(elem)
            break
        else:
            print("Error: You entered not a number or negative number")

print("The list of people on floors: ", end="")
for i in lst:
    print(i, end=" ")
print("")

lst_floor = []
min_floor = lst[0]

for i in range(n):
    if lst[i] < min_floor:
        min_floor = lst[i]

for i in range(n):
    if lst[i] == min_floor:
        lst_floor.append(i)

second_min = 0
for i in range(n):
    if lst[i] != min_floor:
        second_min = lst[i]
        for j in range(n):
            if lst[j] < second_min and lst[j] != min_floor:
                second_min = lst[j]

for i in range(n):
    if lst[i] == second_min:
        lst_floor.append(i)

print(f"floor with a minimum number of people: {lst_floor[0] + 1}\n"
      f"Next floor with a minimum number of people: {lst_floor[1] + 1}\n")

# 11.185
print("11.185")
m = 20
# m - number of teams
lst = []
print("Make the list from bigger to smaller points. Start filling in with the worst team.")
for i in range(m):
    while True:
        elem = input(f"Input point of {m - i}th team >> ")
        if elem.isdigit():
            elem = int(elem)
            if i > 0:
                count = 0
                for j in range(len(lst)):
                    if elem == lst[j]:
                        count += 1
                if count == 0 and elem > lst[i - 1]:
                    lst.append(elem)
                    break
                else:
                    print("Error: Invalid value")
            else:
                lst.append(elem)
                break
        else:
            print("You are entered not a number >> ")

lst = lst[::-1]
print("Rating of points scored:")
for i in range(m):
    print(f"Team No_{i + 1}:", lst[i])

n = input("Input points to display the team's rating  >> ")
if n.isdigit():
    n = int(n)
    count_2 = 0
    for i in range(len(lst)):
        if n == lst[i]:
            count_2 += 1
    if count_2 != 0:
        print(f"{lst.index(n) + 1}th team scored {n} points")
    else:
        print("You have entered non-existent data")

print("")

# 11.216
print("11.216")
n = "20"
# n - numbers of district
while True:
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Error: You entered not a number")
        n = input("Input number of elements >> ")

lst_s = []
lst_harv = []

for i in range(n):
    elem = input(f"Input S district No_{i + 1} >> ")
    while True:
        if elem.isdigit():
            elem = int(elem)
            if elem != 0:
                lst_s.append(elem)
                break
            else:
                print("S shouldn't be equal to 0 ")
                elem = input(f"Input S district No_{i + 1} >> ")
        else:
            print("Error: You entered not a number")
            elem = input(f"Input S district No_{i + 1} >> ")

for i in range(n):
    elem = input(f"Input harvest in district No_{i + 1} >> ")
    while True:
        if elem.isdigit():
            elem = int(elem)
            lst_harv.append(elem)
            break
        else:
            print("Error: You entered not a number")
            elem = input(f"Input harvest in district No_{i + 1} >> ")
print("")

print("S of districts (km**2): ", end="")
for i in lst_s:
    print(i, end=" ")
print("")

print("Harvest in districts (c): ", end="")
for i in lst_harv:
    print(i, end=" ")
print("")
print("")
# 1) без доп. массива
print("ver 1: without an additional array")
s_area = 0
harv_area = 0
print("Average harvest for each district:")
for i in range(n):
    print(f"Average harvest for district No_{i + 1}: ", end="")
    ave_dis = lst_harv[i] / lst_s[i]
    s_area += lst_s[i]
    harv_area += lst_harv[i]
    print(round(ave_dis, 2), "c/ha")

if harv_area != 0:
    ave_area = s_area / harv_area
    print("Average harvest for area:", round(ave_area, 2), "c/ha")
else:
    print("There is no harvest in the region")
print("")

# 2) с доп массивом
print("ver 2: with an additional array")
s_area = 0
harv_area = 0
lst_ave = []
for i in range(n):
    ave = lst_harv[i] / lst_s[i]
    s_area += lst_s[i]
    harv_area += lst_harv[i]
    lst_ave.append(ave)

print("Average harvest for each district:")
for i in range(n):
    print(f"Average harvest for district No_{i + 1}: {round(lst_ave[i], 2)} c/ha")

if harv_area != 0:
    ave_area = s_area / harv_area
    print(f"Average harvest for area: {round(ave_area, 2)} c/ha")
else:
    print("There is no harvest in the region")
