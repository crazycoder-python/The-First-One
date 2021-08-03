
age = input('please choose to do something:\n1.learning python\n2.playing minecraft\n3.playing cricket\n4.slaping jessie\n5.watchin youtube\n0.quit')
running = True
while running:
    if age == '1':
        print('you learned some python!!')
        pop = input('Do you want to do something else')
        if pop.casefold() == 'Yes'.casefold():
            continue
        else:
            print('your lazy!! :(')
            running = False
    elif age == '2':
        print('you found dimonds!!!')
        pop = input('Do you want to do something else')
        if pop.casefold() == 'Yes'.casefold():
            continue
        else:
            print('your lazy!! :(')
            running = False
    elif age == '3':
        print('you hit a six !!!')
        pop = input('Do you want to do something else')
        if pop == 'Yes'.casefold():
            continue
        else:
            print('your lazy!! :(')
            running = False
    elif age == '4':
        print('you felt gooooood!!!')
        pop = input('Do you want to do something else')
        if pop.casefold() == 'Yes'.casefold():
            continue
        else:
            print('your lazy!! :(')
            running = False
    elif age == '5':
        print('your favourite youtuber is goin live!!!')
        pop = input('Do you want to do something else')
        if pop.casefold() == 'Yes'.casefold():
            continue
        else:
            print('your lazy!! :(')
            running = False
    elif age == '0':
        print('you quit!!!')
        running = False
    else:
        print('error error invalid input')
        running = False