"""
Skapa en lista med dina topp tre förebilders förnamn och en annan lista med deras efternamn.
Ordningen måste vara samma i båda listor.Båda listor ska skickas som parametrar till en funktion.
I funktionen ska en slinga användas för att lägga ihop för och efternamnet på dina förebilder.
Funktionen ska returnera en lista med de fullständiga namnen.Dennalista ska därefter skrivas ut.
"""

fname = ["Mas","Morihei","Jack"]
lname = ["Oyama","Ueshiba","Black"]

def listsmasher(l1,l2):
    lst = []
    for i in range(0,len(l1)):
        lst.append(l1[i] + " " + l2[i])
    return lst

print(listsmasher(fname,lname))