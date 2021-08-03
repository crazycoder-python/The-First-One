name = input('Hello Welcome To PFC(Pardha\'s Fried Chicken)\nPls Enter Your Name:')

intro = input('Hello {0} Pls Choose From The Menu:\nMenu:\n Pardha Chicken\n Party fries\n juicy soda\n Pardha\'s'
 'Lunch Meal'.format(name))

if intro == 'Pardha\'s Chicken':
    print('thank you {0} and have a nice day!!'.format(name))
    poop = input('do you want to give a tip?')
    if poop == 'no':
        print('you are a poopy face')
    else:
        print('you are very kind')
elif intro == 'Party fries':
    print('Enjoy those awesome fries {0}'.format(name))
    poop = input('do you want to give a tip?')
    if poop == 'no':
        print('You are not genourous')
    else:
        print('you are very genororus')
elif intro == 'Pardha\'s Chicken and' and ' Party fries':
    print('You Will Like it!!')
    poop = input('do you want to give a tip?')
    if poop == 'no':
        print('you are a poopy face')
    else:
        print('you are very kind')
elif intro == 'Pardha Chicken and' and ' Party fries and' and ' juicy soda':
    print('thank you {0} and you have a good one'.format(name))
    poop = input('do you want to give a tip?')
    if poop == 'no':
        print('you are a poopy face')
    else:
        print('you are very kind')
else:
    print('it better fill your tummy!!:)')
print('Come Back Again {0}'.format(name))