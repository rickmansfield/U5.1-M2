"""
Below, you'll find a class definition for animals. Create two new animals `cat`
and `dog`. Set `cat` to have a name of "Purrfect", kind of "cat",
and color of "brown". Set `dog` to have a name of "Fido",
kind of "dog", and color of "black".
"""
class Animal:
    def __init__(self, name="", kind="", color=""):
      self.name = name
      self.color = color
      self.kind = kind

    def description(self):
        # return "%s is a %s %s." % (self.name, self.color, self.kind)
        return f"{self.name} is a {self.color} {self.kind}"
"""
instantiate an instance of the Animal class labeled cat
instantiate an instance of the Animal class labeled dog

set the name of cat to equal "Purrfect"
set the kind of cat to "cat"
set the color of cat to "brown"

set the name of dog to equal "Fido"
set the kind of dog to "dog"
set the color of dog to "black"

"""
# Create instances of Animal here and modify the instance attributes
# as described above.

# YOUR CODE HERE
cat = Animal("Purrfect", "cat", "Brown")
dog = Animal()

# cat.name = "Purrfect"
# cat.kind = "cat"
# cat.color = "brown"

dog.name = "Fido"
dog.kind = "dog"
dog.color = "black"

# print(help([].sort))


# Should print Purrfect is a brown cat.
print(cat.description())
# Should print Fido is a black dog.
print(dog.description())