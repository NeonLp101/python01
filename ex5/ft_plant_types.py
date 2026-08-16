class Plant():
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = float(new_height)
        else:
            print(f"{self._name}: Error, height can't be negative")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
        else:
            print(f"{self._name}: Error, age can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height = self._height + self._growth_rate

    def age_up(self) -> None:
        self._age = self._age + 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, 0.8, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 0.5, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_up()
    tomato.show()
