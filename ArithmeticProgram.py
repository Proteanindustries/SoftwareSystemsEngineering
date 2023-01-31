# input request loop
while True:
    indvar1 = input('Enter 1st Value: ')
    indvar2 = input('Enter 2nd Value: ')
    select = input('Select + or -: ')
    depvar = 0
# add operation
    if select == '+':
        depvar = float(indvar1) + float(indvar2)
# subtract operation
    elif select == '-':
        depvar = float(indvar1) - float(indvar2)
    print('Value of {0} and {1} is {2}'.format(indvar1, indvar2, depvar))
# repeat or end process
    if input('New calculation? (y/n)') == 'n':
        print('Goodbye')
        break
