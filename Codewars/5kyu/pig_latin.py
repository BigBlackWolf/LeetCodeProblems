from string import ascii_letters


def pig_it(text):
    words = text.split(' ')
    for i in range(len(words)):
        delim = ""
        if words[i][-1] not in ascii_letters:
            delim = words[i][-1]
            words[i] = words[i][:-1]
        if words[i]:
            words[i] = words[i][1:] + words[i][0] + "ay"
        words[i] += delim
    return " ".join(words)


test = "Pig latin is cool"
test2 = "Hello world !"
data = pig_it(test2)
print(data)
