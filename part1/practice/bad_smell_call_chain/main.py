# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, city_population: int, room_num: int):
        self.population = city_population
        self.room = room_num

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.population


person1 = Person(100000, 5)
print(person1.get_person_room())
print(person1.get_city_population())
