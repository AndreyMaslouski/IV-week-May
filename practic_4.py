# Калькулятор. Создайте Класс, где реализованы функции (методы) математических операций.
# А также функция, для ввода данных.


# a = float(input("Введите первое дробное число: "))
# c = input("Введите операцию(+,*,/,-): ")
# b = float(input("Введите второе дробное число: "))

# if c=='+':
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=='*':
#     print(a*b)
# else:
#     print(a/b)

class Calc:

    def __init__(self):
        self.vvod()

    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def dele(self):
        if self.b==0:
            return "error"
        else:
            return self.a / self.b
    def umn(self):
        return self.a * self.b
    def vvod(self):
        self.a=int(input("Введите первое число: "))
        self.b=int(input("Введите второе число: "))

while True:
    ex = Calc()
    c = input("Введите операцию(+,*,/,-): ")

    if c=='+':
        print(ex.plus())
    elif c=="-":
        print(ex.minus())
    elif c=='*':
        print(ex.umn())
    elif c=='0':
        break
    else:
        print(ex.dele())

