import math

# No_1
print('No_1')


class Man:
    def __init__(self, name: str, age: int, weight: float) -> None:
        self._name = name
        self._age = age
        self._weight = weight

    def __str__(self):
        return (f'Name: {self._name}\n'
                f'Age: {self._age}\n'
                f'Weight: {self._weight}')

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_weight(self) -> float:
        return self._weight

    def set_name(self, new_name: str):
        self._name = new_name

    def set_age(self, new_age: int):
        self._age = new_age

    def set_weight(self, new_weight: float):
        self._weight = new_weight


class Student(Man):
    def __init__(self, name: str, age: int, weight: float, study_year: int) -> None:
        super().__init__(name, age, weight)
        self._study_year = study_year

    def __str__(self):
        return (f'Name: {self._name}\n'
                f'Age: {self._age}\n'
                f'Weight: {self._weight}\n'
                f'Year of study: {self._study_year}')

    def get_study_year(self) -> int:
        return self._study_year

    def set_study_year(self, new_study_year: int):
        self._study_year = new_study_year

    def study_up(self):
        self._study_year += 1


student_1 = Student('Aleksey', 32, 70.5, 3)
print(student_1)
print('')
print(student_1.get_name())
print('')
student_1.study_up()
print(student_1)
print('')

# No_2
print('No_2')


class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def __str__(self):
        return f'{self._side_a}, {self._side_b}, {self._side_c}'

    def get_side_a(self) -> float:
        return self._side_a

    def get_side_b(self) -> float:
        return self._side_b

    def get_side_c(self) -> float:
        return self._side_c

    def set_side_a(self, new_a):
        self._side_a = new_a

    def set_side_b(self, new_b):
        self._side_b = new_b

    def set_side_c(self, new_c):
        self._side_c = new_c

    def corner_a(self) -> float:
        corner_a = math.acos((self._side_b**2 + self._side_c**2 - self._side_a**2) / (2 * self._side_b * self._side_c))
        return corner_a

    def corner_b(self) -> float:
        corner_b = math.acos((self._side_a**2 + self._side_c**2 - self._side_b**2) / (2 * self._side_a * self._side_c))
        return corner_b

    def corner_c(self) -> float:
        corner_c = math.acos((self._side_a**2 + self._side_b**2 - self._side_c**2) / (2 * self._side_a * self._side_b))
        return corner_c

    def perimeter(self) -> float:
        perimeter = self._side_a + self._side_b + self._side_c
        return perimeter


class RightAngle(Triangle):
    def __init__(self, side_a: float, side_b: float) -> None:
        super().__init__(side_a, side_b, side_c=math.sqrt(side_a**2 + side_b**2))
        self._area = 0.5 * self._side_a * self._side_b

    def __str__(self):
        return f'{self._side_a}, {self._side_b}, {self._side_c}'

    def set_side_c(self, new_c):
        pass

    def get_area(self) -> float:
        return self._area

    def area(self) -> float:
        return 0.5 * self._side_a * self._side_b


angle_1 = RightAngle(4, 5)
print('')
print(angle_1)
print(angle_1.get_area())
print(angle_1.corner_c())
angle_1.set_side_c(65)
print(angle_1)
print('')

# No_3
print('No_3')


class Date:
    def __init__(self, date: str) -> None:
        date_list = date.split('.')
        date_int = []
        for i in range(len(date_list)):
            if date_list[i].isdigit():
                number = int(date_list[i])
                date_int.append(number)
            else:
                raise ValueError('Incorrect date!')
        self.date = date
        self._year = date_int[0]
        self._month = date_int[1]
        self._day = date_int[2]

        self.months = {
            0: 0,
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if (self._month > 12 or self._month < 1) or (self._day < 1 or self._day > self.months[self._month]):
            raise ValueError('Incorrect date!')

    def __str__(self) -> str:
        return f'{self._year}.{self._month}.{self._day}'

    def get_year(self) -> int:
        return self._year

    def get_month(self) -> int:
        return self._month

    def get_day(self) -> int:
        return self._day

    def set_year(self, new_year: int):
        new_year = abs(new_year)
        self._year = new_year

    def set_month(self, new_month: int):
        new_month = abs(new_month)
        if new_month > 12 or new_month < 1:
            raise ValueError('No such month!')
        self._year = new_month

    def set_day(self, new_day: int):
        new_day = abs(new_day)
        if new_day > self.months[self._month] or new_day == 0:
            raise ValueError('Day does not correspond to the month!')
        self._day = new_day

    def get_number_day(self) -> int:
        number_day = self._day
        for i in range(self._month):
            number_day += self.months[i]
        return number_day

    def plus_days(self, days: int):
        days = abs(days)
        years = days // 365
        self._year += years
        days = days - (365 * years)

        while (days + self._day) > self.months[self._month]:
            days -= self.months[self._month]
            self._month += 1
            if self._month == 13:
                self._month = 1
                self._year += 1

        self._day += days

    def minus_days(self, days: int):
        days = abs(days)
        years = days // 365
        self._year -= years
        days = days - (365 * years)

        if days > self.get_number_day():
            days = days - self.get_number_day()
            self._year -= 1
            self._month = 12
            self._day = 31

        while days > self.months[self._month]:
            days -= self.months[self._month]
            self._month -= 1
            if self._month == 0:
                self._month = 12
                self._year -= 1
            self._day = self.months[self._month]

        self._day -= days

    def days_before(self, other) -> int:
        main_date = int(str(self._year) + str(self._month) + str(self._day))
        other_date = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))

        max_date = Date(self.date)
        min_date = Date(other.date)
        if other_date > main_date:
            buff = max_date
            max_date = min_date
            min_date = buff

        years = max_date._year - min_date._year
        min_date._year += years
        count_days_before = 0
        count_days_before += years * 365

        while min_date.__str__() != max_date.__str__():
            min_date.plus_days(1)
            count_days_before += 1

        return count_days_before

    def __eq__(self, other) -> bool:
        date_string_self = int(str(self._year) + str(self._month) + str(self._day))
        date_string_other = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))
        return date_string_self == date_string_other

    def __ne__(self, other) -> bool:
        date_string_self = int(str(self._year) + str(self._month) + str(self._day))
        date_string_other = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))
        return date_string_self != date_string_other

    def __gt__(self, other) -> bool:
        date_string_self = int(str(self._year) + str(self._month) + str(self._day))
        date_string_other = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))
        return date_string_self > date_string_other

    def __lt__(self, other) -> bool:
        date_string_self = int(str(self._year) + str(self._month) + str(self._day))
        date_string_other = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))
        return date_string_self < date_string_other

    def __ge__(self, other) -> bool:
        date_string_self = int(str(self._year) + str(self._month) + str(self._day))
        date_string_other = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))
        return date_string_self >= date_string_other

    def __le__(self, other) -> bool:
        date_string_self = int(str(self._year) + str(self._month) + str(self._day))
        date_string_other = int(str(other.get_year()) + str(other.get_month()) + str(other.get_day()))
        return date_string_self <= date_string_other


