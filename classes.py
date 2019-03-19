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
        self.
J=Jeu()
println(J.joueurs.nb)
J=Jeu()
println(J.joueurs.nb)
