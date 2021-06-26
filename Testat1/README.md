# Testat 1: Regulare Ausdruecke

## Aufgabe 
Entwickeln Sie zur Unterst¨utzung der Systemumstellung ein Tool, das das Format der zu importierenden Studierendendaten auf Konsistenz mit Best-DBMS prüft.
## Sudierendendaten
Die umzuziehenden Studierendendaten finden Sie in der Datei [Studierendendaten.txt](./Studierendendaten.txt)

```bash
S1 Abschluss\t S1 FD-Nr \t S1 Name \t S1 Geb-Datum \t S1 Tel-Nr \t S1 eMail \t S1 Passwort
```

## Anleitung zum Kompilieren
Im Linux Terminal: 

```bash
git clone https://github.com/gogamid/ATFS
cd ATFS/Testat1/
sudo python tool.py
```
## Ausgabe

Das Tool soll die 98 falsch formatierten Werte auf der Kommandozeile getrennt durch Zeilenumbr¨uche ausgeben