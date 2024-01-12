# 9.9
print("9.9")
fam_1 = input("Input first family >> ")
fam_2 = input("Input second family >> ")

count_1 = 0
for i in fam_1:
    count_1 += 1

count_2 = 0
for i in fam_2:
    count_2 += 1

if count_1 > count_2:
    print("First family is longer")
elif count_2 > count_1:
    print("Second family is longer")
else:
    print("Families are the same length")

# 9.11
print("9.11")
s1 = input("Input country No1 >> ")
s2 = input("Input country No2 >> ")
buf = s1
s1 = s2
s2 = buf
print(f"Country No1: {s1}")
print(f"Country No2: {s2}")

# 9.20
print("9.20")
text = input("Input text (number of letter >= 3) >> ")
count = 0
for i in text:
    count += 1

if count >= 3:
    text_2 = text[2] + text[-1]
    print(f"third letter + last letter: {text_2}")

else:
    print("Error: Letters in the text < 3")

# 9.25
print("9.25")
text_1 = "информатика"
text_2 = text_1[2:7:]
text_3 = text_1[7:10:]

print("Original text: информатика")
print(f"First text: {text_2}")
print(f"Second text: {text_3}")

# 9.29
print("9.29")
text_1 = "клоун"
text_2 = text_1[-2::-3] + text_1[1:3:] + text_1[-1]
text_3 = text_1[0:4:3] + text_1[1:3:] + text_1[-1]
text_4 = text_1[0:3:2] + text_1[1:4:2] + text_1[-1]

print(f"Original text: {text_1}")
print(f"First text: {text_2}")
print(f"Second text: {text_3}")
print(f"Third text: {text_4}")

# 9.32
print("9.32")
text = "курсор"
text = text.replace("курс", "танц")
print(f"курсор --> {text}")

# 9.33
print("9.32")
text = "пробел"
text = text.replace("б", "д")
print(f"пробел --> {text}")

# 9.34
print("9.34")
text = "строка"
text = text.replace("к", "ф")
print(f"строка --> {text}")

# 9.35
print("9.35")
text = "муха"
text = text.replace("муха", "слон")
print(f"муха --> {text}")

# 9.33
print("9.32")
text = "тетрадь"
text = text.replace("тетрадь", "дневник")
print(f"тетрадь --> {text}")

# 9.54
print("9.54")
text = input("Input text >> ")

count = 0
for i in range(len(text)):
    if text[i] == "м" or text[i] == "н":
        print(text[i], end=" ")
        count += 1
if count == 0:
    print("Text doesn't contain letters 'м' and 'н'")

# 9.59
print("9.59")
text = input("Input text >> ")

count = 0
for i in range(len(text)):
    if text[i] == "о":
        count += 1

if count > 0:
    print(f"Text contain {count} letters 'о'")
else:
    print("Text doesn't contain letter 'о'")

# 9.76
print("9.76")
text = input("Input text contain 2 or more letter 'е' >> ")
count = 0
for i in range(len(text)):
    if text[i] == "е":
        count += 1

if count > 1:
    lst = []
    for i in range(len(text)):
        if text[i] == "е":
            lst.append(i)

    print(f"a) Number of first 'е': {lst[0] + 1}")
    print(f"b) Number of last 'е': {lst[-1] + 1}")

else:
    print("Error: The text doesn't match the condition")

# 9.90
print("9.90")
text = input("Input text >> ")

count = 0
for i in range(len(text)):
    if text[i] == "е":
        text = text.replace(text[i], "и")
        count += 1

if count > 0:
    print("Letter 'е' = 'и':", text)
else:
    print("The text doesn't contain letter 'е'")

# 9.139
text = input("Input text >> ")

count = 0
for i in range(len(text)):
    if text[i].isdigit():
        count += 1

if count > 0:
    print("All numbers in text: ", end="")
    for i in range(len(text)):
        if text[i].isdigit():
            print(text[i], end=" ")

else:
    print("Text doesn't contain numbers")

# 9.141
print("9.141")
text = input("Input text with numbers >> ")

count = 0
max = 0
for i in range(len(text)):
    if text[i].isdigit():
        count += 1
        max = int(text[i])

if count > 0:
    for i in range(len(text)):
        if text[i].isdigit():
            if int(text[i]) > max:
                max = int(text[i])

    print("Max number in text:", max)
else:
    print("Error: Text doesn't contain numbers")

# 9.154
print("9.154")
text = input("Input 1 word >> ")

text2 = text.split()
count = 0
for i in text2:
    count += 1

if count == 1:
    lst_origin = []
    for i in range(len(text)):
        count_buf = 0
        for j in lst_origin:
            if text[i] != j:
                count_buf += 1
        if count_buf == len(lst_origin):
            lst_origin.append(text[i])
    print(f"The word contain {len(lst_origin)} different letters")
else:
    print("Error: The text doesn't match the condition")

# 9.157
print("9.157")
text = input("Input 2 words >> ")

text2 = text.split()
if len(text2) == 2:
    first_word = text2[0]
    second_word = text2[1]

    first_origin = []
    for i in range(len(first_word)):
        count_buf = 0
        for j in first_origin:
            if first_word[i] != j:
                count_buf += 1
        if count_buf == len(first_origin):
            first_origin.append(first_word[i])
    print(f"Correspondence of original letters of word '{first_word}' to the letters of word '{second_word}': ", end="")
    for i in range(len(first_origin)):
        count = 0
        for j in second_word:
            if first_origin[i] == j:
                count += 1
        if count > 0:
            print("yes", end=" ")
        else:
            print("no", end=" ")
    print("")
else:
    print("Error: The text doesn't match the condition")
