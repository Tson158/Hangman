import random

with open("Wort_list.txt") as liste:
   wort = random.choice([w.strip().upper() for w in liste])

versuche, gesucht, geraten = 10, set(b for b in wort), set()

while versuche > 0:
   text = f'Noch {versuche:>2} Versuche: '
   text += " ".join([f"{b if b in geraten else '_'}" for b in wort])
   versuch = input(text + " Ihr Buchstabe? ").upper()
   geraten.add(versuch)
   if versuch not in gesucht: versuche -= 1
   if gesucht.issubset(geraten): break

text = "GEWONNEN! " if versuche > 0 else "VERLOREN! "

print(text + "Das gesuchte wort war", wort)