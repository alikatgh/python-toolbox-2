f = [2 * num for num in range(5)]
f2 = (2 * num for num in range(5))

# print(type(f))
# print(type(f2))

res = (2 * num for num in range(5))
for i in res:
    print(i)
    print(type(i))
