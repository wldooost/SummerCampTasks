import re

#tpl = '^\d+$'
tpl = '[a-zA-Zа-я]+\s\S'
x = None
elements =[]


while x != 'end':
    t = 0
    print('Ну?>>', end="")
    x = input()
    if x != 'end':
        if re.fullmatch(tpl, x) is not None:
            print('Full match')
            x = None
        else:
            elements.append(x)

print(elements)

