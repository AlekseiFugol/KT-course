# Fragebogen: Huffman-Codierung (huffman.py)

Nach dem Ausführen des Skripts und **Einfügen der Konsolenausgabe** (Merge-Symbol in der Task-Card):

---

**1. Konsolenausgabe**

Enter the string to compute Huffman Code Tree: ---------------------------------------------------------
Dictionary of Characters with char frequency:       {'B': 1, 'C': 6, 'A': 5, 'D': 3}
Dictionary converted into a list:                   dict_items([('B', 1), ('C', 6), ('A', 5), ('D', 3)])
List of characters sorted to descending frequency:  [('C', 6), ('A', 5), ('D', 3), ('B', 1)]
Huffman Code Dictionary:                            {'C': '0', 'B': '100', 'D': '101', 'A': '11'}

 Char | Huffman code 
----------------------
 'C'  |           0
 'A'  |          11
 'D'  |         101
 'B'  |         100

---

**2. Deine Kommentierung**

- Was zeigen die ausgegebenen Huffman-Codes?  
  Die Ausgabe zeigt, welches Zeichen welchen Bit-Code bekommt. Also zum Beispiel, dass A, B, C oder D jeweils durch eine bestimmte Folge aus 0 und 1 ersetzt werden.

- Warum haben häufigere Zeichen kürzere Codewörter?  
  Häufige Zeichen kommen im Text öfter vor, deshalb lohnt es sich, sie mit weniger Bits zu speichern. Seltene Zeichen können dafür längere Codes bekommen, weil sie nicht so oft benutzt werden. So wird der ganze Text insgesamt kürzer.