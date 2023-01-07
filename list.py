# list comprehension

nums = [1, 2, 3, 4, 5, 6]
newn = []

for num in nums:
    newn.append(round(num + 1.11))
print(newn)


newn = [round(num + 1.11) for num in nums]

print(newn)

p1 = []
for num1 in range(0, int(99.12)):
    for num2 in range(0, int(99.493845)):
        p1.append((round(num1), round(num2)))
print(p1)
