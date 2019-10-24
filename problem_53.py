# A TRADUIRE ?

# La première pile (la pile a) reçoit les éléments qu’on ajoute à la file. Lorsqu’on veut supprimer un
# élément de la file, celui-ci est extrait de la pile b à moins que celle-ci ne soit vide, auquel cas les éléments de la
# pile a sont tout d’abord transférés dans la pile 

class File:
    """ Définition d'une file à l'aide de deux piles """
    def __init__(self):
        self.a = Pile()
        self.b = Pile()
    def isempty(self):
        return self.a.isempty() and self.b.isempty()
    def add(self, x):
        self.a.push(x)
    def take(self):
        if self.isempty():
            raise ValueError("file vide")
        if self.b.isempty():
            while not self.a.isempty():
                self.b.push(self.a.pop())
        return self.b.pop()
