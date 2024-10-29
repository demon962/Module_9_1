class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        return f"{self.name} ест."

    def sleep(self):
        return f"{self.name} спит."


class Plant:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def grow(self):
        return f"{self.name} растет."

    def photosynthesize(self):
        return f"{self.name} фотосинтезирует."


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_color):
        super().__init__(name, age, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} рожает детенышей."


class Predator(Mammal):
    def __init__(self, name, age, habitat, fur_color, prey):
        super().__init__(name, age, habitat, fur_color)
        self.prey = prey

    def hunt(self):
        return f"{self.name} охотится на {self.prey}."


class Flower(Plant):
    def __init__(self, name, age, habitat, color):
        super().__init__(name, age, habitat)
        self.color = color

    def bloom(self):
        return f"{self.name} цветет."


class Fruit(Plant):
    def __init__(self, name, age, habitat, taste):
        super().__init__(name, age, habitat)
        self.taste = taste

    def ripen(self):
        return f"{self.name} созревает."


lion = Predator("Лев", 5, "Саванна", "рыжий", "зебра")
rose = Flower("Роза", 2, "Сад", "красный")
apple = Fruit("Яблоня", 3, "Сад", "сладкий")

print(lion.eat())
print(lion.hunt())
print(rose.grow())
print(rose.bloom())
print(apple.grow())
print(apple.ripen())
