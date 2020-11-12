# Skriv en funktion som returnerar alla heltal i en sträng som användaren matar in! Exempel på inmatning: ”hej32a1”.Exempel på vad funktionen skareturnera:[3,2,1].

def intFinder(s):
    lst = []
    for c in s:
        try:
            if int(c):
                lst.append(c)
        except:
            continue
    return lst
            
s = input("Skriv sträng: ")
print(intFinder(s))