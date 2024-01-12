# 1
def near_target(array: list, target: int) -> int:
    """Search for a close number in the array to the target"""
    near_number = array[0]
    for i in range(1, len(array)):
        if abs(target - array[i]) < abs(target - near_number):
            near_number = array[i]
    return near_number


# 2
def num_original_words(text: str) -> int:
    """Definition of original words in the text"""
    if len(text) != 0:
        lst_word = text.split(' ')
        list_origin_words = []
        for i in range(len(lst_word)):
            if lst_word[i].lower() not in list_origin_words:
                list_origin_words.append(lst_word[i].lower())
        return len(list_origin_words)
    else:
        return 0


# 3

# Проблема: Разработать алгоритм, который анализирует текст - список клиентов и дат их рождения и подсчитывает
#           количество клиентов с четным годом рождения.
# Выходные данные: одно целое число, представляющее количество клиентов имееющих возможность воспользоваться акцией.
#                  Формат - одно целое число
# Входные данные: список строк, строка содержит ФИО и дату рождения клиента.
#                 Формат: список строк текста
#
# Тестовые примеры
# Типовой тест
# Входные данные: Петров П.П. 2.2.1992\nИванов И.И. 3.3.1991\nГрачев Г.Г 1989
# Выходные данные: 1
#
# Текст с некорректными входными данными:
# Входные данные: ''
# Выходные данные: 0
#
# Граничный тест:
# Входные данные:
# Выходные данные:

def count_customer(path: str) -> int:
    """Input file in format .txt with customers and date and return number customers with even date"""
    file = open(path, 'r')
    text = file.read()
    text = text.split('\n')
    years = []
    for i in text:
        year = i[-4:]
        if year.isdigit():
            year = int(year)
            years.append(year)
    count_even = 0
    for i in years:
        if i % 2 == 0:
            count_even += 1
    return count_even
