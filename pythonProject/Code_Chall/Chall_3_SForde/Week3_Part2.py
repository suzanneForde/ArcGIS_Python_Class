
###
# Part 2
###

import pickle
Turtle = open('IDK.dat', 'wb')
data = input('Enter data: ')

pickle.dump(data, Turtle)
Turtle.close()
print("Data recorded...")

# sys.stderr.write('Pickle')






