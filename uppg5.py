"""
Skriv en funktion som väljer den högsta siffran i en talföljd som användaren matar in.
Denna siffra är temperaturen i Kelvin. Ni ska nu beräkna vad temperaturen blir i Celsius genom att använda siffran i funktionen ni skrev i uppgift 3.
Exempel: Inmatning: ”4219”.Den första funktionen skavälja siffran 9.Den andra funktionen ska räkna fram talet -264.
"""

def maxinmat():
    maxtal = 0
    tal = input("Skriv in en talföljd, separera talen med blanksteg: ")
    
    for c in tal:
        if int(c) > maxtal:
            maxtal = int(c)
    
    return maxtal

def KtoC(k):
    return k-273

print(KtoC(maxinmat()))