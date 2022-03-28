def dbl_linear(n):
    linear = [1]
    c = 0

    while len(linear) < n + n * 0.25:
        first = 2 * linear[c] + 1
        second = 3 * linear[c] + 1
        if first not in linear:
            if first > linear[-1]:
                linear.append(first)
            else:
                nc = -1
                while linear[nc] > first:
                    nc -= 1
                linear.insert(nc + 1, first)
        if second not in linear:
            if second > linear[-1]:
                linear.append(second)
            else:
                nc = -1
                while linear[nc] > first:
                    nc -= 1
                linear.insert(nc + 1, first)
        c += 1
    return linear[n]


a = dbl_linear(50)
print(a)
# a = [1, 2, 3, 4]
# a.insert(-1, 10)
# print(a, a[-1])
