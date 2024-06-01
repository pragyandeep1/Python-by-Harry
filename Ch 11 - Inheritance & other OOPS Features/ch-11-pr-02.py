'''Create a class 'Pets' from class 'Animals' and
 further create another class 'Dog' from Pets.
 Add a method 'bark' to the class Dog.'''

class Animal:
    type = 'mammal'

class Pets(Animal):
    color = 'white'

class Dog(Pets):
    @staticmethod
    def bark():
        print('bow wow')

d = Dog()
d.bark()