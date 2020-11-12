import random
"""
Skapa en lista med tal från 5 t.o.m. 15.
Skriv en funktion som slumparett tal från listan och skicka den till en annan
funktion som multiplicerar talet med två och skriver ut resultatet.
tips: använd import random
"""

lst = range(5,16)
print(lst)

def randpick(l):
    return random.choice(l)

def mul2(i):
    print(i*2)
    
mul2(randpick(lst))