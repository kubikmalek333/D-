with open('cisla.txt', 'r') as soubor:
    cisla = [int(radek) for radek in soubor]

print(max(cisla))