# abstract classes are classes that cant be directly instantiated, they need to be inherited by another class
# abc is imported and abc.ABCMeta is extended to make the class abstract the decorator @abc.abstractmethod is used
# to make a method abstract the abstract method needs to be overrided to be used in a child class.
import abc


class AbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def abstract_method(cls):
        print("Hello")


class Child(AbstractClass):
    def method1(cls):
        print("Child")

    def abstract_method(cls):
        print("Implemented abstarct Method")

class Child(AbstractClass):
    def method1(cls):
        print("Child")

    def abstract_method(cls):
        print("Implemented abstarct Method")

c = Child()
c.method1()# prints: "Hello"
c.abstract_method()# prints: "Implemented abstarct Method"