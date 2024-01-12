import random
# 11.1
print("11.1")
lst = [37, 0, 50, 46, 34, 46, 0, 13]

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# 11.2
print("11.2")
n = 10
# n - numbers of elements
lst = []
for i in range(n):
    elem = int(input("Input elements >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# 11.5
print("11.5")
n = 20
# n - numbers of persons
lst = []
for i in range(n):
    weight = random.randint(50, 101)
    lst.append(weight)

print("Weight of 20 persons: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# 11.7
print("11.7")
lst = []
for i in range(20, 0, -1):
    lst.append(i)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# 11.13
print("11.13")
n = int(input("Input number of elements >> "))
lst = []
for i in range(n):
    elem = input(f"Input element No{i + 1} >> ")
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

index = int(input(f"Input index of element [0;{n - 1}] >> "))
print(f"Element with index {index}:", lst[index])

print("")
print("")

# 11.17
print("11.17")
# a)
n = int(input("input number of elements >> "))
lst = []
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

for i in range(n):
    lst[i] = lst[i] * 2

print("a) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

# b)
n = int(input("Input number of elements >> "))
a = int(input("Input number 'A' >> "))
lst = []
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

for i in range(n):
    lst[i] = lst[i] - a

print("b) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

# v)
n = int(input("Input numbers of elements >> "))
lst = []
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

first_elem = lst[0]

for i in range(n):
    lst[i] = lst[i] / first_elem

print("v) lst: ", end="")
for i in lst:
    print(round(i, 2), end=" ")

print("")
print("")

# 11.19
print("11.19")
n = int(input("Input numbers of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

summ = 0
for i in lst:
    summ += i

print("a) Summ all elements of lst: ", summ)

print("")

# b)
n = int(input("Input numbers of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

pro = 1
for i in lst:
    pro *= i

print("b) Product elements of lst: ", pro)

print("")

# v)
n = int(input("Input number of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

summ = 0
for i in lst:
    summ = summ + (i ** 2)

print("v) Summ (elem ** 2) of lst: ", summ)

print("")

# g)
n = int(input("Input number of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

summ = 0
count_index = 0
for i in lst:
    if count_index < 6:
        summ = summ + i
        count_index += 1

if count_index < 6:
    print(f"g) Numbers of elements ({count_index}) < 6, the sum of these numbers: ", summ)
else:
    print("g) Summ first six elements: ", summ)

print("")
print("")

# 11.25
print("11.25")
n = 30
# n - numbers of days june
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    rain_day = random.randint(left, right)
    lst.append(rain_day)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

decade_1 = 0
decade_2 = 0
decade_3 = 0

for i in range(0, 10, 1):
    decade_1 += lst[i]

for i in range(10, 20, 1):
    decade_2 += lst[i]

for i in range(20, 30, 1):
    decade_3 += lst[i]

print(f"First decade: {decade_1} mm; Second decade: {decade_2} mm; Third decade: {decade_3} mm")

print("")
print("")

# 11.36
print("11.36")
n = int(input("Input number of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []
for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

print("a) All non negative elements :", end="")
count_non_neg = 0
for i in lst:
    if i > 0:
        count_non_neg += 1
        print(i, end=" ")
if count_non_neg == 0:
    print("There are no positive numbers in the list")
print("")

print("b) All elements aren't exceed 100 :", end="")
count_less_100 = 0
for i in lst:
    if i <= 100:
        count_less_100 += 1
        print(i, end=" ")
if count_less_100 == 0:
    print("There aren't numbers < 100 in the list")

print("")
print("")

# 11.45
print("11.45")
n = int(input("Input number of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

index = 0

print("Elements with even index first, elements with odd index second: ", end="")
for i in lst:
    if index % 2 == 0:
        print(i, end=" ")
    index += 1

index = 0

for i in lst:
    if index % 2 != 0:
        print(i, end=" ")
    index += 1

print("")

# 11.45 (version 2)
print("11.45")
n = int(input("Input number of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

print("Elements with even index first, elements with odd index second: ", end="")
for i in range(n):
    if i % 2 == 0:
        print(lst[i], end=" ")

for i in range(n):
    if i % 2 != 0:
        print(lst[i], end=" ")

print("")
print("")

# 11.144
print("11.144")
n = int(input("Input number of elements >= 5 >> "))
if n >= 5:
    left = int(input("Input left range boundary >> "))
    right = int(input("Input right range boundary >> "))
    lst = []

    for i in range(n):
        elem = random.randint(left, right)
        lst.append(elem)

    print("lst: ", end="")
    for i in lst:
        print(i, end=" ")
    print("")

    buf = lst[1]
    lst[1] = lst[4]
    lst[4] = buf

    print("a) lst: ", end="")
    for i in lst:
        print(i, end=" ")
else:
    print("Error: Number of element < 5")

print("")
print("")

# 11.11
print(11.11)
n = 20
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
lst = []
if right - left >= 19:
    for i in range(20):
        count = 0
        elem = random.randint(left, right)
        for j in lst:
            if elem == j:
                count += 1
        while count > 0:
            count = 0
            elem = random.randint(left, right)
            for j in lst:
                if elem == j:
                    count += 1
        lst.append(elem)
    print("List of non-repeating elements (lst): ", end="")
    for i in lst:
        print(i, end=" ")
    print("")
else:
    print("Error: There aren't enough elements in the range")

print("")
