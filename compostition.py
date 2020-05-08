# Below is two examples of composition, where a class instantiates another.
# ClassTwo requires ClassOne() to be passed into its constructor, where ClassThree defines ClassOne within its
# constructor method. The drawback with ClassTwo is anything could be passed, causing unwanted behaviour.


class ClassOne:
    def greet(self):
        print("Hello")


class ClassTwo:
    def __init__(self, class_one):
        self.class_one = class_one

    def exexute(self):
        self.class_one.greet()


class ClassThree:
    def __init__(self):
        self.class_one = ClassOne()

    def exexute(self):
        self.class_one.greet()


c1 = ClassTwo(ClassOne())
c1.exexute()# prints: "hello"

c2 = ClassThree()
c2.exexute()# prints: "hello"

