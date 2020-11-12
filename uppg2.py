# Skriv en funktion som vänder på strängen en användare matar in.Exempel på inmatning: ”hej”.Exempel på vad funktionen skareturnera ”jeh”.
def reverser(s): return s[::-1]
s = input("Skriv in sträng som du vill vända: ")
print("Den vända strängen: ",reverser(s))