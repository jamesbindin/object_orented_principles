# variable length arguments can be used to allow classes to take values of various sizes.
# this gives a similar behaviour to method overloading. the '*' notation is used to denote
# a parameter as a variable length argument.


class Demo:
    def __init__(self, *a):
        self.a = a

    # a tuple is returned using this method
    def print_output(self):
        print(self.a[0])

    def sum(self):
        total = 0
        for a_var in self.a:
            total = total + a_var
        return total


# varying parameter type
x = Demo('hello')
y = Demo(1)

# varying parameter length
z = Demo(2, 4)
x.print_output()# prints: hello
y.print_output()# prints: 1
print(z.sum())# prints: 6
