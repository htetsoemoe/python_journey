# Animal Parent Class
class Animal:
    def __init__(self, name):
        """Constructor to create a Animal Object"""
        self.name = name

    def speak(self):
        """Method for the animal to make a sound."""
        print(f"{self.name} makes a sound.")

#Dog Child Class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Calling the parent class (Animal) constructor
        self.breed = breed # Dog class's own attribute
    
    # Overriding the Animal speak() method
    def speak(self):
        """Dog class's own speak() method."""
        print(f"{self.name} (dog) barks.")

# Cat Child Class (inherits from Animal)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # Overriding the Animal speak() method
    def speak(self):
        """Method for the cat to meow"""
        print(f"{self.name} (cat) meows.")


my_dog = Dog("Bob", "Golden Retriever")
my_dog.speak()

my_cat = Cat("Joe", "Black")
my_cat.speak()