'''
A "McGugan beggining game development with python and pygame" book project '''

class Tank(object):

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 10
        self.armor = 100

    def __str__(self):

        if self.alive:
            return f'{self.name} ({self.armor} armor, {self.ammo} shells)'
        else:
            return f'{self.name} is DEAD'

    def fire_at(self, enemy):

        if self.ammo >= 1:
            self.ammo -= 1
            print (self.name + ' fires on ' + enemy.name)
            enemy.hit()
        else:
            print (self.name + ' has no shells!')

    def hit(self):

        self.armor -= 20
        print (self.name + ' is hit!')
        if self.armor <= 0:
            self.explode()

    def explode(self):

        self.alive = False
        print (self.name + ' explodes!')
        

