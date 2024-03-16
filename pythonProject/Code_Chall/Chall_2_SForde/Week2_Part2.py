
###
# Part 2: List Overlap
# Using these lists:
#
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.
###

# Define two lists
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

# Find the intersection of the two lists to identify duplicates
duplicates = set(list_a).intersection(list_b)


print("Items present in both lists:", list(duplicates))

# Find the symmetric difference between the two lists to identify non-overlapping items
non_overlapping_items = set(list_a).symmetric_difference(list_b)
print("Items that do no overlap in the lists:", list(non_overlapping_items))
