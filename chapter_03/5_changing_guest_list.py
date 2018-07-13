# -*- coding: utf-8 -*-
# Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.
guests = ['Harper', 'Theresa', 'Owen', 'Edwin']
person_position = guests.index('Owen')
print('Sorry but %s can\'t visit our dinner 😢' % guests[person_position])
del guests[person_position]
guests.insert(person_position, 'Eric')
for guest in guests:
    print('Dear, %s come and join us at a dinner party with cocktails, dance and music!' % guest)
