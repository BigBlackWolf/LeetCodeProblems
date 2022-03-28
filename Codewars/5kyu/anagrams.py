def anagrams(word, words):
    # My
    def count_letters(w):
        word_dict = {}
        for i in w:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1
        return word_dict
    first_word = count_letters(word)
    return [i for i in words if first_word == count_letters(i)]

    # Best
    return [item for item in words if sorted(item) == sorted(word)]



test1 = 'abba', ['aabb', 'abcd', 'bbaa', 'dada']
test2 = 'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']
data = anagrams(*test2)
print(data)