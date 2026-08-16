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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    Rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    Rose.show()
    print()
    Rose.set_height(25)
    print(f"Height updated: {round(Rose.get_height())}cm")
    Rose.set_age(30)
    print(f"Age updated: {Rose.get_age()} days")
    print()
    Rose.set_height(-5)
    print("Height update rejected")
    Rose.set_age(-3)
    print("Age update rejected")
    print()
    print("Current state: ", end="")
    Rose.show()
