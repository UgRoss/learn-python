# -*- coding: utf-8 -*-
# 10. Every Function: Think of something you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, languages, or any- thing else you’d like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
languages = ['English', 'Ukrainian', 'Russian', 'Spanish', 'Hindi']
print('Languages length: %s' % len(languages))
print('Languages using sorted function: %s' % sorted(languages))
languages.sort()
print('Languages with changed order: %s' % languages)
languages.reverse()
print('Languages with reverse order : %s' % languages)
