# print() is a statement that outputs data to the screen
# something inside quotation marks is called a String
print("Hello World")

'''
This is a multi-line comment
'''

# A variable is a place to store a value
# Its name is like a label for that value

name = "So You Want To Code"

print(name)

# A variable name can hold letters, numbers, or special characters
# variable names cannot start with a number

# There are five built in data types: Numbers, Strings, List, Tuple, Dictionary
# You can store any data type in any variable

name = 15
print(name)

# There are a few arithmetic operators
# they are:   +, -, *, /, %, **, //
# ** is Exponential
# // is Floor Division

print("2 + 2 =", 2+2)
print("4 - 2 =", 4-2)
print("5 * 2 =", 5*2)
print("6 / 2 =", 6/2)
print("7 % 2 =", 7%2)
print("2 ** 2 =", 2**2)
print("9 // 2 =", 9//2)
print("5 / 2.0 =", 5/2.0)
print("5 + 3 * 2 / 6 - 4 =", 5+3*2/6-4)

#  * and / are always performed before + and -

# A string is a sequence of characters surrounded by " or '
# A multi-line quote
multi_line_quote = ''' multi-line 
quote " '''

# To embed a string in output use %s
print("%s %s" % ('This is a',  multi_line_quote))

# To keep from printing newlines use end=""
print("I don't like ",end="")

# printing a string multiple times with *
print('\n' * 5)
