#opdr1
print("hello, world") 


#opdr2
tekst = "Hallo"
getal = 5
kommagetal = 3.14

print(tekst)
print(getal)
print(kommagetal)


#opdr3
naam = input("Wat is je naam? ")
leeftijd = input("Hoe oud ben je? ")

print(f"Hallo, {naam}! Je bent {leeftijd} jaar oud.")

#opdr4
getal1 = 8
getal2 = 4

print(getal1 + getal2)  # Optellen
print(getal1 - getal2)  # Aftrekken
print(getal1 * getal2)  # Vermenigvuldigen
print(getal1 / getal2)  # Delen

#opdr5
boeken = ["De Hobbit", "1984", "To Kill a Mockingbird"]

print(boeken)

boeken.append("Pride and Prejudice")

print(boeken)

#opdr6
leeftijd = int(input("Hoe oud ben je? "))

if leeftijd >= 18:
    print("Je bent oud genoeg om te stemmen.")
else:
    print("Je bent niet oud genoeg om te stemmen.")


#opdr7
for i in range(1, 11):
    print(i)

#opdr8
def hallo():
    print("Hallo, wereld!")

hallo()
