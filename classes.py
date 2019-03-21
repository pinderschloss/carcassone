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
    def __init__(self, direction, interface)
        self.direction = direction
        self.interface = interface

class cotes:
    def __init__(self, nord, est, sud, ouest)
        self.nord = nord
        self.est = est
        self.sud = sud
        self.ouest = ouest
        self.dictdir = { "nord": nord, "est":est, "sud": sud, "ouest": ouest }
        self.listdir = [ nord, est, sud, ouest ]
 

class carte(Enum):
    chemin = 
    def __init__(self, nom,
                 nord = interface.pre,
                 est = interface.pre,
                 sud = interface.pre,
                 ouest = interface.pre,
                 image = "base",
                 ):
        self.cotes = cotes(nord, est, sud, ouest)
        self.image = "img001"
        self.zones = []
        self.nom = nom
        self.nb = 0
        self.nb_posees = 0
        self.nb_reserve = 0
        self.positions = []
        # Liste des rotations pertinentes pour la carte.
        # La première rotation (nord = angle nul) doit être vraie.
        # Par défaut les autres sont déterminées en fonction des symétries des bordures
        # A modifier à la main pour tenir compte de la réalité des zones
        if (nord == sud ) & (est == ouest):
            if (nord == est):
                self.rotations = [ direction.nord ] 
            else:
                self.rotations = [ direction.nord, direction.est ]
         else:
                self.rotations = [ direction.nord, direction.est, direction.sud, direction.ouest ] 
    
    def pose(self, x, y, rotation = direction.nord):
        # La rotation n'est pas comparée à la liste des rotations pertinentes
        # Doit être appelé
        if self.nb_reserve>1:
            self.nb_reserve -= 1
            self.nb_posees1 += 1
            self.positions.append((x,y,rotation))
            return 0
        else:
            print("Il n'y a plus de carte à poser")
            return 100
    def     



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
