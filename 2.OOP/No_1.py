import math


# No_1
class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    def __str__(self) -> str:
        return (f'Width - {self.__width}\n'
                f'Height - {self.__height}')

    def get_square(self) -> int or float:
        square = self.__width * self.__height
        return square

    def get_perimeter(self) -> int or float:
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def get_width(self) -> int or float:
        return self.__width

    def get_height(self) -> int or float:
        return self.__height

    def set_width(self, value: int):
        if value > 0:
            self.__width = value

    def set_height(self, value: int):
        if value > 0:
            self.__height = value


r1 = Rectangle(10, 20)
r1.set_width(20)
print(r1.get_width())
print(r1.get_square())
print(r1)


# No_2
class BankAccount:
    def __init__(self, balance: int, id: int) -> None:
        self.__balance = balance
        self.__id = id

    def __str__(self) -> str:
        return (f'ID: {self.__id}\n'
                f'Balance: {self.__balance}')

    def get_balance_return(self) -> int or float:
        return self.__balance

    def get_id(self) -> int:
        return self.__id

    def set_add_money(self, money):
        self.__balance += money

    def set_withdrawal_money(self, money):
        if self.__balance - money >= 0:
            self.__balance -= money


account_1 = BankAccount(1000, 645424)
account_2 = BankAccount(3456, 745353)

print(account_1)
account_1.set_add_money(5674)
print(f'Balance: {account_1.get_balance_return()}')


# No_3
class Computer:
    def __init__(self, brand: str, model: str, cpu: str, ram: int, storage: int):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.RAM = ram
        self.storage = storage
        self.is_activ = True
        self.soft = []

    def info(self):
        print(f'Computer:\n'
              f'brand: {self.brand}\n'
              f'model: {self.model}\n'
              f'cpu: {self.cpu}\n'
              f'RAM: {self.RAM}\n'
              f'storage: {self.storage}\n'
              f'activ: {self.is_activ}\n')

    def install_soft(self, name: str):
        self.soft.append(name)

    def view_soft(self):
        print('Soft:')
        for i in self.soft:
            print(i)

    def turn_on(self):
        self.is_activ = True

    def turn_off(self):
        self.is_activ = False


computer_1 = Computer('ASUS', 'B123', 'i7 13700h', 16, 1024)
computer_1.info()


# No_4
class MusicAlbum:
    def __init__(self, artist, album, genre):
        self.artist = artist
        self.album = album
        self.genre = genre
        self.list_track = []

    def add_track(self, name_track):
        if name_track not in self.list_track:
            self.list_track.append(name_track)

    def del_track(self, name_track):
        if name_track in self.list_track:
            self.list_track.remove(name_track)

    def info(self):
        print(f'Album: {self.album}\n'
              f'Artist: {self.artist}\n'
              f'Genre: {self.genre}\n'
              f'List of songs:')
        for i in range(len(self.list_track)):
            print(f'      {i + 1}. {self.list_track[i]}')


Album_1 = MusicAlbum('Linkin Park', 'Meteora', 'Alternative')
Album_1.add_track('Numb')
Album_1.add_track('Faint')
Album_1.add_track('Numb')
Album_1.del_track('qwe')
Album_1.info()


# No_5
class Vector2D:
    def __init__(self, x: float or int, y: float or int) -> None:
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f'({self.__x}, {self.__y})'

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def set_x(self, new_x: float or int):
        self.__x = new_x

    def set_y(self, new_y: float or int):
        self.__y = new_y

    def __add__(self, other):
        x = self.__x + other.get_x()
        y = self.__y + other.get_y()
        return Vector2D(x, y)

    def __sub__(self, other):
        x = self.__x - other.get_x()
        y = self.__x - other.get_y()
        return Vector2D(x, y)

    def __mul__(self, number: float or int):
        x = self.__x * number
        y = self.__y * number
        return Vector2D(x, y)

    def __eq__(self, other):
        AB1 = math.sqrt(self.__x ** 2 + self.__y ** 2)
        AB2 = math.sqrt(other.get_x() ** 2 + other.get_y() ** 2)
        return AB1 == AB2

    def __ne__(self, other):
        AB1 = math.sqrt(self.__x ** 2 + self.__y ** 2)
        AB2 = math.sqrt(other.get_x() ** 2 + other.get_y() ** 2)
        return AB1 != AB2

    def __gt__(self, other):
        AB1 = math.sqrt(self.__x ** 2 + self.__y ** 2)
        AB2 = math.sqrt(other.get_x() ** 2 + other.get_y() ** 2)
        return AB1 > AB2

    def __lt__(self, other):
        AB1 = math.sqrt(self.__x ** 2 + self.__y ** 2)
        AB2 = math.sqrt(other.get_x() ** 2 + other.get_y() ** 2)
        return AB1 < AB2

    def __ge__(self, other):
        AB1 = math.sqrt(self.__x ** 2 + self.__y ** 2)
        AB2 = math.sqrt(other.get_x() ** 2 + other.get_y() ** 2)
        return AB1 >= AB2

    def __le__(self, other):
        AB1 = math.sqrt(self.__x ** 2 + self.__y ** 2)
        AB2 = math.sqrt(other.get_x() ** 2 + other.get_y() ** 2)
        return AB1 <= AB2


v1 = Vector2D(10, 20)
v2 = Vector2D(20, 30)

print(v1, v2)
print(v1.__le__(v2))
v3 = v1.__add__(v2)
print(v3)
print(v1 == v2)
