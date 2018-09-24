'''PYTHON TUTORIAL:             <------ This line (Line 1) is a comment
DIFFERENT WAYS TO PRINT STRINGS <------ This line (Line 2) is a comment'''

' Andrew Garcia, 2018         <------ This line (Line 4) is also a comment'
# this one (Line 5) also a comment; can delete these lines and output will not change

#Just print the word hello
print('hello')

#print an empty space
print()

#print a long string
print('This is a very long string, but I want it to print as a single line \
so a backslash symbol like the one at the end of these coding lines \
must be used in order to do so. The backlash is useful in extending \
these lines and can be applied to other data types besides strings \
such as doubles ("numbers"), booleans, etc. ')

#a space again
print()

'Assigning a string to a variable'

#assign hello to variable H
H='hello'

#print it
print(H)

#add a string to H
print(H+'ween')

'String slices'
print(H[:-1]) 
print(H[:-2])
print(H[:-3])

#add a space after world string
print(H +' world')

#print hello in the first line, then print world in the line that follows with 
#a bunch of spaces 
print(H +'\n       world')

#just for fun
print(H[0], H[0], H[1], H[2], H[3], (H[4]+' ')*10, '.'*6)