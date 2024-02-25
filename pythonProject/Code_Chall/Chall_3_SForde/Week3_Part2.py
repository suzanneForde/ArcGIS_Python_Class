
###
# Part 2
###

# I combed through stackoverflow and Youtube but I couldn't figure it out.
# I have no idea what I did here.

import sys

# file = open("testfile.bat", "w") # This did not work so I copied and pasted the .bat file from in-class example

print("Argument 1 = " + str(sys.argv[1]))
print("Argument 2 = " + str(sys.argv[2]))
print("Argument 3 = " + str(sys.argv[3]))


def function_one(spanish):
    print("Hola,", spanish)
function_one (spanish = str(sys.argv[1]))
def function2(name1):
    print("Me llamo", name1)
function2 (name1 = str(sys.argv[2]))


# # # The following code produces a countdown that I found from the following Youtube video
# # # https://www.youtube.com/watch?v=-Wl6ZwlICSE
# # # I was using it to think through the assignment

import time
countdown = 5
while countdown > 0:
    print('Countdown = ', countdown)
    countdown = countdown - 1
    time.sleep(1)


