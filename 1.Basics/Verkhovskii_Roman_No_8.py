import random
# 11.18
print("11.18")
print("a)")
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

for i in range(n):
    lst[i] = lst[i] - 20

print("a) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

print("b)")
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

last_elem = lst[-1]

for i in range(n):
    lst[i] = lst[i] * last_elem

print("b) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

print("v)")
n = int(input("Input number of elements >> "))
left = int(input("Input left range boundary >> "))
right = int(input("Input right range boundary >> "))
b = int(input("Input number 'B' >> "))
lst = []

for i in range(n):
    elem = random.randint(left, right)
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

for i in range(n):
    lst[i] = lst[i] + b

print("v) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# 11.35
print("11.35")
n = 18
# n - number of ratings
lst = []

for i in range(n):
    elem = int(input("Input rating >> "))
    lst.append(elem)

print("list of ratings (lst): ", end="")
for i in lst:
    print(i, end=" ")

print("")

mandatory_prog = 0
short_prog = 0
arbitrary_prog = 0

for i in range(0, 6, 1):
    mandatory_prog += lst[i]

for i in range(6, 12, 1):
    short_prog += lst[i]

for i in range(12, 18, 1):
    arbitrary_prog += lst[i]

max = []
if mandatory_prog >= short_prog and mandatory_prog >= arbitrary_prog:
    max.append("mandatory")

if short_prog >= mandatory_prog and short_prog >= arbitrary_prog:
    max.append("short")

if arbitrary_prog >= mandatory_prog and arbitrary_prog >= short_prog:
    max.append("arbitrary")

print("The best program(s): ", end="")
for i in max:
    print(i, end="  ")

print("")
print("")

# 11.48
print("11.48")
print("a)")
n = int(input("Input numbers of elements >> "))
k1 = int(input("Input element 'k1' >> "))
k2 = int(input("Input element 'k2' >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

for i in range(n):
    if lst[i] > 0:
        lst[i] = lst[i] - k1
    elif lst[i] <= 0:
        lst[i] = lst[i] - k2

print("a) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# b)
print("b)")
n = int(input("Input number of elements >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

for i in range(n):
    if i % 2 != 0:
        lst[i] += 1
    elif i % 2 == 0:
        lst[i] -= 1

print("b) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# 11.87
print("11.87")
n = 22
# n - number of participants
lst = []

count_male = 0
count_female = 0
for i in range(n):
    gender = int(input("Сhoose the gender of the student: input >= 6 - for male, input < 6 - for female >> "))
    if gender >= 6:
        height = int(input("Input height of student >> ")) * -1
        lst.append(height)
        count_male += 1
    else:
        height = int(input("Input height of student >> "))
        lst.append(height)
        count_female += 1

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

sum_male = 0
sum_female = 0
for i in lst:
    if i < 0:
        sum_male += abs(i)
    else:
        sum_female += i

ave_male = sum_male / count_male
ave_female = sum_female / count_female

print("Average height of male: ", ave_male)
print("Average height of female: ", ave_female)

print("")

# 11.103
print("11.103")
n = int(input("Input number of elements >> "))
lst = []
count = 0
for i in range(n):
    elem = int(input("Input element != 0 >> "))
    if elem != 0:
        count += 1
        lst.append(elem)
    else:
        print("Error: element = 0")
        break

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

if count == n:
    last_elem = lst[0]
    count_change = 0
    for i in lst:
        if (last_elem < 0 and i > 0) or (last_elem > 0 and i < 0):
            count_change += 1
            last_elem = i

    print(f"The sign changes {count_change} times")
else:
    print("Error: The list isn't complete")

print("")

# 11.118
print("11.118")
n = 30
# n - number of people
lst = []

count = 0
for i in range(n):
    birthday = int(input("Input year of birthday >> "))
    if birthday >= 0:
        lst.append(birthday)
        count += 1
    else:
        print("Error: You entered a negative number")
        break

if count == n:
    print("List of dates of birth : ", end="")
    for i in lst:
        print(i, end=" ")

    print("")

    first = lst[0]
    old = []
    number = 0
    for i in lst:
        number += 1
        if i == first:
            old.append(number)
        elif i < first:
            first = i
            old = []
            old.append(number)

    print("The list of number of the oldest: ", end="")
    for i in old:
        print(i, end=" ")

    print("")

    print(f"a) Number of first oldest: {old[0]}")
    print(f"b)Number of last oldest: {old[-1]}")
    print("")

else:
    print("Error: The list isn't complete")
    print("")

# 11.124 a), b)
print("11.124 a), b)")
n = int(input("Input number of elements >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

min = lst[0]
max = lst[0]
lst_min = []
lst_max = []
number_elem = 0
for i in lst:
    number_elem += 1
    if i == min:
        lst_min.append(number_elem)
    if i == max:
        lst_max.append(number_elem)
    if i < min:
        lst_min = []
        lst_min.append(number_elem)
        min = i
    elif i > max:
        lst_max = []
        lst_max.append(number_elem)
        max = i

first = lst[0]
count = 0
for i in lst:
    if first == i:
        count += 1

print("a) Number of min elements: ", end="")
if count < n:
    for i in lst_min:
        print(i, end=" ")
else:
    print("All elements are equal")

print("")

print("b) Number of max elements: ", end="")
if count < n:
    for i in lst_max:
        print(i, end=" ")
else:
    print("All elements are equal")


print("")

# 11.153
print("11.153")
# a)
print("a)")
n = int(input("Input number of elements >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

index = 0
for i in lst:
    if i < 0:
        for j in range(index, n):
            if j < n - 1:
                lst[j] = lst[j + 1]
            else:
                lst[j] = 0
        break
    index += 1

lst_buf = lst
lst = []
for i in range(len(lst_buf) - 1):
    lst.append(lst_buf[i])

print("a) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# b)
print("b)")
n = int(input("Input number of elements >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
count_even = 0
for i in range(n):
    if lst[i] % 2 == 0:
        count_even += 1

if count_even > 0:
    index_last_even = 0
    for i in range(n):
        if lst[i] % 2 == 0:
            index_last_even = i

    for i in range(n):
        if i == index_last_even:
            for j in range(i, n):
                if j < n - 1:
                    lst[j] = lst[j + 1]
                else:
                    lst[j] = 0

    lst_buf = lst
    lst = []

    for i in range(len(lst_buf) - 1):
        lst.append(lst_buf[i])

    print("b) lst: ", end="")
    for i in lst:
        print(i, end=" ")

    print("")
    print("")

else:
    print("b)There aren't even numbers in the list 'lst'")
    print("")

# 11.159
print("11.159")
print("a)")
n = int(input("Input number of elements >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

lst.append(lst[n - 1])
for i in range(n):
    if i < n - 3:
        lst[(n - 1) - i] = lst[(n - 2) - i]
    elif i == n - 3:
        lst[(n - 1) - i] = 10

print("a) lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")
print("")

# b)
print("b)")
n = int(input("Input number of elements >> "))
m = int(input(f"Input the number of the element [0; {n}] after which you want to put the number 100 >> "))
lst = []

for i in range(n):
    elem = int(input("Input element >> "))
    lst.append(elem)

print("lst: ", end="")
for i in lst:
    print(i, end=" ")

print("")

if m < n and m >= 0:
    lst.append(lst[n - 1])
    for i in range(n):
        if i < n - m - 1:
            lst[(n - 1) - i] = lst[(n - 2) - i]
        elif i == n - m - 1:
            lst[(n - 1) - i] = 100

    print("b) lst: ", end="")
    for i in lst:
        print(i, end=" ")

    print("")
    print("")

else:
    lst.append(100)
    print("b) lst: ", end="")
    for i in lst:
        print(i, end=" ")

    print("")
    print("")
