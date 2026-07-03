import dictionary
import re

dizionario: list[dictionary.Parola] = []

with open("dictionary.txt", "r") as f:
    for line in f:
        l = line.strip().split(" ")
        parola = dictionary.Parola(l[0], l[1])
        if len(l) > 2:
            parola.traduzioni.extend(l[2:])
        dizionario.append(parola)

menuText = """
-------------------------
Translator Alien-Italian
-------------------------
1. Aggiungi nuova parola
2. Cerca una traduzione
3. Cerca con wildcard
4. Stampa tutto il Dizionario
5. Exit
-------------------------
"""

while True:
    print(menuText)

    input_uomo = input()
    if not input_uomo.isdigit():
        print("Inserisci un numero")
        exit(1)
    input_uomo = int(input_uomo)
    if input_uomo > 5 or input_uomo < 1:
        print("Inserisci un numero valido")

    if input_uomo == 1:

        input_parola = input("Aggiungi nuova parola e la sua traduzione: ")
        i = input_parola.lower().strip().split(" ")

        if len(i) == 2:
            p = i[0].isalpha()
            t = i[1].isalpha()
            if p == True and t == True:
                for parola in dizionario:
                    if parola.parola == i[0]:
                        parola.traduzioni.append(i[1])
                        break
                else:
                    parola = dictionary.Parola(i[0], i[1])
                    dizionario.append(parola)
        if len(i) > 2:
            p = i[0].isalpha()
            t = all(map(lambda x: x.isalpha(), i[1:]))
            if p == True and t == True:
                for parola in dizionario:
                    if parola.parola == i[0]:
                        parola.traduzioni.extend(i[1:])
                        break
                else:
                    parola = dictionary.Parola(i[0], i[1])
                    parola.traduzioni.extend(i[2:])
                    dizionario.append(parola)

    if input_uomo == 2:
        input_parola = input("Cerca traduzione: ")
        i = input_parola.lower().strip()
        if i.isalpha():
            for t in dizionario:
                if t.parola == i:
                    print(" ".join(t.traduzioni))
                    break
            else:
                print("Parola non trovata")

    if input_uomo == 3:  # Usiamo regex per semplificarci la vita, il . Indica todas le lettere
        # la funzione regex funziona anche per più di un punto ?
        input_wild = input("inserisci parola da cercare (max 1 ?): ")
        new = input_wild.replace("?", ".")
        i = new.lower().strip()
        for parola in dizionario:
            if re.match(i, parola.parola):
                print(" ".join(parola.traduzioni))

    if input_uomo == 4:
        for line in dizionario:
            print(f"{line.parola} {" ".join(line.traduzioni)}")

    if input_uomo == 5:
        with open(r"dictionary.txt", "w") as f:
            for i in dizionario:
                f.write(f"{i.parola} {" ".join(i.traduzioni)} \n")

        exit(0)
