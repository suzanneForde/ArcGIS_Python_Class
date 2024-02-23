
###
# Part 3
###

s = ('hi dee hi how are you mr dee')

x = s.split()
print(x)

for item in x:
    print(str(item) + " = " + str(x.count(item)))

hi = x.count('hi')
print(hi)

dee = x.count('dee')
print(dee)

how = x.count('how')
print(how)

are = x.count('are')
print(are)

you = x.count('you')
print(you)

mr = x.count('mr')
print(mr)



