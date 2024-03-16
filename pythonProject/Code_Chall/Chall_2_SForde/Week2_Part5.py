

###
# Part 5: User input 2
# Using the following dictionary (or a similar one you found on the internet), ask the user for a word,
# and compute the Scrabble word score for that word
# (Scrabble is a word game, where players make words from letters, each letter is worth a point value),
# steal this code from the internet, format it and make it work:
###


letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}

# Prompt user to enter word
print('Please enter a word:')
word = input().lower() # convert input word to lowercase for consistency

# Calculate total score for input word:

# Iterate over each pair in letter_scores.items()
# chars represents group of characters
# score represents score associated with characters
# Iterate over each character (c) in the input word
# Check if character (c) exists in the group of characters (chars)
# If it does, add the corresponding score to the total score (cnt)
cnt = sum(score for chars, score in letter_scores.items() for c in word if c in chars)
print(f'{word} is worth {cnt} points.')

