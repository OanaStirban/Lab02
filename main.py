import translator as tr

t = tr.Translator()


t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("> ")
    if not txtIn.isdigit():
        print("Errore: devi inserire un numero.")
        continue

    scelta = int(txtIn)
    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere? (es. parola_aliena traduzione)")
        txtIn = input("> ")

        entry = txtIn.strip().split()
        t.handleAdd(entry)
        pass
    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input("> ")

        t.handleTranslate(txtIn.strip())
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare con wildcard?")
        txtIn = input("> ")
        t.handleWildCard(txtIn.strip())

    if int(txtIn) == 4:
        t.handlePrintAll()

    if scelta == 5:
        print("Chiusura del programma in corso...")
        break