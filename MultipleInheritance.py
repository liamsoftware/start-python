class Cat:
    def purr(self):
        print('puuuurrrrr')


class Dog:
    def bark(self):
        print('woof, woof')


class ComboAnimal(Cat, Dog):
    def make_sound(self):
        print('meow woof')


combo = ComboAnimal()
combo.purr()
combo.bark()
combo.make_sound()