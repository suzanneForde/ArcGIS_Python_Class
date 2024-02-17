
###
# Part 2
###

import sys

print("This is the name of the program:", sys.argv[0])

print("Argument List:", str(sys.argv))

print("Argument 1 = " + str(sys.argv[1]))
print("Argument 2 = " + str(sys.argv[1]))
print("Argument 3 = " + str(sys.argv[1]))

def main(arg):
    print("My argument" + str(arg))
main(sys.argv[1])