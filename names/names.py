import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
# time complexity of O(n^2)
'''
duplicates = []

# instantiate BST
bst = BinarySearchTree('name')

#add all names from names_1 to a binary search tree
for name in names_1:
    bst.insert(name)

#check each name in names_2 to see if it exists in the tree
for name in names_2:
    #if it does, append it to the dulicates array
    if bst.contains(name):
        duplicates.append(name)

# O(n) time complexity


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?


# duplicates = set(names1).intersection(names_2)
# 64 duplicates 
# runtime: 0.0040435791015625 seconds