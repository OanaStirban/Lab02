from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dizionario = Dictionary()

    def printMenu(self):
        print("\n-----------------------------")
        print("Translator Alien-Italian")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("-----------------------------\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary

        try:
            with open(dict, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        parola_aliena = parts[0]
                        traduzioni = parts[1:]
                        self.dizionario.addWord(parola_aliena, traduzioni)

        except FileNotFoundError:
            print(f"Attenzione: Il file '{dict}' non è stato trovato. Il dizionario partirà vuoto.")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

        if len(entry) < 2:
            print("Errore: formato non valido. Inserire <parola_aliena> <traduzione>")
            return

        parola_aliena = entry[0].lower()

        traduzioni = entry[1:]

        if not parola_aliena.isalpha():
            print("Errore: la parola aliena può contenere solo caratteri alfabetici [a-zA-Z].")
            return

        traduzioni_valide = []
        for t in traduzioni:
            t_lower = t.lower()
            if t_lower.isalpha():
                traduzioni_valide.append(t_lower)
            else:
                print(f"Attenzione: la traduzione '{t}' contiene caratteri non validi e verrà ignorata.")

        if traduzioni_valide:
            self.dizionario.addWord(parola_aliena, traduzioni_valide)
            print("Aggiunta!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>

        if not query.isalpha():
            print("Errore: la parola da cercare può contenere solo caratteri alfabetici [a-zA-Z].")
            return
        query_lower = query.lower()

        traduzioni = self.dizionario.translate(query_lower)

        if traduzioni:

            print(f"{traduzioni}")
        else:
            print("Nessuna traduzione trovata.")

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>

        query = query.lower()

        if query.count('?') != 1:
            print("Errore: devi inserire esattamente un simbolo '?' per la ricerca con wildcard.")
            return

        temp_query = query.replace('?', '')

        if not temp_query.isalpha() and len(temp_query) > 0:
            print("Errore: la parola può contenere solo lettere alfabetiche e un singolo '?'.")
            return

        risultati = self.dizionario.translateWordWildCard(query)
        if risultati:

            for parola_trovata, traduzioni in risultati.items():
                print(f"{parola_trovata}: {traduzioni}")
        else:
            print("Nessuna corrispondenza trovata.")

    def handlePrintAll(self):

        if not self.dizionario.dict:
            print("Il dizionario è vuoto.")
            return

        print("\nContenuto del Dizionario:")

        for parola, traduzioni in self.dizionario.dict.items():
            print(f"- {parola}: {traduzioni}")
