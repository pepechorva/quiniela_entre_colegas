import random
from random import shuffle
listaJugadores = ["jugador1", "jugador2", "jugador3", "jugador4", "jugador5"]

listaCasillas = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","primer resultat pleno","segon resultat pleno","doble","doble","doble","doble"]

shuffle(listaJugadores)

for i in range(20):
	shuffle(listaCasillas)

count = 0
while (len(listaCasillas) != 0):
	print(listaJugadores[count] + ' ' + listaCasillas[0])
	listaCasillas.pop(0)
	count = count +1
	if(count > len(listaJugadores)-1):
		count = 0
