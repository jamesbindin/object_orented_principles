# Properties can belong to the instance of a class or the class its self. below the company_name belongs to the class,
# where name, salary and age belong to the instance. Similarly class methods can only access class variables like
# company_name. Static methods can not access anything belonging to the class or instance so are used as utility methods


class Employee:
    company_name = "Facebook"
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def method(self):
        print(self.name)

    @classmethod
    def company_info(cls):
        print("The Company name is", cls.company_name)

    @staticmethod
    def general_utility_method(x, y):
        return x * y

# method() is a normal method, it can only be called when a instance is made.
e = Employee("Rohn", 30000, 26)
e.method()

# class methods can access class variables but not instance variables
Employee.company_info()
e.company_info()

# Static methods can be called using ether the instantiated object or the class.
# They cant access class properties
print(e.general_utility_method(2, 3))
print(Employee.general_utility_method(5, 6))
