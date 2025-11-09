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
    
    def bark(self):
        """Method for the dog to bark"""
        print(f"{self.name} (dog) barks.")

# Cat Child Class (inherits from Animal)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        """Method for the cat to meow"""
        print(f"{self.name} (cat) meows.")

# Creating and testing objects
animal1 = Animal("Unknown Animal")
animal1.speak()

my_dog = Dog("Bob", "Golden Retriever")
my_dog.speak()
my_dog.bark()
print(f"My dog's breed is {my_dog.breed}")

my_cat = Cat("Joe", "Black")
my_cat.speak()
my_cat.meow()
print(f"My cat's color is {my_cat.color}")