# Installare NodeJS

Il computer funziona con dei segnali elettrici e non puo' capire direttamente il codice che scriviamo. Ogni linguaggio ha un "traduttore" che prende il codice scritto da noi e lo traduce in linguaggio macchina, che il computer puo' capire ed eseguire.

Il "traduttore" di Javascript e' NodeJS.

Il modo piu' semplice per installare NodeJS su Windows e' andare sul [sito di NodeJS](www.nodejs.org), scaricare e seguire i passaggi dell'installer.


## Terminale

Finita la procedura di installazione, dov'e' Node?

Node e' stato installato nei programmi di sistema, ma non e' un'applicazione con un'interfaccia grafica. Per poter usare Node abbiamo bisogno del terminale.

Su Windows basta aprire il menu' e scrivere "cmd", il primo risultato dovrebbe essere "Prompt dei comandi" ed e' quello che stiamo cercando.

> Alternativa, questo fa la stessa cosa ma e' molto piu' carino: [cmder](https://cmder.net/).

Quando apri il prompt dei comandi hai una finestra nera con una scritta bianca e un cursore.

La scritta bianca e' il "prompt", ci da qualche informazione utile e ti fa sapere che sta aspettando che tu scriva un comando.

Nel terminale scriviamo i comandi e li eseguiamo dando Invio.

## Proviamo Node

Apri il terminale e scrivi `node --version`.
Se ti stampa qualcosa del tipo

```
v11.1.0
```
e non un messaggio di errore, Node e' installato correttamente.

## Comando `dir`

Quando apri il terminale, la finestra "punta" alla tua cartella home. Se vuoi eseguire un comando, viene eseguito sulla cartella home.

#### Scrivi `dir` e premi Invio.

Hai eseguito il primo comando, che stampa la cartella in cui sei e lista il suo contenuto.

## Comando `cd`

Il comando `cd` ti fa cambiare cartella.

Ad esempio se abbiamo appena aperto il terminale e il comando `dir` ci dice che abbiamo la cartella Downloads, possiamo fare `cd Downloads` e ci spostiamo nella cartella Downloads, se facciamo di nuovo `dir` il terminale stampa il contenuto della cartella Downloads.

Per tornare indietro di una cartella, quindi salire di un livello e lavorare sulla cartella che contiene quella in cui siamo ora, facciamo `cd ..`.

## Autocompletamento dei comandi

Se sto scrivendo un comando e premo il tasto Tab (quello a sinistra della Q), il terminale prova ad autocompletare quello che sto scrivendo.

Eg:

`cd Down` → Premo Tab → Se nella cartella in cui sono c'e' qualcosa che inizia con "Down", autocompleta → `cd Downloads`

### Esercizio

Prova a girare le cartelle del computer con il comando `cd` e stampare il loro contenuto con il comando `dir`. Ricorda che puoi usare `cd ..` per tornare indietro di una cartella, o solo il comando `cd` per tornare alla cartella iniziale.

## Cartella per i programmi

Con la finestrella classica di Windows, quella che hai usato per tutta la vita fino ad ora, scegli un posto che ti pare nel computer e crea una cartella (con click destro) in cui vuoi tenere i programmi che scriverai.

## Raggiungiamo questa cartella con il terminale

Apri il terminale e prova a raggiungere la cartella che hai appena creato.

# Installa Atom

Scarica e installa l'editor [Atom](atom.io).

Lo useremo per scrivere il codice.

# Primo programma

1. Apri Atom
- Scrivi questo codice di prova nel file `console.log("Ciao Luca");`
- Salva il file come `test.js`, nella tua cartella dei programmi (quella che hai fatto poco fa)
- Dal Terminale, raggiungi la tua cartella dei programmi, come hai fatto prima
- Dal Terminale esegui il comando `node test.js`
    - Se non funziona, prova a usare `nodejs test.js` 
- Dovresti vedere stampata la scritta `Ciao Luca`

