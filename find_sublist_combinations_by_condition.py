#!/usr/bin/env python

"""
pick all matched combinations by  certain criteria from a list

"""

import itertools

def find_combinations_by_criteria(orig_list,number_of_ele = 0,condition = None):
    """ find all the sublist combinations of  a list that matchs the specified condition function.
    """

    result_list = []
    if orig_list is None:
        raise "orignal list cannot be None or empty!"
        
    # by default find the maxium elements
    if number_of_ele == 0:
        seq_length = len(orig_list)
    # reset to default value(maxium elements)
    elif number_of_ele > len(orig_list):
        seq_length = len(orig_list) 

    else:
        seq_length = number_of_ele

    # enumerate all the combinations 
    for i in range(1,seq_length + 1):
        iter_combination = itertools.combinations(orig_list,i)
        result_list.extend(list(filter(condition,iter_combination)))

    return result_list
    
# utility functions
###################
def inverse_dict(d):
    """ swap key and value in a given dict return a new dict with value:key
        eg: d = {'a' = 1,
                 'b' = 2,
                 'c' = 3
                }
        after reverse we will have a new dict iva_d
        iva_d = {1: 'a', 2: 'b', 3: 'c'}
    """
    if d and isinstance(d,dict):
        ivs_d = {v:k for k,v in d.items()}
        return ivs_d
    else:
        raise 'Error when reverse given dictionary'

def values_to_keys(vlist,ivs_d):
    """ find the keys combinations from the corresponding values
        eg:d = {'a' = 1,
                 'b' = 2,
                 'c' = 3
                }
        dl = list(itertools.combinations(a.values(),2))
        [(3, 2), (3, 1), (2, 1)]

        after this function we will get a list of corresponding keys combinations
        value combinations : [(3,    2),  (3,    1),  (2,   1)]
                               ^     ^     ^     ^      ^   ^
        keys combinations:   [('c', 'b'), ('c', 'a'), ('b','a')]
        :param ivs_d: a reversed dict based on the values in vlist
    """
    #TODO: to be refactored to be more explicit
    return list(map(lambda y: tuple(map(lambda x:ivs_d[str(x)],y)),vlist))

def main():

    # test data
    prod_number_list_raw = """
N1
N2
N3
N4
N5
N6
N7
N8
N9
N10
N11
N12
N13
N14"""

    points_list_raw = """
514
220
91
96
111
97
98
104
106
117
177
138
85
62"""

    # generate product seq list as keys remomve empty values
    # by filter(None, list)
    prod_seq = list(filter(None,prod_number_list_raw.split('\n')))
    print(prod_seq)

    points_list = list(filter(None,points_list_raw.split('\n')))
    print(points_list)
    
    # generate a dict key: point value: product number
    points_product_dict=dict(map(reversed,zip(prod_seq,points_list)))
    
    product_points_dict = inverse_dict(points_product_dict)
    product_points_dict_values = list(map(int,product_points_dict.values()))
    
    print('BEGIN'.center(80,'*'))
        # find all the combinations that sum of all values  equals 852
    result_values = find_combinations_by_criteria(product_points_dict_values,0,condition=lambda x:852 - sum(x) == 0)
    results = values_to_keys(result_values,points_product_dict)
    
    for i in results:
        print(i)
    
    print('END'.center(80,'*'))
    
if __name__ == '__main__':
    main()
