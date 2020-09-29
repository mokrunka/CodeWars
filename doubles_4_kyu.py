import time
start_time = time.time()
def doubles(maxk, maxn):
    n = 0
    k = 0
    v = pow(10,-9)
    while k < maxk:
        k += 1
        if k < 7:
            while n < maxn:
                n += 1
                v += (1 / (k * pow((n + 1),(2 * k))))
            n = 0
        else:
            v += 0
    # print(v)
    return v

# def doubles(maxk, maxn):
#     n = 0
#     k = 0
#     v = 0
#     while k < maxk:
#         k += 1
#         while n < maxn:
#             n += 1
#             v += (1 / (k * (n + 1) ** (2 * k)))
#         n = 0
#     # print(v)
#     return v

# def doubles(maxk, maxn):
#     n = 0
#     k = 0
#     v = 0
#     while k < maxk:
#         k += 1
#         while n < maxn:
#             n += 1
#             v += (1 / (k * pow((n + 1),(2 * k))))
#         n = 0
#     # print(v)
#     return v

# def doubles(maxk, maxn):
#     error = pow(10,-8)
#     n = 0
#     k = 0
#     v = pow(10,-7)
#     while k < maxk:
#         k += 1
#         while n < maxn:
#             n += 1
#             if v < error:
#                 v += 0
#             else:
#                 v += (1 / (k * pow((n + 1),(2 * k))))
#                 # print(v)
#         n = 0
#     # print(v)
#     return v

# doubles(1, 3)
# doubles(1, 10)
# doubles(10, 100)
# doubles(10, 1000)
doubles(20, 100000) #19.156490802764893 s, 18.453163862228394 s, 19.09548258781433 s, 20.041353702545166 s

run_time = time.time() - start_time
print(f'run time is {run_time} s')
print(time.time())