# inheritance allows for code to be reused. one class can inherit the properties and methods of another.
# in the example below class B is inheriting from class A. so it can call the method m1 from its parent.


class A:
    def m1(self):
        print('Method m1() of class A')


class B(A):
    def m2(self):
        print('Method m2() of class B')


b = B()
b.m1()
