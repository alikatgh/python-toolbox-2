f = [2 * num for num in range(5)]
f2 = (2 * num for num in range(5))

# print(type(f))
# print(type(f2))

res = (2 * num for num in range(5))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

res2 = (2 * num for num in range(5))
for i in res2:
    print((i))
    # print(type(i))

# print(next(res))
