from textblob import TextBlob
from spellchecker import SpellChecker

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = SpellChecker()

    def correct_spell(self, text):
        corrected_words = []
        for word in text.split():
            if self.spell_check.correction(word) == word:
                corrected_words.append(word)
            else:
                corrected_words.append(self.spell_check.correction(word))
        return " ".join(corrected_words)

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine to appple. appple. Bananan"
    print(obj.correct_spell(message))
