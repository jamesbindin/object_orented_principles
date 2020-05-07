class Demo:
    def __init__(self, a):
       self.a = a

# use magic methods to allow more than one behaviour for operators
# the '+' operator relates to the __add__ method
    def __add__(self, other):
        return self.a + other.a


b = Demo(1)
a = Demo(2)
# when more than one object of the class Demo are added the __add__ method is called
print(b + a)
