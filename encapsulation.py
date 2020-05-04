# encapsulisation ensures that each class is responsible for dealing with
# its own properties. This allows the programmer to easily add validation
# within setters and return the properties only if desired in getters
class Encap:
    def __init__(self):
        self.name = None
        self.username = None
        self.password = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password


b = Encap()
b.set_name("John")
name = b.get_name()
print(name)



