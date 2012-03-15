import time
from time import strftime
print('Hey and welcome to DynamicLog! V: 1.0 (Bug free!)')
time.sleep(1)
name = input('Your full name: ') + ' '
email = '<' + input('Your email: ') + '>'
date = strftime('%Y-%m-%d ')
changes = {}
x = 0
while x != -1:
    changes[x] = '* ' + input('Change: ')
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















