#1
class StringFoo:
    def __init__(self):
        self.attribut = None

    def set_string(self, parametre):
        self.attribut = parametre

    def print_string(self):
        print(self.attribut.upper())

stringfoo = StringFoo()
stringfoo.set_string('salut')
stringfoo.print_string()

#2

class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
    def calcul_aire(self):
        return self.longueur*self.largeur

    def afficher_infos(self):
        print('longueur: ', self.longueur)
        print('largeur: ', self.largeur)
        print('Aire: ', self.calcul_aire())

rectangle = Rectangle(10, 16)
rectangle.afficher_infos()
rectangle2 = Rectangle(4,7)
rectangle2.afficher_infos()
