import time
from time import strftime
print('Hey and welcome to DynamicLog! V: 1.0 (Bug free!)')
time.sleep(1)
# If you don't want to have to enter your name and email each time just...
# change the variables to look like "name = '(your name)'"
name = input('Your full name: ') + ' '
email = '<' + input('Your email: ') + '>'
date = strftime('%Y-%m-%d ')
changes = {}
x = 0
while x != -1:
    changes[x] = '+ ' + input('New features: ')
    if changes[x] == '+ ':
        del changes[x]
        break
    x += 1
while x != -1:
    changes[x] = '- ' + input('Removed features: ')
    if changes[x] == '- ':
        del changes[x]
        break
    x += 1
while x != -1:
    changes[x] = '* ' + input('Bugs: ')
    if changes[x] == '* ':
        del changes[x]
        break
    x += 1
print('Formatting into changelog...')
time.sleep(.5)
print('\n' * 100)
print(date + name + email)
for i in changes:
    print('')
    print('    ' + changes[i])















