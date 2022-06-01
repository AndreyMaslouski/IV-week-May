class Car:
    # Статические поля (переменные класса)
    default_color = 'Grey'
    default_weight = 5000

    def __init__(self, color, model):
        # Динамические поля (переменные объекта)
        self.color = color
        self.model = model

    def turn_on(self):
        pass

    def ride(self):
        pass


car_object = Car('red', 'BMW')

print(car_object.default_color)
print(car_object.color)

print(dir(Car))