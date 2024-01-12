# No_1
print('No_1')


class Cook:
    def __init__(self, name: str, speciality: str, post: str, salary: float) -> None:
        self.__name = name
        self.__speciality = speciality
        self.__post = post
        self.__salary = salary

    def __str__(self) -> str:
        return (f'Name: {self.__name}\n'
                f'Speciality: {self.__speciality}\n'
                f'Post: {self.__post}\n'
                f'Salary: {self.__salary}')

    def get_name(self) -> str:
        return self.__name

    def get_speciality(self) -> str:
        return self.__speciality

    def get_post(self) -> str:
        return self.__post

    def get_salary(self) -> float:
        return self.__salary

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_speciality(self, new_speciality: str):
        self.__speciality = new_speciality

    def set_post(self, new_post: str):
        self.__post = new_post

    def set_salary(self, new_salary: float):
        self.__salary = new_salary

    def check_speciality(self, dish) -> bool:
        if dish.get_speciality() == self.__speciality:
            return True
        else:
            return False

    def cooking(self):
        print('The dish is ready!')

    def __eq__(self, other):
        post_1 = 1
        post_2 = 1
        if self.__post == 'chef':
            post_1 *= 2
        if other.__post == 'chef':
            post_2 *= 2
        return post_1 == post_2

    def __ne__(self, other):
        post_1 = 1
        post_2 = 1
        if self.__post == 'chef':
            post_1 *= 2
        if other.__post == 'chef':
            post_2 *= 2
        return post_1 != post_2

    def __gt__(self, other):
        post_1 = 1
        post_2 = 1
        if self.__post == 'chef':
            post_1 *= 2
        if other.__post == 'chef':
            post_2 *= 2
        return post_1 > post_2

    def __lt__(self, other):
        post_1 = 1
        post_2 = 1
        if self.__post == 'chef':
            post_1 *= 2
        if other.__post == 'chef':
            post_2 *= 2
        return post_1 < post_2


class Dish:
    def __init__(self, name: str, speciality: str, price: float) -> None:
        self.__name = name
        self.__speciality = speciality
        self.__price = price

    def get_name(self) -> str:
        return self.__name

    def get_speciality(self) -> str:
        return self.__speciality

    def get_price(self) -> float:
        return self.__price

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_specialization(self, new_speciality: str):
        self.__speciality = new_speciality

    def set_price(self, new_price: float):
        self.__price = new_price


cook1 = Cook('Gordon', 'chef', 'chef', 4000)
cook2 = Cook('Takuma', 'su-chef', 'cook', 3000)
dish_1 = Dish('sushi', 'su-chef', 30)

if cook2.check_speciality(dish_1):
    cook2.cooking()
print(cook1 > cook2)
print(cook1 < cook2)
print(cook1 == cook2)
print(cook1 != cook2)
print('')


# No_2
print('No_2')


class Waiter:
    def __init__(self, name: str, level: 1-3, salary: float) -> None:
        self.__name = name
        self.__level = level
        self.__salary = salary

    def __str__(self) -> str:
        return (f'Name: {self.__name}\n'
                f'Level: {self.__level}\n'
                f'Salary: {self.__salary}')

    def get_name(self) -> str:
        return self.__name

    def get_level(self) -> str:
        return self.__level

    def get_salary(self) -> float:
        return self.__salary

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_level(self, new_level: 1 - 3):
        self.__level = new_level

    def set_salary(self, new_salary: float):
        self.__salary = new_salary

    def servicing(self, table: int):
        print(f'The table {table} served!')

    def check_level(self, people: int):
        if people <= 2 and people > 0:
            buff = 1
            if self.__level >= buff:
                return True
            else:
                return False
        elif people <= 4 and people > 2:
            buff = 2
            if self.__level >= buff:
                return True
            else:
                return False
        elif people <= 6 and people > 4:
            buff = 3
            if self.__level >= buff:
                return True
            else:
                return False
        else:
            return False


waiter1 = Waiter('Nikolay', 3, 1300)
waiter2 = Waiter('Robert', 2, 1100)

print(waiter1.check_level(8))
print(waiter2)
waiter1.servicing(3)
print('')

# No_3
print('No_3')


