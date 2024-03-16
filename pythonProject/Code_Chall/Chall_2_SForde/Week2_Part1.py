
###
# Part 1: List values
# Using this list:
#
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# You need to do two separate things here and report both in your Python file.
# You should have two solutions in this file, one for item 1 and one for item 2.
# Item 2 is tricky so if you get stuck try your best (no penalty), for a hint check out the solution by desiato here.
#
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python (you do not need to append to a list just print the output).
###

# Define list
my_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
print(my_list)

# Create empty list to store elements less than 5
new_list = []

# Iterate over each element in the original list
for i in my_list:
    # Check if the element is less than 5
    if i < 5:  # If element is less than 5, append to new list
        new_list.append(i)
print(new_list)


# Delete elements from index 3 to 85
del my_list[3:85]
print(my_list)
