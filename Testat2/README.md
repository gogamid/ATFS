# Testat 2: Parserentwicklung mit JavaCC

View in GitHub: https://github.com/gogamid/ATFS/blob/main/Testat2/README.md

## Aufgabe 

Aufgabe Nutzen Sie den Java Compiler Compiler [JavaCC](https://javacc.github.io/javacc/) um einen Parser und eingeschraenkten
Interpreter fuer Brainfuck Programme zu implementieren. JavaCC ueubersetzt eine Grammatikspezikation, die in einem proprietaeren Format spezifiziert wurde (*.jj Dateien), in ein Java Programm, das Eingabedateien scannt und parst. Zusaetzlich erlaubt es JavaCC waehrend des Parsens Befehle eingeschraenkt zu interpretieren, was das gleichzeitige Parsen und Auswerten ermoeglicht.

1. Der Parser soll Brainfuck Programme als Eingabeparameter einlesen und ihre Syntax verifizieren. Fuer syntaktisch fehlerhafte Programme
soll eine Fehlermeldung ausgegeben werden. Beispiele fuer syntaktische Fehler sind unerlaubte Symbole oder unausgeglichene
Schleifenbefehle ("[" und "]"). Zusaetzlich zu den Brainfuckbefehlen sind in er Eingabedatei alle Whitespace Zeichen erlaubt (`" " | "\t" | "\n" | "\r"  | "\\"` )

2. Der Interpreter soll Brainfuck Programme auswerten und alle Befehle bis auf die Schleifenbefehle `"["` und` "]"` interpretieren. Die Schleifenbefehle sollen ignoriert werden. Die Ein- und Ausgabe von Zeichen mittels der "." und "," Befehle soll auf der Kommandozeile erfolgen. Der Interpreter soll den Zustand in einem Ringpuffer von 256 Speicherzellen speichern, die Werte im Bereich von 0 - 255 enthalten duerfen.

## Anleitung zum Kompilieren

Compile um Java und Class Dateien zu erstellen

```bash
git clone https://github.com/gogamid/ATFS
cd ATFS/Testat2
./compile.sh
```

Brainfuck Datei [`example_brainfuck_prog_v_1_0.bf`](./example_brainfuck_prog_v_1_0.bf) als Eingabe

```bash
java SyntaxChecker example_brainfuck_prog_v_1_0.bf
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
