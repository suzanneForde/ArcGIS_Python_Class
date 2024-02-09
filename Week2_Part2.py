
###
# Part 2
###


list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

duplicates = set(list_a).intersection(list_b)

print(duplicates)

joinedlist = list(set(list_a + list_b))
print(joinedlist)