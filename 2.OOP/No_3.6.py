# No_1
print('No_1')


class Student:
    def __init__(self, first_name: str, second_name: str, age: int, ave_point: float) -> None:
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age
        self.__ave_point = ave_point

    def __str__(self) -> str:
        return (f'First name: {self.__first_name}, Second name: {self.__second_name}, Age: {self.__age},'
                f'Average point: {self.__ave_point}')

    def get_first_name(self) -> str:
        return self.__first_name

    def get_second_name(self) -> str:
        return self.__second_name

    def get_age(self) -> int:
        return self.__age

    def get_ave_point(self) -> float:
        return self.__ave_point

    def set_first_name(self, new_name: str):
        self.__first_name = new_name

    def set_second_name(self, new_name: str):
        self.__second_name = new_name

    def set_age(self, new_age: int):
        self.__age = new_age

    def set_ave_point(self, new_ave_point: float):
        self.__ave_point = new_ave_point

    def __eq__(self, other):
        return self.__ave_point == other.__ave_point

    def __ne__(self, other):
        return self.__ave_point != other.__ave_point

    def __lt__(self, other):
        return self.__ave_point < other.__ave_point

    def __gt__(self, other):
        return self.__ave_point > other.__ave_point

    def __le__(self, other):
        return self.__ave_point <= other.__ave_point

    def __ge__(self, other):
        return self.__ave_point >= other.__ave_point


student_1 = Student('James', 'Cameron', 22, 5)
student_2 = Student('Brad', 'Pitt', 20, 8)
print(student_1 == student_2)
print(student_1 > student_2)

# No_2
print('No_2')


class Car:
    def __init__(self, brand: str, model: str, year: int, coast: float, status: str = 'ожидается') -> None:
        self._brand = brand
        self._model = model
        self._year = year
        self._coast = coast
        if status != 'в наличии' or status != 'продано' or status != 'ожидается':
            raise ValueError('Incorrect data')
        self._status = status

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def get_coast(self) -> float:
        return self._coast

    def get_status(self) -> str:
        return self._status

    def set_brand(self, brand: str) -> None:
        self._brand = brand

    def set_model(self, model: str) -> None:
        self._model = model

    def set_year(self, year: int) -> None:
        self._year = year

    def set_coast(self, coast: float) -> None:
        self._coast = coast

    def set_status(self, status: str) -> None:
        if status != 'в наличии' or status != 'продано' or status != 'ожидается':
            raise ValueError('Incorrect data')
        self._status = status


class Salesperson:
    def __init__(self, name: str, experience: int, cars_sold: list = None) -> None:
        self._name = name
        self._experience = experience
        self._cars_sold = cars_sold

    def get_name(self) -> str:
        return  self._name

    def get_experience(self) -> int:
        return self._experience

    def get_cars_sold(self) -> list:
        return self._cars_sold

    def set_name(self, name: str) -> None:
        self._name = name

    def set_experience(self, experience: str) -> None:
        self._experience = experience

    def sold_car(self, car: object) -> None:
        self._cars_sold.append(car)

    def cancel_sold_car(self, car: object) -> None:
        if car in self._cars_sold:
            self._cars_sold.remove(car)


class Customer:
    def __init__(self, name: str, phone: int, mail: str, cars_buy: list = None) -> None:
        self._name = name
        self._phone = phone
        self._mail = mail
        self._cars_buy = cars_buy

    def get_name(self) -> str:
        return self._name

    def get_phone(self) -> int:
        return self._phone

    def get_mail(self) -> str:
        return self._mail

    def get_cars_buy(self) -> list:
        return self._cars_buy

    def set_name(self, name: str) -> None:
        self._name = name

    def set_phone(self, phone: int) -> None:
        self._phone = phone

    def set_mail(self, mail: str) -> None:
        self._mail = mail

    def buy_car(self, car: object) -> None:
        self._cars_buy.append(car)

    def cancel_buy_car(self, car: object) -> None:
        if car in self._cars_buy:
            self._cars_buy.remove(car)


class Dealership:
    def __init__(self, cars: list = None, salespersons: list = None, customers: list = None) -> None:
        self._cars = cars
        self._salespersons = salespersons
        self._customer = customers

    def get_cars(self) -> list:
        return self._cars

    def get_salespersons(self) -> list:
        return self._salespersons

    def get_customer(self) -> list:
        return self._customer

    def add_car(self, car: object) -> None:
        self._cars.append(car)

    def sold_car(self, car: object) -> None:
        if car in self._cars:
            self._cars.remove(car)

    def del_car(self, car: object) -> None:
        if car in self._cars:
            self._cars.remove(car)


