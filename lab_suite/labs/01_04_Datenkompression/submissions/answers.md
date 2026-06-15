# Fragebogen: Wort-Entropie (word_dictionary.py)

Nach dem Ausführen von `word_dictionary.py` mit eigenem Text in `sampletext.txt`:

**Konsolenausgabe einfügen:** Nutze das Merge-Symbol in der Task-Card, um die Ausgabe aus `console_log.txt` hier einzufügen. Anschließend die Ausgabe **kommentieren**.

---

**1. Konsolenausgabe**

Analyze the file:  C:\Fugol\KT-course\lab_suite\labs\01_04_Datenkompression\submissions\sidedata/sampletext.txt
Total number of words:     23
Number of different words: 22

-------Table of words:-----------------------------------------
                            die | cnt=  2    p=0.087   H=3.524 bit/word   H_av=0.306 bit/word
                           Dies | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                            ist | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                            ein | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                         kurzer | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                   Beispieltext | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                           fuer | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                Entropieanalyse | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                            Der | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                           Text | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                       enthaelt | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                   verschiedene | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                     Buchstaben | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                    Leerzeichen | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                            und | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                    Satzzeichen | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                            Die | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                     Verteilung | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                            der | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                        Zeichen | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                    beeinflusst | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
                       Entropie | cnt=  1    p=0.043   H=4.524 bit/word   H_av=0.197 bit/word
-----------------------------------------------------------------

Average Entropy H = 4.437 bit/word
Total Entropy of 23 words H=102.042 bit (13 bytes)
Size of text file: 185 bytes

---

**2. Deine Kommentierung**
* Wie unterscheidet sich die Wort-Entropie von der Zeichen-Entropie (entropy1.py)?
  Bei der Wort-Entropie werden ganze Wörter gezählt und nicht einzelne Zeichen. Deshalb gibt es hier nur 23 Wörter, aber bei der Zeichen-Entropie viel mehr Zeichen. Die Entropie pro Wort ist höher, weil ein Wort mehr Information enthält als ein einzelnes Zeichen. Insgesamt ist der Wert aber kleiner, weil es viel weniger Wörter als Zeichen gibt.

* Was sagt die Entropie in Byte im Vergleich zur tatsächlichen Dateigröße aus?
  Die Entropie ergibt hier 13 Bytes, die Datei ist aber 185 Bytes groß. Das zeigt, dass die Entropie nur ein theoretischer Wert ist. Die echte Datei braucht mehr Speicher, weil auch Leerzeichen, Zeilenumbrüche, Satzzeichen und die normale Textspeicherung dazugehören.

