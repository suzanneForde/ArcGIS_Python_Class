
###
# Part 4: User input
# Ask the user for an input of their current age,
# and tell them how many years until they reach retirement (65 years old).
#
# Hint:
#
# age = input("What is your age? ")
# print "Your age is " + str(age)
###

print('What is your age?')
age = int(input())

retire_age = 65
result = int(retire_age) - int(age)
print("You will retire " + str(result) + " years. ")


#