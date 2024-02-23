

###
# Part_5.py
###

scores = {
    "aeioulnrst": 1,
    "gd": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10,
}
print('Please enter a word.')
word = input()
#

cnt = sum(scores[char] for char in word)
print(f'{word} is worth {cnt} points.')




#











