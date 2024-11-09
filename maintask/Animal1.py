# .Create a class Animal with attributes species and sound.Add a method make_sound that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.
class animal1():
    def __init__(self, species, sound):
        # attributes
        self.species= species
        self.sound=sound
    def make_sound(self):
        return f'The {self.species} goes {self.sound}'
Cow = animal1('Cow', 'Moo')
print (Cow.make_sound())
Cat = animal1("Cat","meow")
print(Cat.make_sound())
Cock = animal1('Cock', 'crow')
print (Cock.make_sound())
Dog = animal1('Dog', 'Bark')
print(Dog.make_sound())

    
        