class Track:
    def __init__(self, name: str, artist: str, album: str, genre: str, duration: int) -> None:
        self.__name = name
        self.__artist = artist
        self.__album = album
        self.__genre = genre
        self.__duration = duration

    def __str__(self) -> str:
        return (f'Name: {self.__name}\n'
                f'Artist: {self.__artist}\n'
                f'Album: {self.__album}\n'
                f'Genre: {self.__genre}\n'
                f'Duration: {self.__duration}')

    def get_name(self) -> str:
        return self.__name

    def get_artist(self) -> str:
        return self.__artist

    def get_album(self) -> str:
        return self.__album

    def get_genre(self) -> str:
        return self.__genre

    def get_duration(self) -> int:
        return self.__duration

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_artist(self, new_artist: str):
        self.__artist = new_artist

    def set_album(self, new_album: str):
        self.__album = new_album

    def set_genre(self, new_genre: str):
        self.__genre = new_genre

    def set_duration(self, new_duration: int):
        self.__duration = new_duration


class Album:
    def __init__(self, name: str, artist: str, year: int, tracks: list) -> None:
        self.__name = name
        self.__artist = artist
        self.__year = year
        self.__tracks = tracks

    def __str__(self) -> str:
        lst = []
        for i in self.__tracks:
            lst.append(i.get_name())

        return (f'Name: {self.__name}\n'
                f'Artist: {self.__artist}\n'
                f'Year: {self.__year}\n'
                f'Tracks: {", ".join(lst)}')

    def get_name(self) -> str:
        return self.__name

    def get_artist(self) -> str:
        return self.__artist

    def get_year(self) -> int:
        return self.__year

    def get_tracks(self) -> list:
        return self.__tracks

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_artist(self, new_artist: str):
        self.__artist = new_artist

    def set_year(self, new_year: int):
        self.__year = new_year

    def add_track(self, track):
        if track not in self.__tracks:
            self.__tracks.append(track)

    def del_track(self, track: str):
        if track in self.__tracks:
            self.__tracks.remove(track)


class Artist:
    def __init__(self, name: str, albums: list) -> None:
        self.__name = name
        self.__albums = albums

    def __str__(self) -> str:
        lst = []
        for i in self.__albums:
            lst.append(i.get_name())
        return (f'Name: {self.__name}\n'
                f'Albums: {", ".join(lst)}')

    def get_name(self) -> str:
        return self.__name

    def get_albums(self) -> list:
        return self.__albums

    def set_name(self, new_name: str):
        self.__name = new_name

    def add_album(self, album):
        if album not in self.__albums:
            self.__albums.append(album)

    def del_album(self, album):
        if album in self.__albums:
            self.__albums.remove(album)


class MusicCollection:
    def __init__(self) -> None:
        self.__tracks = []
        self.__albums = []
        self.__artists = []

    def __str__(self):
        return (f'Artists: {", ".join(self.__artists)}\n'
                f'Albums: {", ".join(self.__albums)}\n'
                f'Tracks: {", ".join(self.__tracks)}')

    def get_tracks(self) -> list:
        return self.__tracks

    def get_albums(self) -> list:
        return self.__albums

    def get_artists(self) -> list:
        return self.__artists

    def add_track(self, track):
        if track.get_name() not in self.__tracks:
            self.__tracks.append(track.get_name())
            if track.get_album() not in self.__albums:
                self.__albums.append(track.get_album())
            if track.get_artist() not in self.__artists:
                self.__artists.append(track.get_artist())

    def del_track(self, track: str):
        if track in self.__tracks:
            self.__tracks.remove(track)

    def add_album(self, album):
        if album.get_name() not in self.__albums:
            self.__albums.append(album.get_name())
        if len(album.get_tracks()) > 0:
            for i in album.get_tracks():
                self.add_track(i)

    def add_artist(self, artist):
        if artist.get_name() not in self.__artists:
            self.__artists.append(artist.get_name())
        if len(artist.get_albums()) > 0:
            for i in artist.get_albums():
                self.add_album(i)


# tracks
track_1 = Track('Numb', 'Linkin Park', 'Meteora', 'Hard Rock', 176)
track_2 = Track('Enter Sandman', 'Metallica', 'The Black Album', 'Metal', 330)
track_3 = Track('Sad but true', 'Metallica', 'The Black Album', 'Metal', 424)
track_4 = Track('The Unforgiven', 'Metallica', 'The Black Album', 'Metal', 656)

# albums
album_1 = Album('The Black Album', 'Metallica', 1991, [])

# artists
artist_1 = Artist('Metallica', [])

# collections
collection_1 = MusicCollection()

album_1.add_track(track_2)
album_1.add_track(track_3)
album_1.add_track(track_4)
print('Album')
print(album_1)
print('')

artist_1.add_album(album_1)
print('Artist')
print(artist_1)
print('')

collection_1.add_artist(artist_1)
print('Music collection')
print(collection_1)
print('')
