import time


class Catapult:
    def fire(self):
        pass

    def reload(self):
        pass


class IntergalacticCatapult(Catapult):
    def __init__(self):
        print('You have a new inter galactic catapult. ')
        self.light_year_range = 100
        self.secs_to_reload = 2

    def fire(self):
        print('Firing now! Range: ' + str(self.light_year_range))
        print('Reloading time in seconds: ' + str(self.secs_to_reload))

    def reload(self):
        print('Reloading...')
        time.sleep(self.secs_to_reload)
        print('Reload complete. Ready to fire.')


cata = IntergalacticCatapult()
cata.fire()
cata.reload()
print('\nPython does not have interfaces, so I used an abstract class to do this, but it is not perfect. \n'
      'Python used an ABC module to incorporate interface functionality, I should check that out.')
print('\nPython has multiple inheritance, subclasses can have more than one base class.')