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

# new way doing things

p2 = [(n1, n2) for n1 in range(0, 11) for n2 in range(5, 33)]
print(p2)

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']


# def sort_it_out:
#     for doc in doctor:
#         doc[0]
#     return

# Create list comprehension: squares
squares = [i ** 2 for i in range(0, 10)]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)
