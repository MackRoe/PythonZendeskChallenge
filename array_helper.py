def make_array():
    ''' Creates an array with a length of 100 and containing values
    from 1 to 100'''
    new_array = [1, 2, 3, 4, 5, 6, 7]
    highest_value = max(new_array)
    # # ** Print statement for debugging **
    # print('Highest Value: ', highest_value)
    while highest_value < 100:
        highest_value += 1
        # ** Print statement for debugging **
        # print(highest_value)
        new_array.append(highest_value)
    return new_array
