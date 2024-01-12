# 1 print list
def printlst(lst: list):
    for i in lst:
        if type(lst) == list:
            print("You entered matrix")
            break
        else:
            print(i, end=" ")

# 2 print matrix
def printmatr(matrix):
    try:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print("")
    except TypeError:
        print("Error: You entered not a matrix")

# 3
def printdown(matrix):
    try:
        for i in range(len(matrix)):
            for j in range(0, i + 1):
                print(matrix[i][j], end=" ")
            print("")
    except TypeError:
        return print("Error: You entered not a matrix")

# 4
def sumeven(lst: list):
    count = 0
    summ = 0
    for i in lst:
        if type(i) == list:
            print("Error: You entered matrix")
            break
        else:
            if i % 2 == 0:
                count += 1
                summ += i

    if count > 0:
        return summ
    else:
        return print("The list don't contain even numbers")

# 5
def searchtarget(lst:list, a):
    index = -1
    count = 0
    for i in lst:
        index += 1
        if type(i) == list:
            print("Error: You entered matrix")
            break
        if i == a:
            count += 1
            break
    if count == 0:
        return -1
    else:
        return index

# 6
def nonevensq(lst: list):
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            lst[i] = lst[i] ** 2
    return lst
def evenmin3(lst: list):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] - 3
    return lst

def sqmin3(lst: list):
    nonevensq(lst)
    evenmin3(lst)
    return lst

# 7
def countodd(lst: list):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            count += 1
    return count




