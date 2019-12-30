import string


class Solution:
    letters = string.ascii_letters
    def findAndReplacePattern(self, words, pattern):
        bi_pattern = self.patternate(0, pattern)[1]
        bi_words = list(map(lambda x: self.patternate(*x), enumerate(words)))
        bi_result = list(filter(lambda x: x[1] == bi_pattern, bi_words))
        result = [words[word[0]] for word in bi_result]
        return result

    def patternate(self, index: int, word: str):
        for number, char in enumerate(word):
            if char in self.letters:
                word = word.replace(char, str(number))
        return index, word