# task 1
from email.policy import default


class Soda:
    def __init__(self, taste=None):
        if isinstance(taste, str) and taste.isalpha():
            self.taste = taste
        else:
            self.taste = None

    def taste_soda(self):
        if self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        return "У вас обычная газировка"


user_input = input("What taste does your soda have? ")
if user_input and not user_input.isalpha():
    print("Ошибка: введите вкус буквами")
else:
    soda_taste = Soda(user_input)
    print(soda_taste.taste_soda())


# task 2
class Math:
    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            self.x = None
            self.y = None

    def addition(self):
        if self.x is not None and self.y is not None:
            return self.x + self.y
        return "Error: enter incorrect data"

    def subtraction(self):
        if self.x is not None and self.y is not None:
            return self.x - self.y
        return "Error: enter incorrect data"

    def multiplication(self):
        if self.x is not None and self.y is not None:
            return self.x * self.y
        return "Error: enter incorrect data"

    def division(self):
        if self.x is not None and self.y is not None:
            return self.x / self.y
        return "Error: enter incorrect data"


def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Enter only numbers!")


x_input = get_number_input("What is the first number? ")
y_input = get_number_input("What is the second number? ")

my_math = Math(x_input, y_input)
print(f"Addition: {my_math.addition()}")
print(f"Subtraction: {round(my_math.subtraction(), 4)}")
print(f"Multiplication: {my_math.multiplication()}")
print(f"Division: {round(my_math.division(), 4)}")


# task 3
class Car:
    def __init__(self, colour, type, year):
        self.colour = colour
        self.type = type
        self.year = year

    def car_is_started(self):
        print("The car is started!")

    def car_off(self):
        print("The engine is off!")

    def car_info(self):
        print(f"Car information: colour: {self.colour}, type: {self.type}, year: {self.year}")


def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            year = int(user_input)
            if 1990 <= year <= 2026:
                return year
            else:
                print("Year must be between 1990 and 2026!")
        except ValueError:
            print("Year must be an integer number!")


def get_text_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("Enter only words!")


colour_input = get_text_input("What colour does your car have? ")
type_input = get_text_input("What type of car is yours? ")
year_input = get_number_input("What is the year of your car? ")
my_car = Car(colour_input, type_input, year_input)
my_car.car_is_started()
my_car.car_off()
my_car.car_info()

# task 4
import math


class Sphere:
    def __init__(self, radius=1, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def get_square(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x_point, y_point, z_point):
        distance = math.sqrt((x_point - self.x) ** 2 + (y_point - self.y) ** 2 + (z_point - self.z) ** 2)
        return distance <= self.radius


def get_number_input(prompt, default):
    while True:
        user_input = input(prompt)
        if not user_input:
            return default
        try:
            return float(user_input)
        except ValueError:
            print("Enter only numbers!")


radius_sph = get_number_input("Radius (default 1): ", 1.0)
while radius_sph <= 0:
    print("Radius must be greater than 0!")
    radius_sph = get_number_input("Radius (default 1): ", 1.0)
x_coord = get_number_input("Coordinate X (default 0): ", 0.0)
y_coord = get_number_input("Coordinate Y (default 0): ", 0.0)
z_coord = get_number_input("Coordinate Z (default 0): ", 0.0)
my_sphere = Sphere(radius_sph, x_coord, y_coord, z_coord)
print(f"Volume: {my_sphere.get_volume()}")
print(f"Surface Area: {my_sphere.get_square()}")
print(f"Radius: {my_sphere.get_radius()}")
print(f"Center: {my_sphere.get_center()}")
new_radius = get_number_input("Enter new radius: ", 1.0)
if new_radius > 0:
    my_sphere.set_radius(new_radius)  # ВЫЗОВ МЕТОДА
    print(f"New radius is set: {my_sphere.get_radius()}")
else:
    print("Error: radius must be a positive number!")
new_x = get_number_input("New coordinate X of the sphere center: ", 0.0)
new_y = get_number_input("New coordinate Y of the sphere center: ", 0.0)
new_z = get_number_input("New coordinate Z of the sphere center: ", 0.0)
my_sphere.set_center(new_x, new_y, new_z)
print(f"New center position: {my_sphere.get_center()}")
x_point = get_number_input("Coordinate X of a random point: ", 0.0)
y_point = get_number_input("Coordinate Y of a random point: ", 0.0)
z_point = get_number_input("Coordinate Z of a random point: ", 0.0)
if my_sphere.is_point_inside(x_point, y_point, z_point):
    print("The point is inside the sphere!")
else:
    print("The point is outside the sphere!")


# task 5

class SuperStr(str):
    def is_repeatance(self, s):
        # Проверяем, что s не пустая, и текущая строка не пустая
        if not s or not self:
            return False

        # Строка может быть получена повтором s, если:
        # Длина основной строки делится на длину s без остатка
        # Результат умножения s на это количество повторов равен исходной строке
        count = len(self) // len(s)
        return s * count == self

    def is_palindrom(self):
        if not self:
            return True
        s_low = self.lower()
        return s_low == s_low[::-1]


def get_text_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("Enter only words!")


user_input = get_text_input("Enter a string: ")
s = SuperStr(user_input)
repeat_s = get_text_input("Enter a substring to check repeatability: ")
print(f"Is repeatable? {s.is_repeatance(repeat_s)}")
print(f"Is palindrome? {s.is_palindrom()}")
