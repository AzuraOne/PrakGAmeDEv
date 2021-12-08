def comma(num):
    '''Add comma to every 3rd digit. Takes int or float and
    returns string.'''
    if type(num) == int:
        return '{:,}'.format(num)
    elif type(num) == float:
        return '{:,.2f}'.format(num) # Rounds to 2 decimal places
    else:
        print("Need int or float as input to function comma()!")


comma(20000000000000000)