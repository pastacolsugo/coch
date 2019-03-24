# chiedo all'utente il numero di parole che vuole inserire
n = input("quante parole vuoi inserire? ")

n = int(n)

# creo parole come array vuoto
parole = []

# creo il range di numeri da 0 a n-1 (i numeri tra zero e n-1 sono esattamente n)
# per ognuno di questi numeri, chiedo all'utente di inserire una parola
for i in range(n):
	parola = input('inserisci una parola: ')
	# con la funzione append() aggiungo la parola all'array parole
	parole.append(parola)

# alla fine stampo il contenuto dell'array parole 
print(parole)