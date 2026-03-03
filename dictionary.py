class Dictionary:
    def __init__(self):
        self.dict = {}

    def addWord(self, alien_word, translations):
        alien_word = alien_word.lower()

        if not isinstance(translations, list):
            translations = [translations]

        if alien_word not in self.dict:
            self.dict[alien_word] = []

        for t in translations:
            t_lower = t.lower()
            if t_lower not in self.dict[alien_word]:
                self.dict[alien_word].append(t_lower)

    def translate(self, alien_word):
        alien_word = alien_word.lower()
        return self.dict.get(alien_word, [])

    def translateWordWildCard(self, wildcard_word):
        wildcard_word = wildcard_word.lower()
        matches = {}

        for word, translations in self.dict.items():
            if len(word) == len(wildcard_word):
                match = True
                for i in range(len(word)):
                    if wildcard_word[i] != '?' and wildcard_word[i] != word[i]:
                        match = False
                        break
                if match:
                    matches[word] = translations

        return matches

    def getAll(self):

        return self.dict

