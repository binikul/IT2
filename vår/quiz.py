poeng = 0

print("Velkommen til Quiz")

print("Hva er hovedstaden i Danmark")
print("Svaralternativer: A: Oslo, B: København, C: Amsterdam")
svar = input("ditt svar: ")
if svar == "B" or svar == "b":
    print ("Riktig!")
    poeng += 1


    print ("Nå har du", poeng, "poeng")
else:
    print ("Feil svar")
    print ("Nå har du", poeng, "poeng")