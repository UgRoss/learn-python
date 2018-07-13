# -*- coding: utf-8 -*-
# Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.
names = ['John', 'Frenk', 'Frederick']
message = 'Hello, %s! How are you?'
print(message % names[0])
print(message % names[1])
print(message % names[2])