date_1 = Date('2023.12.31')
date_2 = Date('2022.1.1')
print('DATE 1:', date_1)
print('DATE 2:', date_2)
print('Number of the day of the year (data 1):', date_1.get_number_day())
print('Number of the day of the year (data 2):', date_2.get_number_day())
print('')

print('Minus 59 days')
date_2.minus_days(59)
print('DATE 2:', date_2, 'NEW')
print('')

print('Plus 59 days')
date_2.plus_days(59)
print('DATE 2:', date_2, 'NEW')
print('')

print('Plus 28 days')
date_2.plus_days(28)
print('DATE 2:', date_2, 'NEW')
print('')


print('DATE 1 days before DATE 2:', date_2.days_before(date_1))
print('')

print(date_1 >= date_2)


# No_4
print('No_4')


class Task:
    def __init__(self, question: str, answers: list, true_answer: int, point: int) -> None:
        self._question = question
        self._answers = answers
        self._true_answer = true_answer
        self._point = point

    def __str__(self) -> str:
        answers = ''
        for i in range(len(self._answers)):
            answers += f'{i+1}. {self._answers[i]}\n'
        answers = answers[:-1]
        return (f'Question: {self._question}\n'
                f'Answers:\n{answers}')

    def get_question(self) -> str:
        return self._question

    def get_answers(self) -> list:
        return self._answers

    def get_true_answer(self) -> int:
        return self._true_answer

    def get_point(self) -> int:
        return self._point

    def set_question(self, new_question):
        self._question = new_question

    def set_answers(self, lst: list):
        self._answers = lst

    def set_true_answer(self, new_true: 1 - 5):
        self._true_answer = new_true

    def set_point(self, new_point: int):
        self._point = new_point


class TestContent:
    def __init__(self, tasks: [Task]):
        self.tasks = tasks

    def __str__(self) -> str:
        tasks = ''
        for i in range(len(self.tasks)):
            tasks += f'Task No_{i+1}\n{self.tasks[i]}\n\n'
        return tasks[:-1]

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)

    def del_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_list_tasks(self) -> str:
        tasks = ''
        for i in range(len(self.tasks)):
            tasks += f'{i+1}. {self.tasks[i].question}\n'
        tasks = tasks[:-1]
        return tasks

    def get_task(self, number_task: int):
        if len(self.tasks) <= number_task:
            return self.tasks[number_task - 1]

    def __add__(self, other):
        lst = []
        for i in self.tasks:
            lst.append(i)

        for i in other.tasks:
            count_eq = 0
            for j in self.tasks:
                if i.get_question == j.get_question:
                    count_eq += 1
            if count_eq == 0:
                lst.append(i)

        new_test = TestContent(lst)
        return new_test

    def __sub__(self, other):
        lst = []
        for i in self.tasks:
            lst.append(i)

        list_eq = []
        for i in other.tasks:
            count_eq = 0
            for j in self.tasks:
                if i.get_question == j.get_question:
                    list_eq.append(i)
                    count_eq += 1
            if count_eq == 0:
                lst.append(i)

        for i in list_eq:
            if i in lst:
                lst.remove(i)

        new_test = TestContent(lst)
        return new_test


question_1 = 'What color is grass?'
answers_1 = ['Red', 'Yellow', 'Green', 'Black', 'White']
task_1 = Task(question_1, answers_1, 3, 5)
print('Task No_1')
print(task_1)
print('True answer:', task_1.get_true_answer())
print('')

question_2 = 'How many grams per kilogram?'
answers_2 = ['100', '1000', '1', '10', '50']
task_2 = Task(question_2, answers_2, 2, 3)
print('Task No_2')
print(task_2)
print('True answer:', task_2.get_true_answer())
print('')

question_3 = 'How many seconds in a minute'
answers_3 = [10, 100, 20, 120, 60]
task_3 = Task(question_3, answers_3, 5, 2)
print('Task No_3')
print(task_3)
print('True answer:', task_3.get_true_answer())
print('')

print('TEST_1')
test_1 = TestContent([task_1, task_2])
print(test_1)

print('TEST_2')
test_2 = TestContent([task_1, task_3])
print(test_2)

test_3 = test_1 + test_2
print('TEST_3')
print(test_3)

test_4 = test_1 - test_2
print('TEST_4')
print(test_4)
