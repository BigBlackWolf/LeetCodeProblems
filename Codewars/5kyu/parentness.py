def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


test1 = ")(()))"
test2 = "("
test3 = "()"
test4 = "(())((()())())" # True
data = valid_parentheses("")
print(data)