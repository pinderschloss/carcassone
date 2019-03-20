from enum inport Enum, auto

class Jeu:
    def __init__(self, nb_joueurs = 2):
        self.plateau = Plateau()
        self.joueurs = []
        for i in range(0,nb_joueurs):
            self.joueurs.append(Joueur())
        self.joueurs.nb=nb_joueurs
        
class plateau:
  def __init__(self):
    self.cartes = []
  def pose(self, carte, x, y, r):
    ## Vérifie l'absence d'interférence
    for carte in cartes:
      if carte.x==x & carte.y==y:
        print("erreur il y a déjà une carte à cette position")
class carte:
    def __init__(self, nom):
        self.nom = nom
        self.nb = 0
        self.nb_posees = 0
        self.nb_reserve = 0

class direction(Enum):
    nord = 0
    est = 90
    sud = 180
    ouest = 270
    def __init__(self, angle):
        self.angle = angle
    
class interface(Enum):
    pre = auto()
    chemin = auto()
    ville = auto()
    riviere = auto()

class cote:
    def __init__(self, direction
    
    
class carte:
    def __init__(self):
        self.nord = interfaces["pré"]
        self.est = interfaces["pré"]
        self.sud = interfaces["pré"]
        self.ouest = interfaces["pré"]
        self.cotes = [self.nord, self.est, self.sud, self.ouest]
        self.image = "img001"
        self.zones = []
        self.rotation = 



class zone(Enum):
    pre = auto()
    chemin = auto()
    ville = auto()
    abbaye = auto()
    jardin = auto()
    
class carte:
    def __init__(self):
        self.cotes=[cot
        
cartes = {
    "chemin" : carte 
J=Jeu()
println(J.joueurs.nb)
J=Jeu()
println(J.joueurs.nb)
