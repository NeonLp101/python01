class Plant():
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = float(height)
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age} days old")

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age_up(self) -> None:
        self.age = self.age + 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    Rose = Plant("Rose", 25, 30, 0.8)
    start = Rose.height
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        Rose.show()
        Rose.grow()
        Rose.age_up()
    print(f"Growth this week: {round(Rose.height - start)}cm")
