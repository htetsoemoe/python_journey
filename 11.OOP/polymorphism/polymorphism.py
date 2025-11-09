# Animal Parent Class
class Animal:
    def __init__(self, name: str):
        """Constructor to create a Animal Object"""
        self.name = name

    def speak(self):
        """Method for the animal to make a sound."""
        print(f"{self.name} makes a sound.")

#Dog Child Class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name) # Calling the parent class (Animal) constructor
        self.breed = breed # Dog class's own attribute
    
    # Overriding the Animal speak() method
    def speak(self):
        """Dog class's own speak() method."""
        print(f"{self.name} (dog) barks.")

# Cat Child Class (inherits from Animal)
class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    # Overriding the Animal speak() method
    def speak(self):
        """Method for the cat to meow"""
        print(f"{self.name} (cat) meows.")


def make_animal_speak(animal: Animal):
    """A function that calls the speak() method for any animal object"""
    animal.speak()

my_animal = Animal("Unknown Animal")
my_dog = Dog("Bob", "Golden Retriever")
my_cat = Cat("Alice", "Black")

make_animal_speak(my_animal)
make_animal_speak(my_dog)
make_animal_speak(my_cat)