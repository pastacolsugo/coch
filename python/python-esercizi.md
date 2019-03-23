# Esempio

Creiamo un array e stampiamo i suoi elementi:

```python
saluti = ['ciao', 'buongiorno', 'buonasera', 'porcodio']

print(saluti[0])
print(saluti[1])
print(saluti[2])
print(saluti[3])
```

### Esercizio 1

Copia questo codice in un nuovo file, salvalo come `esercizio1.py`, vai nella cartella con il terminale, esegui il codice con `python esercizio1.py` e guarda il risultato.

> Se non funziona `python esercizio1.py` prova `python3 esercizio1.py`

### Il problema

Il codice va bene, fa quello che vogliamo, ma appena aggiungo un altro elemento, questo non viene stampato.

```python
saluti = ['ciao', 'buongiorno', 'buonasera', 'porcodio', 'barchetta']

print(saluti[0])
print(saluti[1])
print(saluti[2])
print(saluti[3])
```

In questo caso, ho aggiunto `barchetta` ma non ho detto al computer di stamparlo e infatti non lo fa.

### Miglioriamo

```python
saluti = ['ciao', 'buongiorno', 'buonasera', 'porcodio', 'barchetta']

for parola in saluti:
	print(parola)
```

Usiamo un nuovo tipo di `for`, lo puoi proprio leggere come "per ogni `parola` dentro `saluti` fai questo".

Ora abbiamo reso la stampa dell'array indipendente dal numero di elementi! Possiamo metterne anche 100.000 e li stampera' comunque tutti.

Copia il codice e prova ad eseguirlo, per verificare che li stampi tutti anche se aggiungi altri elementi!

# Leggere da console

Vediamo come scrivere fare in modo che il programma chieda un dato all'utente prima di eseguire il codice.

```python
valore = input("scrivi un numero: ")

print("hai inserito:" + valore)
```

Copia questo codice e vedi cosa fa.

Il risultato dovrebbe essere che il programma stampa "scrivi un numero" e sta ad aspettare. A questo punto tu puoi scrivere un numero che ti pare e quando premi invio lo mandi al programma, che continua ad eseguire.
A questo punto ti stampa il numero inserito e termina.

E' proprio la funzione `input()` che si occupa di stampare un messaggio per l'utente (in questo caso il testo "inserisci un numero") e di leggere poi il testo scritto dall'utente.

Come puoi vedere dal codice, il testo scritto dall'utente viene salvato dentro la variabile `valore` e poi stampata di nuovo a schermo.

### Esercizio

Scriviamo un programma che prenda in input un numero, gli aggiunge 1 e lo ristampa subito dopo.

```python
valore = input("scrivi un numero: ")
valore = valore + 1
print("hai inserito:" + valore)
```

#### Prova ad eseguire il codice

E' sbagliato! Dovrebbe darti un errore.

#### Qual'e' il problema?

La funzione `input()` restituisce un valore che e' di tipo `stringa` (testo)! Il numero che vogliamo sommare e' 1 e appunto e' di tipo `numero`.

Il computer ci da dei coglioni perche' non possiamo sommare un numero a una frase. Prendiamo le bastonate e risolviamo.

### Soluzione

```python
valore = input("scrivi un numero: ")

valore = int(valore) # conversione ad intero

valore = valore + 1
print("hai inserito:" + valore)
```

Nella seconda riga dico che `valore` e' uguale a `int(valore)`, ovvero _converto_ `valore` da `stringa` ad `intero` (numero senza la virgola).
Fatta la conversione, posso sommare `1` e il programma funziona.

Questa procedura si chiama **casting**: cambiare il tipo delle variabili da uno ad un altro.

Viene da se che se cerco di convertire `"ciao"` in un numero intero, Python si incazza.

### Commenti

I commenti in Python sono diversi da Javascript.

```python
# commento linea singola

'''
commento
su
tante
righe diverse
'''
```

* Uso il cancelletto `#` per il commento a linea singola
	* su Javascript era `//`
* Uso tre apostrofi `'''` per il commento su tante linee, ne metto tre all'inizio e tre alla fine
	* su Javascript era `/*` all'inizio e `*/` alla fine.
