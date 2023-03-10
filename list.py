# list comprehension

nums = [1, 2, 3, 4, 5, 6]
newn = []

for num in nums:
    newn.append(round(num + 1.11))
# print(newn)


newn = [round(num + 1.11) for num in nums]

# print(newn)

p1 = []
for num1 in range(0, int(99.12)):
    for num2 in range(0, int(99.493845)):
        p1.append((round(num1), round(num2)))
# print(p1)

# new way doing things

p2 = [(n1, n2) for n1 in range(0, 11) for n2 in range(5, 33)]
# print(p2)

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
# for row in matrix:
# print(row)

cond = [round(num ** 0.33, 2) if num % 1 == 0 else 0 for num in range(20)]
print(cond)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)
