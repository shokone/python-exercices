class Jugador:
    def __init__(self,nombre,puntos):
        self.nombre=nombre
        self.puntos=puntos

    def __add__(self,objeto2):
        return self.puntos+objeto2.puntos

pj1=Jugador("Carlos",21)
pj2=Jugador("Bryan",32)
print("Los jugadores han anotado el total de puntos de: ")
print(pj1+pj2)

