# Статические и динамические атрибуты класса
#  Класс может содержать атрибуты и методы. Атрибут может быть статическим и динамическим (уровня объекта класса).
# Суть в том, что для работы со статическим атрибутом, Нам не нужно создавать экземпляр класса, а для работы с
# динамическим - нужно. Пример:

class Rectangle:
    default_color="green"

    def __init__(self,width,height):
        self.width=width
        self.height=height

# В представленном выше классе, атрибут default_color - это статический атрибут, и доступ к нему, как было сказано выше,
# можно получить не создавая объект класса Rectangle

Rectangle.default_color
# green'

# width и height - это динамические атрибуты, при их создании было использовано ключевое слово self. Для доступа к
# width и height предварительно нужно создать объект класса Rectangle:

rect=Rectangle(10,20)
rect.width
# 10
rect.height

# Если обратиться через класс, то получим Ошибку:
# Rectangle.width

# Traceback (most recent call last):
#   File "C:/Users/Андрей/PycharmProjects/prob/OOP/practic_2.py", line 28, in <module>
#     Rectangle.width
# AttributeError: type object 'Rectangle' has no attribute 'width'

# При этом, если вы обратитесь к статическому атрибуту через
# экземпляр класса, то все будет ОК, до тех пор, пока вы не попытаетесь
# его поменять.
#
# Проверим ещё раз значение атрибута default_color:

Rectangle.default_color
# green'
# Присвоим ему новое значение:
Rectangle.default_color="red"
Rectangle.default_color
# red'

# Создадим два объекта класса Rectangle и проверим, что default_color у
# них совпадает:
r1=Rectangle(1,2)
r2=Rectangle(10,20)
r1.default_color
# red'
r2.default_color
# red'

# Если поменять значение default_color через имя класса Rectangle, то
# все будет ожидаемо: у объектов r1 и r2 это значение изменится, но
# если поменять его через экземпляр класса, то у экземпляра будет
# создан атрибут с таким же именем как статический, а доступ к
# последнему будет потерян:
#
# Меняем default_color через r1:

r1.default_color = "blue"
r1.default_color
# blue'

# При этом у r2 остается значение статического атрибута:
r2.default_color
# red'
Rectangle.default_color
# red'

# Вообще напрямую работать с атрибутами – не очень хорошая идея,
# лучше для этого использовать свойства.