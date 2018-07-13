# -*- coding: utf-8 -*-
# Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
name = ' Ross '
print(name.strip().replace(' ', '[whitespace]'))
print(name.lstrip().replace(' ', '[whitespace]'))
print(name.rstrip().replace(' ', '[whitespace]'))
