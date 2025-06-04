# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        sorted_original = sorted(self.word)

        for w in word_list:
            if sorted(w) == sorted_original:
                matches.append(w)

        return matches
