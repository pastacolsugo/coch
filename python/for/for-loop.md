##### Coch into Computer Science

## Ripetizioni

Voglio stampare 5 volte la parola `"ciao"`.

```javascript
console.log("ciao");
console.log("ciao");
console.log("ciao");
console.log("ciao");
console.log("ciao");
```

Questo programma risolve correttamente il problema, ma non e' elegante, e se voglio cambiare il numero di volte, devo riscrivere un casino di codice.

## Ciclo `for`

Vediamo il modo corretto di farlo, e capiamo cosa succede.

```javascript
for (var i = 0; i < 5; i = i + 1) {
    console.log("ciao");
}
```

* Creo la variabile `i` con valore `0`, verra' usata per _contare quante volte ripetiamo_,
* Imposto la __condizione__ `i < 5`: finche' questa condizione e' _vera_, ripeto il codice nelle parentesi graffe.
* Specifico cosa fare alla fine di ogni ripetizione, con `i = i + 1` mi sto segnando nella variabile che ho fatto una ripetizione in piu' di quelle che avevo fatto prima.
* Sono pronto per partire: controllo la condizione `i < 5`, `i` vale `0` e `0` e' minore di `5`. La condizione e' _vera_, quindi
* eseguo il codice tra le parentesi
* ho finito di eseguire il codice, devo contare la ripetizione. Eseguo il `i = i + 1`.
* Ora `i` vale `1`.
* Controllo la condizione, `1 < 5`? _vero_
* Eseguo il codice tra le parentesi
* Aggiungo `1`
* Ora `i` vale `2`.
* Controllo la condizione, `2 < 5`? _vero_

E cosi' via, fino a che:

* Aggiungo `1`
* Ora `i` vale `5`
* Controllo la condizione, `5 < 5`? _falso_ (5 non e' minore, e' uguale).
* La condizione e' falsa quindi il `for` finisce.
* Se c'e' altro codice dopo il `for` continua ad eseguire quello.

---
Un'analogia piu' semplice puo' essere:

Devo fare 5000 passi.

* Conto con la mano, ho fatto zero passi.
* Devo fare altri passi? Zero e' minore di cinquemila, quindi si.
* Faccio un passo.
* Ho fatto un passo, me lo segno nella mano.
* Devo fare altri passi? La mano mi dice che ne ho fatto uno, uno e' minore di cinquemila, quindi si (vero).
* Faccio un passo.
* Ho fatto un passo, lo segno nella mano.
* Devo fare altri ...

* Ho segnato 4999 passi.
* Faccio un passo.
* Lo segno nella mano.
* Devo fare altri passi? La mano mi dice che ne ho fatti 5000, non devo fare altri passi (condizione `5000 < 5000` falsa).
* Smetto di ripetere.
* Faccio quello che dice il programma dopo i 5000 passi.

---

## Esercizio

Scrivi un programma che usando un `for` stampi 10 volte una frase che ti pare. Dopo averlo scritto controlla che venga scritto davvero 10 volte (non di piu', non di meno).

