def missing(s):
    length = find_length(s)
    test = [s[i: i+length] for i in range(len(s) // length)]
    a = 1


def find_length(s) -> int:
    if int(s[1]) in (int(s[0]) + 1, int(s[0]) + 2):
        return 1

    tmp = s[0]
    for i in range(1, len(s)):
        if s[i] in (tmp[0], tmp[0] + 1):
            if s[i: i + len(tmp)] in (int(tmp) + 1, int(tmp) + 1):
                return len(tmp)
        tmp += s[i]


# assert missing("123567") == 4
assert missing("899091939495") == 92
assert missing("9899101102") == 100
assert missing("599600601602") == 1
assert missing("8990919395") == 1
assert missing("998999100010011003") == 1002
assert missing("99991000110002") == 10000
assert missing("979899100101102") == 1
assert missing("900001900002900004900005900006") == 900003