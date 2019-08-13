"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.
    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.
    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID
Гараж має наступні характеристики:
    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.
    Повинен мати реалізованими наступні методи
    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.
    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.
    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

import random
import uuid
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS


class Car:

    def __init__(self, producer: CARS_PRODUCER, car_type: CARS_TYPES, price: float, mileage: float):
        self.price = price
        self.number = uuid.uuid4()
        self.mileage = mileage
        self.producer = producer
        self.car_type = car_type if car_type in CARS_TYPES else None

    def __repr__(self):
        return 'producer: {self.producer}, type: {self.car_type}, price: {self.price}, ' \
               'mileage: {self.mileage}, number: {self.number}'.format(self=self)

    def change_number(self):
        self.number = uuid.uuid4()

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __gt__(self, other):
        return self.price > other.price


class Garage:

    def __init__(self, cars, places, town: TOWNS, owner=None):
            self.town = town if town in TOWNS else None
            self.cars = cars
            self.places = places
            self.owner = owner if owner else uuid.uuid4()

    def __repr__(self):
        return 'town: {self.town}, car: {self.cars}, place: {self.places}, ownerid: {self.owner}'.format(self=self)

    def add_car(self, car: Car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return f'Car was added to garage: {self.town}'

    def free_places(self):
        return self.places - len(self.cars)

    def remove_car(self, car: Car):
        self.cars.remove(car)

    def hit_hat(self):
        sum_car = 0
        for car in self.cars:
            sum_car = sum_car + car.price
        return sum_car

class Cesar:


    def __init__(self, name: str, garages=[]):
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()

    def __str__(self):
        return 'name: {self.name}, garage: {self.garages}, id: {self.register_id}'.format(self=self)

    def hit_hat(self):
        car_price = 0
        for garage in self.garages:
            for car in garage.cars:
                car_price += car.price
        return car_price

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        car_amount = 0
        for garage in self.garages:
            len(garage.cars)
            car_amount += 1
        return car_amount

    def add_car(self, car, garage=None):
        if garage is None:
            maximum = 0
            max_garage = None
            for garage in self.garages:
                if garage.free_places() >= maximum:
                    maximum = garage.free_places()
                    max_garage = garage
            return max_garage.add_car(car) if garage else 'no free space'
        else:
            return garage.add_car(car)

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()


if __name__ == "__main__":
    cesar_id = uuid.uuid4()
    print("id of cesar: ", cesar_id)
    print(" ")

    garages = []

    for _ in range(5):
        garage = Garage(
            cars=[],
            town=random.choice(TOWNS),
            places=4,
            owner=cesar_id
        )
        garages.append(garage)

    cesar1 = Cesar('Tom', garages)
    cesar2 = Cesar('James', garages)

    cars = []
    for _ in range(10):
        car = Car(
            car_type=random.choice(CARS_TYPES),
            producer=random.choice(CARS_PRODUCER),
            price=random.uniform(100000, 1000000),
            mileage=random.uniform(25, 10000)
        )
        cars.append(car)

        cesar1.add_car(car, random.choice(garages))
        cesar2.add_car(car, random.choice(garages))

