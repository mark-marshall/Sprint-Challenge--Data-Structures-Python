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

# First pass solution using Python in-built "in" function (from C so much faster)
# Runtime = 1.0 seconds
# duplicates = []
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# Second pass Solution using binary search tree data structure
#  Runtime = 0.1 seconds
# duplicates = []
# Initialise the search tree with letter m to give a better chance of an even tree
# comparison_tree = BinarySearchTree('m')
# insert each name from names_2 into the binary search tree
# for name_2 in names_2:
#     comparison_tree.insert(name_2)
# loop over names_1 and use the contains method on comparison_tree to check for duplicates
# for name_1 in names_1:
#     if comparison_tree.contains(name_1):
#         duplicates.append(name_1)

# STRETCH solution merging lists and sorting
# Runtime = 0.03 seconds
def get_duplicates(list):
        duplicates = []
        sorted_list = sorted(list)
        for i in range(0, len(sorted_list) - 1):
                if sorted_list[i] == sorted_list[i+1]:
                        duplicates.append(sorted_list[i])
        return duplicates

def remove_duplicates(list, duplicates):
        deduplicated_list = []
        for name in list:
                if name not in duplicates:
                       deduplicated_list.append(name) 
        return deduplicated_list

names_1_dupe = get_duplicates(names_1)
name_1_deduped = remove_duplicates(names_1, names_1_dupe)

names_2_dupe = get_duplicates(names_2)
name_2_deduped = remove_duplicates(names_2, names_2_dupe)

duplicates = []
merged_names = sorted(name_1_deduped + name_2_deduped)
for i in range(0, len(merged_names) - 1):
        if merged_names[i] == merged_names[i+1] and merged_names[i]:
                duplicates.append(merged_names[i+1])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")