# -*- coding: utf-8 -*-
# More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement
# to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
guests = ['Harper', 'Theresa', 'Owen', 'Edwin']
print('Hello, dear friends! Party becomes bigger! 🎉 \nNew invites:')
guests.insert(0, 'Kira')
guests.insert(len(guests) / 2, 'Bob')
guests.append('Victoria')
for guest in guests:
    print('Dear, %s come and join us at a dinner party with cocktails, dance and music!' % guest)
