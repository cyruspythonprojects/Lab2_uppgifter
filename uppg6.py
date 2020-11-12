import time
# Skriv en funktion som börjar räknaner från 20 sekundernär den anropas.tips: använd import time

def sleep20():
    time.sleep(20)

print("Start:",time.asctime(time.localtime(time.time())))
sleep20()
print("End:",time.asctime(time.localtime(time.time())))