
###
# Part 2
###

# I copied the .bat file from step 2 into my week3_part2 file because I was very confused on how to make one.
# I combed through stackoverflow and Youtube but I couldn't figure it out.
# I have no idea what I did here.

import sys


print("Argument 1 = " + str(sys.argv[1]))
print("Argument 2 = " + str(sys.argv[2]))
print("Argument 3 = " + str(sys.argv[3]))



def function_one(spanish):
    print("Hola,", spanish)
function_one (spanish = "como estas.")
def function2(name1):
    print("Me llamo", name1)
function2 (name1 = "Suzie.")


# # # The following code produces a countdown that I found from the following Youtube video
# # # https://www.youtube.com/watch?v=-Wl6ZwlICSE
# # # I was using it to think through the assignment

import time
countdown = 5
while countdown > 0:
    print('Countdown = ', countdown)
    countdown = countdown - 1
    time.sleep(1)


