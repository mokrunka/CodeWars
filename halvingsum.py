# def halving_sum(n): # this works but too slowly
#     result = n
#     i = 2
#
#     while n // i != 1:
#         result += n // i
#         i *= 2
#
#     return (result + 1)

def halving_sum(n):
    i = 2
    if n // i == 1:
        return 1
    else:
        i *=2
        return halving_sum((n // i) + n)

halving_sum(25)
halving_sum(127)

# 127 + 63 + 31 + 127 / 8 + 127/16