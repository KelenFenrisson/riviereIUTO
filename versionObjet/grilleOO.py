# coding=utf-8
# construit une nouvelle grille hexagonale.
# Cette grille contiendra nbLig lignes, nbCol colonnes.
# si paire est à True la grille sera paire sinon elle sera impaire
# valeur sera la valeur par défaut stockée dans chaque case de la grille

class GrilleHexa(object):
    def __init__(self,nbLig,nbCol,paire=True,valeur={}):
        self.nbLig = nbLig
        self.nbCol = nbCol
        self.paire = paire
        self.grille= {}

        if type(self.nbCol) is int and type(self.nbLig) is int and type(self.paire) is bool:

            for x in range(nbLig):
                for y in range(nbCol):
                    if paire:
                        if x%2 == y%2:
                            self.grille[(x,y)]=valeur
                    else:
                        if not x%2 == y%2:
                            self.grille[(x,y)]=valeur

    # retourne le nombre de lignes de la grille
    def getNbLigGH(self):
        return self.nbLig


    # retourne le nombre de colonnes de la grille
    def getNbColGH(self):
        return self.nbCol


    # indique si la grille est paire ou impaire
    def estPaireGH(self):
        return self.paire


    # vérifie si une position est bien une position de la grille
    # par exemple si la grille est paire, lig vaut 2 et col vaut 3
    # la fonction retourne False car il n'y a pas de colonne 3 dans une ligne
    # de numéro paire d'une grille paire
    def estPosGH(self, lig, col):
        estPos = False
        if (lig, col) in self.grille:
            estPos = True
        return estPos


    # retourne la valeur qui se trouve dans la grille à la ligne lig, colonne col
    def getValGH(self, lig, col):
        if self.estPosGH(lig, col):
            return self.grille[(lig,col)]


    # met la valeur val dans la grille à la la ligne lig, colonne col
    def setValGH(self, lig, col, val):
        if self.estPosGH(lig, col):
            self.grille[(lig,col)] = val

    # retourne un couple d'entier qui indique de combien de ligne et de combien
    # de colonnes il faut se déplacer pour aller dans une direction.
    # par exemple si direction vaut 'S' le retour sera (2,0) car pour se déplacer
    # vers le sud, on ne change pas de colonne par contre on passe 2 lignes
    # Si la direction est 'NE' le resultat sera (-1,1) car pour aller dans cette direction
    # il faut remonter d'une ligne et aller une colonne vers la droite
    # Cette fonction vous sera utile pour la fonction suivante.
    def incDirectionGH(self, direction):
        d_direction = {'N': (-2, 0),
                       'S': (2, 0),
                       'NE': (-1, 1),
                       'NO': (-1, -1),
                       'SE': (1, 1),
                       'SO': (1, -1),
                       'X': (0,0)}

        return d_direction.get(direction, None)


    # permet de retourner la liste des n valeurs qui se trouvent dans la grille
    # dans une direction donnée à partir de la position lig,col
    # si il y a moins n celulles dans la grille dans la direction données on retourne
    # toutes le cellules trouvées
    def getNProchainsGH(self, lig, col, direction, n=3):
        liste_NProchains = []
        vx, vy = self.incDirectionGH(direction)

        # On regarde le prochain pas
        lig += vx
        col += vy

        for i in range(n):
            x_a_i_pas = lig + vx * i
            y_a_i_pas = col + vy * i

            if (self.estPosGH(x_a_i_pas, y_a_i_pas)):
                valeur = self.grille[(x_a_i_pas,y_a_i_pas)]
                liste_NProchains.append(valeur)

        return liste_NProchains


    # fonction d'initiation d'une grille avec des caractères pour faire des tests
    # la grille doit être créée
    def initAlphaGH(self):
        possibles = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        nbLig = self.nbLig
        nbCol = self.nbCol
        if self.estPaireGH():
            dec = 0
        else:
            dec = 1
        k = 0
        for i in range(nbLig):
            for j in range(dec, nbCol, 2):
                self.setValGH(i, j, possibles[k])
                k = (k + 1) % len(possibles)
            dec = (dec + 1) % 2


    # affichage en mode texte d'une grille hexagonale
    def afficheGH(self):
        nbLig = self.nbLig
        nbCol = self.nbCol
        if self.estPaireGH():
            print(" ", end='')
            debut = 0
        else:
            debut = 1
            print("   ", end='')
        for j in range(debut, nbCol, 2):
            print("_   ", end='')
        print()

        c1 = c2 = ' '
        for i in range(nbLig):
            if debut == 1:
                print(c1 + '_', end='')
            prem = ''
            for j in range(debut, nbCol, 2):
                print(prem + '/' + str(self.getValGH(i, j)) + '\\', end='')
                prem = '_'
            if j != nbCol - 1:
                print('_' + c2)
            else:
                print()
            c1 = '\\'
            c2 = '/'
            debut = (debut + 1) % 2
        if debut == 1:
            print('\\', end='')
            debut = 0
        else:
            print('  \\', end='')
            debut = 1
        for j in range(debut, self.nbCol - 2, 2):
            print('_/ \\', end='')
        print('_/')


# tests-------------------------------------------------
if __name__ == '__main__':

    print('TEST des fonctions de grille.py : ')
    l_grille=[GrilleHexa(10,10,True), GrilleHexa(10,10,False), GrilleHexa(9,10, True), GrilleHexa(9,10, False), GrilleHexa(10,9, True),GrilleHexa(10,9, False)]
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
    for even_grid in l_grille:
        print(even_grid)
        even_grid = GrilleHexa(10, 10, True, None)
        even_grid.initAlphaGH()
        even_grid.afficheGH()

        print('getNbLigGH() : ', even_grid.getNbLigGH())
        print('getNbColGH() : ', even_grid.getNbColGH())
        print('estPaireGH() : ', even_grid.estPaireGH())

        for x in range(even_grid.getNbLigGH()):
            for y in range(even_grid.getNbColGH()):
                print('________________________________________________________________________________ ')
                print('COORDS : ', (x, y))
                print('estPosGH() : ', even_grid.estPosGH(x, y))
                print('getValGH() : ', even_grid.getValGH(x, y))

                for dir in ['N', 'S', 'NE', 'NO', 'SE', 'SO', 'X']:
                    print('incDirectionGH() : ', even_grid.incDirectionGH(dir), 'direction : ', dir)
                    print('getNPProchains() : ', even_grid.getNProchainsGH(x, y, dir))

                print('setValGH() : ', even_grid.setValGH(x, y, "$"))
                print('POST SET getValGH() : ', even_grid.getValGH(x, y))

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
