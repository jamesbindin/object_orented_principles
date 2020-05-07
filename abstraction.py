class Hide:
    def __init__(self, name, a, b):
        self.__name = name
        self.a = a
        self.b = b

    def get_name(self):
        return self.__name

    def mean(self):
        return self.__total()/2

    def __total(self):
        return self.a + self.b


# The __ syntax makes either a property or method private.
# this insures they can only be accessed by the class they belong to
h = Hide("John", 4, 6)
print(h.get_name())
print(h.mean())

# however they can be accessed if needed using the following syntax
print(h._Hide__name)
print(h._Hide__total())


