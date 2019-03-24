# chiedo all'utente il numero di valori da inserire
n = input("quanti valori vuoi inserire? ")

# converto n in un numero (operazione di casting)
# devo farlo perche' la funzione input mi restituisce una stringa (testo)
n = int(n)

# creo valori come array vuoto
valori = []

# creo il range di numeri da 0 a n-1 (i numeri tra zero e n-1 sono esattamente n)
# per ognuno di questi numeri, chiedo all'utente di inserire un valore
for i in range(n):
	valore = input('inserisci una parola: ')
	# con la funzione append() aggiungo la parola all'array valori
	valori.append(int(valore))

# creo la variabile somma, a cui andro' a sommare tutti i valori inseriti
somma = 0

# per ogni valore x contenuto nell'array valori
for x in valori:
	# dico che somma e' uguale al valore di somma piu' il valore che sto considerando ora
	somma = somma + x

# partendo da zero e sommando ogni volta un numero, alla fine li ho sommati tutti
print(somma)