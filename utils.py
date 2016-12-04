def remove_values_from_list(the_list, val):
    ''' remove ocurrences of value from a list and return the list '''
    return [value for value in the_list if value != val]

def list_of_tuples_2_array_of_arrays(the_list):
    # same as np.array(the_list).squeeze
    return [list(item) for item in the_list]


