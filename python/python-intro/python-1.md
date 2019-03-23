# Python!

Python e' molto simile a JavaScript, e' sempre un linguaggio di scripting e va molto meglio per  il lavoro sul terminale/prompt dei comandi.

La maggior parte della sintassi che hai visto fino ad ora e' la stessa, ma non tutto!

## Variabili

In _Javascript_:

```javascript
var topolino = "si fa le topoline";
var pippo = 'si fa le pippe';
```

In _Python_:

```python
topolino = "si fa le topoline"
pippo = 'si fa le pippe'
```

Differenze principali:

* In Javascript uso `var`, in Python scrivo la variabile e lui capisce che la voglio creare. 
* In Javascript uso `;`, in Python no.

## `console.log()`

In Javascript:

```javascript
console.log('dio sventrato');
```

In Python:

```python
print('dio sventrato')
```

## `if`

Qui incontriamo la prima differenza, guarda questo codice.

Javascript:

```javascript
if (altezza < 160) {
	console.log('Non puoi salire sulle montagne russe');
}
```

Python:

```python
if (altezza < 160):
	print('Non puoi salire sulle montagne russe')
```

Qual'e'?

In Javascript usiamo le parentesi graffe `{}`, in Python usiamo i due punti `:` e il codice che vogliamo *dentro* l'`if` **deve** essere spostato verso destra di 1 tab. Vediamo un esempio.

> NOTA sul __tab__:
> tab e' il tasto con la freccia a fianco della Q.
> In python si indenta con un tab lungo 4 spazi.
> Un'altra differenza importante e' il carattere che usi per indentare: puoi fare in modo che l'indentazione sia fatta con il carattere `tab` o con 4 `spazi`. Nei programmi non possiamo mescolare il tipo di indentazione, quindi per convenzione usiamo **sempre** 4 spazi.
> Se vai nelle impostazioni di Atom, nel pannello Editor in basso trovi "Tab Length" (mettilo a 4) e "Tab Type" (mettilo soft).

Esempio in Javascript, il codice dentro l'`if` non e' indentato (= non e' spostato a destra).

```javascript
if (altezza < 160) {
console.log('Non puoi salire sulle montagne russe');
}
```
Il codice funziona perfettamente, lo possiamo eseguire come l'esempio precedente. E' solo piu' difficile da leggere.

Esempio in Python, il codice dopo l'`if` non e' indentato:

```python
if (altezza < 160):
print('non puoi salire sulle montagne russe')
```
Il codice in python **non** funziona! Il "traduttore" si aspetta di trovare del codice dentro l'`if`, ma siccome la linea con il `print` non e' spostata a destra, per come si scrive il Python, non e' dentro l'if e il "traduttore" si incazza.


