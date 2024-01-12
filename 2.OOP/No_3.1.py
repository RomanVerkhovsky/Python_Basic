print('No_1')


class Animal:
    def __init__(self, name: str, kind: str, age: int, sounds: list) -> None:
        self.__name = name
        self.__kind = kind
        self.__age = age
        self.__sounds = sounds

    def __str__(self) -> str:
        return (f'Name: {self.__name}\n'
                f'Kind: {self.__kind}\n'
                f'Age: {self.__age}\n'
                f'Sounds: {", ".join(self.__sounds)}')

    def get_name(self) -> str:
        return self.__name

    def get_kind(self) -> str:
        return self.__kind

    def get_age(self) -> int:
        return self.__age

    def get_sounds(self) -> list:
        return self.__sounds

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def add_sound(self, sound):
        if sound not in self.__sounds:
            self.__sounds.append(sound)

    def del_sound(self, sound):
        if sound in self.__sounds:
            self.__sounds.remove(sound)


animal_1 = Animal('Rex', 'Dog', 4, ['gav'])
print(animal_1)
print('')
animal_1.add_sound('uav')
print(animal_1.get_sounds())
print('')
animal_1.set_age(5)
print(animal_1)
print('')


# No_2
print('No_2')


class Book:
    def __init__(self, name: str, author: str, page_count: int) -> None:
        self.__name = name
        self.__author = author
        self.__page_count = page_count

    def __str__(self) -> str:
        return (f'Name: {self.__name}\n'
                f'Author: {self.__author}\n'
                f'Number of page: {self.__page_count}')

    def get_name(self) -> str:
        return self.__name

    def get_author(self) -> str:
        return self.__author

    def get_number_pages(self) -> int:
        return self.__page_count

    def open_page(self, number_page):
        if number_page > self.__page_count:
            print("Error: The book do not contain such number of page")
        else:
            print(f'Page {number_page} opened')


book_1 = Book('The Shining', 'Stephen King', 150)
print(book_1)
book_1.open_page(6)
book_1.open_page(500)

print('')


# No_3
print('No_3')


class PassengerPlane:
    def __init__(self, manufacturer: str, model: str, capacity: int, cur_height: float, cur_speed: float) -> None:
        self.__manufacturer = manufacturer
        self.__model = model
        self.__capacity = capacity
        self.__cur_height = cur_height
        self.__cur_speed = cur_speed
        self.__take_off = False
        self.__landing = False

    def __str__(self) -> str:
        return (f'Manufacturer: {self.__manufacturer}\n'
                f'Model: {self.__model}\n'
                f'Capacity: {self.__capacity} passengers\n'
                f'Height: {self.__cur_height}\n'
                f'Speed: {self.__cur_speed}\n'
                f'Takeoff activity: {self.__take_off}\n'
                f'Landing activity: {self.__landing}')

    def get_manufacturer(self) -> str:
        return self.__manufacturer

    def get_model(self) -> str:
        return self.__model

    def get_capacity(self) -> int:
        return self.__capacity

    def get_current_height(self) -> float:
        return self.__cur_height

    def get_current_speed(self) -> float:
        return self.__cur_speed

    def set_current_height(self, new_height):
        if new_height >= 0 and new_height <= 13100:
            self.__cur_height = new_height

    def set_current_speed(self, new_speed):
        if new_speed >= 0 and new_speed <= 956:
            self.__cur_speed = new_speed

    def on_take_off(self):
        self.__take_off = True
        self.__landing = False
        print('The plane begins to take off')

    def off_take_off(self):
        self.__take_off = False
        print('The plane took off successfully')

    def on_landing(self):
        self.__landing = True
        self.__take_off = False
        print('The plane begins to landing')

    def off_landing(self):
        self.__landing = False
        print('The plane landing successfully')


plan_1 = PassengerPlane('The Boing Company', 'Boing 787', 300, 0, 0)
print(f'INFO:\n{plan_1}')
print('')
print('INFO')
plan_1.on_take_off()
print('')
print('INFO')
plan_1.off_take_off()
print('')
plan_1.set_current_height(5000)
plan_1.set_current_speed(800)
print('INFO')
print(plan_1)
print('')
print('INFO')
plan_1.on_landing()
print('')
print('INFO')
plan_1.off_landing()
print('')
print('INFO')
print(plan_1)
print('')


# No_4
print("No_4")


class MusicAlbum:
    def __init__(self, artist: str, album: str, genre, tracklist: list) -> None:
        self.__artist = artist
        self.__album = album
        self.__genre = genre
        self.__tracklist = tracklist

    def __str__(self) -> str:
        return (f'Artist: {self.__artist}\n'
                f'Album: {self.__album}\n'
                f'Genre: {self.__genre}\n'
                f'Tracklist: {", ".join(self.__tracklist)}')

    def get_artist(self) -> str:
        return self.__artist

    def get_album(self) -> str:
        return self.__album

    def get_genre(self) -> str:
        return self.__genre

    def get_tracklist(self) -> list:
        return self.__tracklist

    def add_track(self, track: str):
        if track not in self.__tracklist:
            self.__tracklist.append(track)

    def del_track(self, track: str):
        if track in self.__tracklist:
            self.__tracklist.remove(track)

    def play_track(self, track: str):
        if track in self.__tracklist:
            print(f'"{track}" is playing...')


album_1 = MusicAlbum('Metallica', 'The Black Album', 'metal', ['Enter Sandman'])
print(album_1)
print('')
album_1.play_track('Enter Sandman')
album_1.add_track('Sad but true')
print(album_1.get_tracklist())
print('')
print(album_1)
print('')
album_1.del_track('Enter Sandman')
print(album_1)
print('')
album_1.del_track('Sad but true')
print(album_1)

# No_5
print('No_5')


class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self) -> str:
        return f'{self.__numerator}/{self.__denominator}'

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def __add__(self, other):
        numerator = self.__numerator + other.__numerator
        denominator = self.__denominator + other.__denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.__numerator - other.__numerator
        denominator = self.__denominator - other.__b
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__numerator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        first = self.__numerator / self.__denominator
        second = other.__numerator / other.__denominator
        return first == second

    def __ne__(self, other):
        first = self.__numerator / self.__denominator
        second = other.__numerator / other.__denominator
        return first != second

    def __gt__(self, other):
        first = self.__numerator / self.__denominator
        second = other.__numerator / other.__denominator
        return first > second

    def __lt__(self, other):
        first = self.__numerator / self.__denominator
        second = other.__numerator / other.__denominator
        return first < second

    def __ge__(self, other):
        first = self.__numerator / self.__denominator
        second = other.__numerator / other.__denominator
        return first >= second

    def __le__(self, other):
        first = self.__numerator / self.__denominator
        second = other.__numerator / other.__denominator
        return first <= second


fraction_1 = Fraction(3, 4)
fraction_2 = Fraction(5, 3)
fraction_3 = fraction_1 + fraction_2
fraction_4 = fraction_1 / fraction_2
print(f'{fraction_1} + {fraction_2} = {fraction_3}')
print(f'{fraction_1} / {fraction_2} = {fraction_4}')
print(fraction_1 > fraction_2)
