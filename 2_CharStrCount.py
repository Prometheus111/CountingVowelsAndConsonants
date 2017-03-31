# 2_CharStrCount.py
# by Prometheus111
# for a given string, calculate the number of occurrences of a character in it
# that is read from the keyboard
s = 'Here is your own text!'            #we have the string s
print(s)                                #output the string s
a = input('Input the character: ')
n = 0
for i in s:                             #checking each character in a string
    if i == a:                          #if the character is in the string
        n += 1                          #count it
    else:                               #if the character isn't in the string
        pass                            #do nothing
if n >= 1:                              #if found
    print('The character "%s" occurs in the string %d times' % (a, n))
else:                                   #if not found
    print('The character "%s" in the string does not occur' %a)
# Enjoy learning new things!
# https://github.com/Prometheus111 
