# Testat 1: Parserentwicklung mit JavaCC
View in GitHub: 
## Aufgabe 

Aufgabe Nutzen Sie den Java Compiler Compiler [JavaCC](https://javacc.github.io/javacc/) um einen Parser und eingeschrankten
Interpreter fur Brainfuck Programme zu implementieren. JavaCC ubersetzt eine Grammatikspezikation, die in einem proprietaren Format spezifiziert wurde (*.jj Dateien), in ein Java Programm, das Eingabedateien scannt und parst. Zusatzlich erlaubt es JavaCC wahrend des Parsens Befehle eingeschrankt zu interpretieren, was das gleichzeitige Parsen und Auswerten ermöglicht.

1. Der Parser soll Brainfuck Programme als Eingabeparameter einlesen und ihre Syntax verizieren. Fur syntaktisch fehlerhafte Programme
soll eine Fehlermeldung ausgegeben werden. Beispiele fur syntaktische Fehler sind unerlaubte Symbole oder unausgeglichene
Schleifenbefehle ("[" und "]"). Zusatzlich zu den Brainfuckbefehlen sind in er Eingabedatei alle Whitespace Zeichen erlaubt (`" " | "\t" | "\n" | "\r"  | "\\"` )

2. Der Interpreter soll Brainfuck Programme auswerten und alle Befehle bis auf die Schleifenbefehle "[" und "]" interpretieren. Die Schleifenbefehle sollen ignoriert werden. Die Ein- und Ausgabe von Zeichen mittels der "." und "," Befehle soll auf der Kommandozeile erfolgen. Der Interpreter soll den Zustand in einem Ringpuffer von 256 Speicherzellen speichern, die Werte im Bereich von 0 - 255 enthalten durfen.

## Anleitung zum Kompilieren

Compile um Java und Class Dateien zu erstellen

```bash
git clone https://github.com/gogamid/ATFS
cd Testat2
./compile.sh
```

Brainfuck Datei [`example_brainfuck_prog_v_1_0.bf`](./example_brainfuck_prog_v_1_0.bf) als Eingabe

```bash
java SytaxChecker example_brainfuck_prog_v_1_0.bf
```

Eingabe

```bash
F
u
l
d
a
```

Ausgabe
```bash
ShyWn
```

Um java und class Dateien zu löschen
```bash
./clean.sh
```
