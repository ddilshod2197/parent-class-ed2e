class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class GrandChild(Child):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city

parent = Parent("John")
print(parent.name)

child = Child("Alice", 25)
print(child.name)
print(child.age)

grand_child = GrandChild("Bob", 30, "New York")
print(grand_child.name)
print(grand_child.age)
print(grand_child.city)
