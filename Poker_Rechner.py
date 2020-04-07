# Pot Odds

import time


# Überschrift

print(" ")
print("=" * 40)
print("=            POT ODDS Rechner          =")
print("=" * 40)
print(" ")


# Schleife

def calculate():

    return play_again()

def play_again():
    while True:


# Abfrage des Tisches
    
        pot = input("Potgröße: ")   # Potgröße ohne dem Call aber mit dem Raise

        callsize = float(input("Callsize: "))

        outs = float(input("Outs: "))

        tor = input("Noch 2 oder 1 Karte: ")


# Grundberechnung Odds

        finalpot = float(pot) + (float(callsize) * 2 )

        odds = float(callsize) / finalpot * 100


        print(" ")
        print("Pot Odds: " + str(odds) + " %")


# Grundberechnung Outs
    
        if tor == "2":
            outs = outs * 4 

        else:
            outs = outs * 2
            
        print("  Equity: " + str(outs) + " %")
        print(" ")


# Vergleich Von Odds and Equity(Outs) --> Call: Equity % > Pot Odds in %; Fold: Equity % < Pot Odds %

        if outs > odds:
            print("Call")
            print(" ")
            
        else:
            print("Fold")
            print(" ")


# 3 Sekunden warten

        time.sleep(3)
            
        print("=" * 40)
        print(" ")



calculate()

