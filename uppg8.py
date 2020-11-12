"""
1.Skapa en miniräknare. Den ska ha fyra funktioner: Addition, subtraktion, multiplikation och division. 
Funktionerna ska kunna behandla två parametrar som man skickar in utifrån.Bonus: Skapa en mainfunktionsom frågar användaren om två siffror. 
Efter att man skrivit in dem ska den fråga vilken matematisk operation man vill göra med dem, addition, subtraktion etc.
Därefter ska den valda funktionen anropas automatiskt och returnera det rätta svaret.
"""

def ask():
    tal1 = float(input("Skriv in det första talet: "))
    tal2 = float(input("Skriv in det andra talet: "))
    return tal1,tal2
    
def addition(a,b):
    return a+b

def subtraktion(a,b):
    return a-b

def multiplikation(a,b):
    return a*b

def division(a,b):
    return a/b

def main():
    print("Välkommen till miniräknar programmet!")
    tal1,tal2 = ask()
    choice = input("Vilken operation vill du utföra (addition,subtraktion,multiplikation eller division):")
    print("Tal1:",tal1)
    print("Tal2:",tal2)
    
    
    if choice == "addition":
        print("Svar:",addition(tal1,tal2))
    elif choice == "subtraktion":
        print("Svar:",subtraktion(tal1,tal2))
    elif choice == "multiplikation":
        print("Svar:",multiplikation(tal1,tal2))
    elif choice == "division":
        print("Svar:",division(tal1,tal2))
    
    
if __name__ == "__main__":
    main()
