# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)

jack = Person("Jack")
jill = Person("Jill")

jack.greet("Jill")
jack.greet("Mary")
jill.greet("Jack")

print(jill.name)
print(jack.greet("Jill"))
print(jack.greet("Mary"))
print(jill.greet("Jack"))
