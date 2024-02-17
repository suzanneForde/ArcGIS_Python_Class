
###
# Part 2
###

# I copied the .bat file from step 2 into my week3_part2 file because I was very confused on how to make one.
# I combed through stackoverflow and Youtube but I couldn't figure it out.

import sys

def function_one(name1):
    print("Hello, my name is", name1)
function_one (name1 = "Suzie")

def main(arg):
    print("My argument: " + str(arg))
main(sys.argv[1])

# # The following code produces a countdown that I found from the following Youtube video
# # https://www.youtube.com/watch?v=-Wl6ZwlICSE
# # I was using it to think through the assignment

import time
countdown = 5
while countdown > 0:
    print('Countdown = ', countdown)
    countdown = countdown - 1
    time.sleep(1)


