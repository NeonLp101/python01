class Plant():
    class Stats():
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._height = 0.0
        self._age = 0
        self._stats = self._make_stats()
        self.set_height(height)
        self.set_age(age)

    def _make_stats(self) -> "Plant.Stats":
        return Plant.Stats()

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    def show(self) -> None:
        self._stats.record_show()
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
        self._stats.record_grow()
        self._height = self._height + self._growth_rate

    def age_up(self) -> None:
        self._stats.record_age()
        self._age = self._age + 1

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color: str,
                 seed_count: int) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        seeds = self._seed_count if self._bloomed else 0
        print(f" Seeds: {seeds}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = float(trunk_diameter)

    def _make_stats(self) -> "Plant.Stats":
        return Tree.TreeStats()

    def produce_shade(self) -> None:
        stats = self._stats
        if isinstance(stats, Tree.TreeStats):
            stats.record_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, 8.0, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 0.5, 5)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, 30.0, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)
