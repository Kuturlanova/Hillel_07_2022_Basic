# Homework_1

class Car:
    def __init__(self, name, year, manufacturer, volume, color, price) -> None:
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.volume = volume
        self.color = color
        self.price = price

    def show_details(self):
        print(f"Car name: {self.name}\nYear of issue:{self.year}\nManufacturer:{self.manufacturer}\n"
              f"Engine volume:{self.volume}\nColor:{self.color}\nPrice: {self.price}")

    def name(self):
        print(f'Car name:{self.name}')
        return self.name

    def year(self):
        print(f'Year of issue:{self.year}')
        return self.year

    def manufacturer(self):
        print(f'Manufacturer:{self.manufacturer}')
        return self.manufacturer

    def volume(self):
        print(f'Engine volume:{self.volume}')
        return self.volume

    def color(self):
        print(f'Color:{self.color}')
        return self.color

    def price(self):
        print(f'Price:{self.price}')
        return self.price


honda = Car(name="Honda Accord", year="2019", manufacturer="Honda Motor Co., Ltd.", volume="3,5 l", color="White",
            price=27000)
tesla = Car(name="Tesla Model 3", year="2020", manufacturer="Tesla", volume="Electric", color="Red", price=40000)

Car.show_details(honda)
Car.show_details(tesla)

Car.name(honda)
Car.name(tesla)

Car.year(honda)
Car.year(tesla)

Car.manufacturer(honda)
Car.manufacturer(tesla)

Car.volume(honda)
Car.volume(tesla)

Car.color(honda)
Car.color(tesla)

Car.price(honda)
Car.price(tesla)


# Homework_2

class Book:
    def __init__(self, name, year, edition, genre, author, price) -> None:
        self.name = name
        self.year = year
        self.edition = edition
        self.genre = genre
        self.author = author
        self.price = price

    def show_details(self):
        print(f"Book name: {self.name}\nYear of publication:{self.year}\nPublishing house:{self.edition}\n"
              f"Book genre:{self.genre}\nAuthor:{self.author}\nPrice: {self.price}")

    def show_genre(self):
        print(f"Book genre:{self.genre}")

    def show_edition(self):
        print(f"Publishing house:{self.edition}")

    def show_name(self):
        print(f"Book name:{self.name}")

    def show_year(self):
        print(f"Year of publication:{self.year}")

    def show_author(self):
        print(f"Author:{self.author}")

    def show_price(self):
        print(f"Price:{self.price}")


getsbi = Book(name="The Great Gatsby", year="1925", edition="Scribner’s", genre="Novel",
              author="Francis Scott Key Fitzgerald", price="8 $")
potter = Book(name="Harry Potter and the Philosopher's Stone", year="1997", edition="Bloomsbury Publishing",
              genre="Novel", author="Joanne Rowling", price="9 $")

Book.show_details(getsbi)
Book.show_details(potter)

Book.show_name(getsbi)
Book.show_name(potter)

Book.show_year(getsbi)
Book.show_year(potter)

Book.show_genre(getsbi)
Book.show_genre(potter)

Book.show_edition(getsbi)
Book.show_edition(potter)

Book.show_author(getsbi)
Book.show_author(potter)

Book.show_price(getsbi)
Book.show_price(potter)


# Homework_3

class Stadium:
    def __init__(self, name, year, country, city, placement) -> None:
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.placement = placement

    def show_details(self):
        print(f"Stadium name: {self.name}\nYear of opening:{self.year}\nCountry:{self.country}\n"
              f"City:{self.city}\nPlacement:{self.placement}")

    def show_name(self):
        print(f"Stadium name: {self.name}")
        return self.name

    def show_placement(self):
        print(f"Placement:{self.placement}")
        return self.placement


santiago = Stadium(name="Estadio Santiago Bernabéu", year="1947", country="Spain", city="Madrid", placement="81044")
france = Stadium(name="Stade de France", year="19987", country="France", city="Sen-Deni", placement="81338")

Stadium.show_details(santiago)
Stadium.show_details(france)

Stadium.show_name(santiago)
Stadium.show_name(france)

Stadium.show_placement(santiago)
Stadium.show_placement(france)
