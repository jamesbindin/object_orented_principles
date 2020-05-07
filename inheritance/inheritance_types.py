# single inheritance
class Parent:
    def method_1(self):
        print("parent method")


class Child(Parent):
    def child_method(self):
        print("child class method")


c = Child()
c.method_1()# prints: "parent method"
c.child_method()# prints: "child class method"
print('________________________________')
#-----------------------------------------------------------------------------------------------------------------------

# multiple inheritance
class ParentOne:
    def method_1(self):
        print("parent_One")


class ParentTwo:
    def method_2(self):
        print("parent_Two")


class Child(ParentOne, ParentTwo):
    def child_method(self):
        print("child class method")


c = Child()
c.method_1()# prints "parent_Two"
c.child_method()# prints "child class method"
print('________________________________')
#-----------------------------------------------------------------------------------------------------------------------


# hirachical inheritance
class Parent:
    def parent_method(self):
        print("parent method")


class ChildOne(Parent):
    def child_one_method(self):
        print("child one class method")


class ChildTwo(Parent):
    def child_two_method(self):
        print("child two class method")

c1 = ChildOne()
c1.parent_method()# prints: "parent method"
c1.child_one_method()# prints: "child one class method"

c2 = ChildTwo()
c2.parent_method()# prints: "parent method"
c2.child_two_method()# prints: "child two class method"
print('________________________________')
#-----------------------------------------------------------------------------------------------------------------------


# hierarchical inheritance
class ParentOne:
    def parent_one_method(self):
        print("parent_One")


class ParentTwo:
    def parent_two_method(self):
        print("parent_Two")


class Multiple(ParentOne, ParentTwo):
    def multiple_method(self):
        print("Multiple class method")


class HierarchicalOne(Multiple):
    def hierarchical_one_method(self):
        print("HierarchicalOne class method")


class HierarchicalTwo(Multiple):
    def hierarchical_two_method(self):
        print("HierarchicalTwo class method")

h1 = HierarchicalOne()
h1.parent_one_method()#prints: "parent_One"
h1.parent_two_method()#prints: "parent_Two"
h1.multiple_method()#prints: "Multiple class method"
h1.hierarchical_one_method()#prints: "HierarchicalOne class method"
h2 = HierarchicalTwo()
# similar for h2
print('________________________________')
#-----------------------------------------------------------------------------------------------------------------------


# multi level inheritance

class Parent:
    def method1(self):
        print("Parent")


class Child(Parent):
    def method2(self):
        print("Child")


class GrandChild(Child):
    def method3(self):
        print("GrandChild")


gc = GrandChild()
gc.method1()# prints: "Parent"
gc.method2()# prints: "Child"
gc.method3()# prints: "GrandChild"
print('________________________________')
#-----------------------------------------------------------------------------------------------------------------------


# overriding methods
class Parent:
    def method1(self):
        print("Parent")


class Child(Parent):
    def method1(self):
        print("new output")


c = Child()
c.method1()#prints: "new output"
