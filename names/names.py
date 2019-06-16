import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Provided solution
# Runtime = 4.6 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Solution using binary search tree data structure
#  Runtime = 0.1 seconds
duplicates = []
# Initialise the search tree with letter m to give a better chance of an even tree
comparison_tree = BinarySearchTree('m')
# insert each name from names_2 into the binary search tree
for name_2 in names_2:
    comparison_tree.insert(name_2)
# loop over names_1 and use the contains method on comparison_tree to check for duplicates
for name_1 in names_1:
    if comparison_tree.contains(name_1):
        duplicates.append(name_1)

# STRETCH solution using Python in-built "in" function (from C so much faster)
# Runtime = 1.0 seconds
# duplicates = []
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")