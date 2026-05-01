class Parent:
    def __init__(self, first_name, favourite_food, hobby, catchphrase, age):
        self.first_name = first_name
        self.favourite_food = favourite_food
        self.hobby = hobby
        self.catchphrase = catchphrase
        self.age = age

    def speak(self):
        print(f"Hello, I am {self.first_name} and I am {self.age}: {self.catchphrase}")

    def introduce(self):
        print(f"{self.first_name} enjoys {self.favourite_food} and likes {self.hobby}.")

    def relax(self):
        print(f"{self.first_name} is now chilling.")

    def indulge(self):
        print(f"{self.first_name} is now eating {self.favourite_food}.")


class Child(Parent):  # Child inherits from Parent
    def speak(self):
        print(f"Hi, I am {self.first_name} and I am {self.age}: {self.catchphrase}")

    def introduce(self):
        print(f"{self.first_name} enjoys {self.favourite_food} and likes {self.hobby}.")

    def relax(self):
        print(f"{self.first_name} is now chilling.")

    def indulge(self):
        print(f"{self.first_name} is now eating {self.favourite_food}.")