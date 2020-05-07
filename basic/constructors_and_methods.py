# The example below is a basis class in python. the constructor is defined using the method name '__init__'.
# the 'self' syntax denotes the instance of the class. It is a requisite for each method

class Person:
    def __init__(self, name, age, wake_up_time):
        self.name = name
        self.age = age
        self.wake_up_time = wake_up_time

    def behaviour(self):
        print("Hello, My name is:", self.name, "and i wake up at:", self.wake_up_time)

# objects can be instantiated using the classes constructor, allowing different properties
p1 = Person("Tom", 23, 6)
p2 = Person("John", 24, 8)

p1.behaviour()#prints: Hello, My name is: Tom and i wake up at: 6
p2.behaviour()#prints:  Hello, My name is: John and i wake up at: 8

