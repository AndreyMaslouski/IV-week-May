# Пример простейшего класса, который ничего не делает
# class A:
#     pass
# Теперь Мы можем создать несколько экземпляров этого класса:
# a = A()
# b = A()
# a.arg = 1    # у экземпляра а появился атрибут arg, равный 1
# b.arg = 2    # a у экземпляра b - атрибут arg, равный 2
# print(a.arg)
# Результат: 1
# print (b.arg)
# Результат: 2
# c = A
# print(c.arg)    # а у этого экземпляра нет arg
# Результат:
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'A' object has no attribute 'arg'

# Классу возможно задать собственные методы:
class A:
    def g(self):    #self - обязательный аргумент, содержащий в себе экземпляр класса,передающийся при вызове метода,
                    # поэтому этот аргумент должен присутствовать
                    # во всех методах класса.
        return 'hello world'

a = A()
print(a.g())
# Результат: 'hello world'

# И напоследок ещё один пример:
class B:
    arg = 'Python' # Все экземпляры этого класса будут иметь атрибут arg,
                    # равный "Python"
                    # Но впоследствии Мы его можем изменить
    def g(self):
        return self.arg

b = B()
print(b.g())
# Результат: 'Python'
print(B.g(b))
# Результат: 'Python'
b.arg = 'spam'
print(b.g())
# Результат: 'spam'




