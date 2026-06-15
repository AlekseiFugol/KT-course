# -*- coding: utf-8 -*-

import math
import os


R = 30

try:
    eingabe = input(f"Anzahl Bierdeckel R (Bezeichnungsraum) [Standard {R}]: ").strip()
    if eingabe != "":
        R = int(eingabe)
except ValueError:
    R = 30


ausgabe = []

ausgabe.append("")
ausgabe.append(f"Bierdeckel-Telegraf: R = {R} Deckel")
ausgabe.append("B = Brauereien / Basis")
ausgabe.append("n = R / B")
ausgabe.append("V = B^n")
ausgabe.append("G = log2(V)")
ausgabe.append("=" * 60)

moegliche_B = [1, 2, 3, 5, 6, 10, 15, 30]

bestes_B = 1
bestes_n = R
bestes_V = 1
bestes_G = 0.0

ausgabe.append(f"{'B':>4} | {'n=R/B':>6} | {'V = B^n':>12} | {'G [bit]':>10}")
ausgabe.append("-" * 45)

for B in moegliche_B:
    n = R // B
    V = B ** n
    G = math.log2(V)

    ausgabe.append(f"{B:>4} | {n:>6} | {V:>12} | {G:>10.2f}")

    if G > bestes_G:
        bestes_B = B
        bestes_n = n
        bestes_V = V
        bestes_G = G

ausgabe.append("=" * 60)
ausgabe.append("Maximum:")
ausgabe.append(f"Optimale Wahl B = {bestes_B}")
ausgabe.append(f"n = {bestes_n}")
ausgabe.append(f"V_max = {bestes_V}")
ausgabe.append(f"G_max = {bestes_G:.2f} bit")
ausgabe.append("")
ausgabe.append(f"Bei R = {R} ist also B = {bestes_B} die beste Wahl.")

text = "\n".join(ausgabe)

print(text)

script_dir = os.path.dirname(os.path.abspath(__file__))
submissions_dir = os.path.join(script_dir, "submissions")
os.makedirs(submissions_dir, exist_ok=True)

log_path = os.path.join(submissions_dir, "console_log.txt")

with open(log_path, "w", encoding="utf-8") as file:
    file.write(text)

input("\nDruecke Enter zum Beenden...")
