# -*- coding: utf-8 -*-

import math

R = 30

print("Bierdeckel-Telegraf")
print("R =", R)
print("Gesucht wird die optimale Basis B")
print()

# Nur diese Werte teilen R = 30
werte_B = [1, 2, 3, 5, 6, 10, 15, 30]

beste_basis = None
beste_stellen = None
groesster_signalvorrat = 0
groesster_informationsgehalt = 0

print(f"{'B':>4} | {'n = R/B':>8} | {'V = B^n':>12} | {'G = log2(V)':>14}")
print("-" * 50)

for B in werte_B:
    n = R // B
    V = B ** n
    G = math.log2(V)

    print(f"{B:>4} | {n:>8} | {V:>12} | {G:>14.2f}")

    if G > groesster_informationsgehalt:
        beste_basis = B
        beste_stellen = n
        groesster_signalvorrat = V
        groesster_informationsgehalt = G

print()
print("Maximum:")
print("Optimale Wahl B =", beste_basis)
print("n =", beste_stellen)
print("V_max =", groesster_signalvorrat)
print("G_max =", round(groesster_informationsgehalt, 2), "bit")
