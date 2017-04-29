class Jugador:
    def __init__(self,nombre,puntos):
        self.nombre=nombre
        self.puntos=puntos

    def __eq__(self,objeto2):
        if self.puntos==objeto2.puntos:
            return True
        else:
            return False

pj1=Jugador("Carlos",21)
pj2=Jugador("Bryan",32)
if pj1==pj2:
    print("Los jugadores han anotado los mismos puntos")
else:
    print("Los jugadores no han anotado los mismos puntos")

