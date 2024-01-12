import random
# 12.1
print("12.1 a), b)")
n = int(input("Input number of rows >> "))
m = int(input("Input number of columns >> "))

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        elem = int(input("Input element >> "))
        matrix[i].append(elem)

print("matrix: ")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print("")

print("a) matrix[0][-1]: ", end="")
for i in range(0, 1):
    for j in range(n - 1, n):
        print(matrix[i][j])

print("b) matrix[n -1][0]: ", end="")
for i in range(n - 1, n):
    for j in range(0, 1):
        print(matrix[i][j])

print("")

# 12.23
print("12.23")
print("a)")
n = 7
m = 7
# n - row, m - column
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        if j == i or j == n - i - 1:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

print("matrix: ")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="  ")
    print("")

print("")

print("b)")
n = 7
m = 7
# n - row, m - column
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        if j == i or j == n - i - 1 or i == 3 or j == 3:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

print("matrix: ")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="  ")
    print("")

print("")

# 12.25
# a)
print("12.25")
print("a)")
n = 12
m = 10
# n - numbers of rows; m - numbers of columns
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(1, m + 1):
        matrix[i].append(j + (i * 10))

print("matrix: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 10:
            print(matrix[i][j], end="   ")
        elif matrix[i][j] >= 10 and matrix[i][j] < 100:
            print(matrix[i][j], end="  ")
        elif matrix[i][j] >= 100:
            print(matrix[i][j], end=" ")
    print("")

print("")

# b)
print("b)")
n = 12
m = 10
# n - numbers of rows; m - numbers of columns
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(1, (12 * m), 12):
        matrix[i].append(i + j)

print("matrix: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 10:
            print(matrix[i][j], end="   ")
        elif matrix[i][j] >= 10 and matrix[i][j] < 100:
            print(matrix[i][j], end="  ")
        elif matrix[i][j] >= 100:
            print(matrix[i][j], end=" ")
    print("")
print("")

# 12.35 a), b)
print("12.35 a), b)")
n = int(input("Input number of rows (n >= 3) >> "))
m = int(input("Input number of columns >> "))
s = int(input(f"Choose column [1, {m}] >> "))
if n >= 3 and (s >= 0 and s <= m):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            elem = int(input("Input element >> "))
            matrix[i].append(elem)

    print("matrix: ")
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print(" ")

    sum = 0
    for i in matrix[2]:
        sum += i

    print("a) Sum of elements of third row: ", sum)

    sum = 0
    for i in range(n):
        for j in range(s - 1, s):
            sum += matrix[i][j]

    print(f"b) Sum of elements of column No{s}: ", sum)

    print("")

else:
    print("Error: You entered a number out of range")

print("")

# 12.39
print("12.39")
n = 25
m = 36
# n - number of row; m - number of seats
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        elem = random.randint(0, 1)
        matrix[i].append(elem)

print("Plan of free (0) and occupied (1) seats:")
print("Seats    ", end="")
for i in range(1, m + 1):
    if i <= 9:
        print(i, end="   ")
    else:
        print(i, end="  ")
print("")
print("")
for i in range(n):
    if i <= 8:
        print(f"Row {i + 1} : ", end=" ")
    elif i > 8:
        print(f"Row {i + 1}: ", end=" ")
    for j in range(m):
        print(matrix[i][j], end="   ")
    print("")

count = 0
for i in matrix[11]:
    if i == 1:
        count += 1

print("")
print("Number of occupied seats in row No_12: ", count)

print("")

# 12.54
print("12.54")
n = 8
m = 5
# n - number of group; m - number of course
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        num_stud = int(input(f"Input number of student Group No{i + 1} Course No{j + 1} >> "))
        matrix[i].append(num_stud)

print("")

print("Institute (number of students):")
print("Course", end="      ")
for i in range(1, m + 1):
    print(i, end="   ")
print("")
print("")

for i in range(n):
    print(f"Group No{i + 1}:", end="  ")
    for j in range(m):
        if matrix[i][j] < 10:
            print(matrix[i][j], end="   ")
        elif matrix[i][j] >= 10:
            print(matrix[i][j], end="  ")
    print("")

print("")

course_3 = 0
for i in range(n):
    for j in range(2, 3):
        course_3 += matrix[i][j]

ave_course_3 = course_3 / n

print("Average number of students in one group in the 3rd course:", round(ave_course_3))
print("")

# 12. 72 a), b), v), g)
print("12.72")
n = int(input("Input number of rows >> "))
m = int(input("Input number of columns >> "))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        elem = int(input("Input integer number >> "))
        matrix[i].append(elem)

print("matrix:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print("")

print("")

count = 0
count_50 = 0
count_non_even = 0
sum_non_even = 0
summ_even = 0
sum_elem_ind3 = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] % 2 == 0:
            summ_even += matrix[i][j]
            count += 1
        if matrix[i][j] < 50:
            count_50 += 1
        if matrix[i][j] % 2 != 0:
            count_non_even += 1
            sum_non_even += matrix[i][j]
        if (i + j) % 3 == 0 and (i + j) != 0:
            sum_elem_ind3 += matrix[i][j]

ave_non_even = sum_non_even / count_non_even

if count > 0:
    print("a) Sum of even elements:", summ_even)
else:
    print("a) There aren't even elements in the list")

print("b) Number of elements of matrix < 50:", count_50)
print("v) Average of non-even elements of matrix:", round(ave_non_even))
print("g) The sum of elements with an index sum multiple of three: ", sum_elem_ind3)
