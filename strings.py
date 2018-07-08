# -*- coding: utf-8 -*-

# 1  Store a person’s name in a variable, and print a message
# to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
print('1. ========================================================')
name = 'Ross'
print('Hello ' + name + ', would you like to learn some Python today?')

# 2. Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase
print('2. ========================================================')
person = 'RoSs'
print('Lowercase: ' + person.lower())
print('Uppercase: ' + person.upper())
print('Titlecase: ' + person.title())

# 3. Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
#   Albert Einstein once said, “A person who never made a
#   mistake never tried anything new.”
print('3. ========================================================')
print('\tSteve Jobs once said, ""Your time is limited, \n\tso don\'t waste it living someone else\'s life.""')

# 4. Repeat Exercise 3, but this time store the famous person’s
# name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message
print('4. ========================================================')
famous_person = 'Steve Jobs'
message = '\t' + famous_person + \
    ' once said, ""Your time is limited, \n\tso don\'t waste it living someone else\'s life.""'
print(message)

# 5. Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
print('5. ========================================================')
name = ' Ross '
print(name.strip().replace(' ', '[whitespace]'))
print(name.lstrip().replace(' ', '[whitespace]'))
print(name.rstrip().replace(' ', '[whitespace]'))
