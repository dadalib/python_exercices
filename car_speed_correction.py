class Voiture:
    def __init__(self, vitesse_change):
        self.__vitesse_change = vitesse_change

    def change_vitesse_haut(self, delta_v=None):
        if delta_v is None:
            self.__vitesse_change += 1
        else:
            self.__vitesse_change += delta_v

    def change_vitesse_bas(self):
        self.__vitesse_change -= 1

    def afficher_vitesse(self):
        print(f"Vitesse actuelle: {self.__vitesse_change}")

if __name__ == "__main__":
    v = Voiture(0)
    v.change_vitesse_haut()  # Increments by 1
    v.afficher_vitesse()
    v.change_vitesse_haut(5) # Increments by 5
    v.afficher_vitesse()
    v.change_vitesse_bas()   # Decrements by 1
    v.afficher_vitesse()
