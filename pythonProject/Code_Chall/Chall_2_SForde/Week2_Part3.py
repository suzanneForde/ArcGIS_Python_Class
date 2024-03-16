
###
# Part 3: Given a singe phrase, count the occurrence of each word
# Using this string:
#
# string = 'hi dee hi how are you mr dee'
# Count the occurrence of each word, and print the word plus the count
# (hint, you might want to "split" this into a list by a white space: " ").
###

# Define string
s = ('hi dee hi how are you mr dee')

# Split string into a list of words
x = s.split()
print(x)

# Iterate over each word in the list
for item in x:
    # Print each word along with its count in the list
    print(str(item) + " = " + str(x.count(item)))




