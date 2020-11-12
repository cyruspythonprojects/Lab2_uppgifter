import random
"""
Skapa ett sten-sax-påse spel. 
Användaren ska mata in antingen sten, sax eller påse.
Inmatningen ska skickas till en funktion som sedan jämför inmatningen med ett slumpat värde som antingen är sten, sax eller påse.
Extra: Först till 3 vinner. Håll reda på poängen och meddela vem vinnaren är!
"""

def comp_choice():
    c_choice = random.randint(1,3)
    if c_choice == 1:
        return "sten"
    elif c_choice == 2:
        return "sax"
    elif c_choice == 3:
        return "påse"
    
def fight(u,c):
    print("Du valde:",u)
    print("Datorn valde: ",c)
    
    if u == c:
        return("Lika")
    elif u == "sten" and c == "sax":
        return("Du vinner")
    elif u == "sax" and c == "påse":
        return("Du vinner")
    elif u == "påse" and c == "sten":
        return("Du vinner")
    else:
        return("Datorn vinner")
        
stats_user = 0
stats_comp = 0

while True:
    user_choice = input("sten, sax eller påse: ")
    c_choice = comp_choice()
    
    resultat = fight(user_choice,c_choice) 
    
    if resultat == "Du vinner":
        print("Du vann!")
        stats_user += 1
    elif resultat == "Lika":
        print("Lika!")
    else:
        print("Datorn vann!")
        stats_comp += 1

    print("DU:",stats_user,"DATORN:",stats_comp)
    if stats_user == 3 or stats_comp == 3:
        if stats_user == 3:
            print("DU VANN ÖVER DATORN!")
        else:
            print("DATORN KNÄCKTE DIG!")
        break
