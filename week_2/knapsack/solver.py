#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_dp(items, capacity):
    def build_tab(items, capacity):
        tab = [[0]*(capacity+1) for x in range(0, (len(items)+1))]
        
        for item in items:
            i = item.index + 1
            # fill the column i
            for j in range(0, capacity+1):
                if item.weight > j :
                    tab[i][j] = tab[i-1][j]
                else:
                    tab[i][j] = max( tab[i-1][j], item.value + tab[i-1][j - item.weight] )
        return tab

    def backtrace(tab, items):
        taken = [0]*len(items)

        i = len(items)
        j = capacity

        while i > 0 and j > 0:
            if tab[i][j] != tab[i-1][j]:
                taken[i-1] = 1
                j -=  items[i-1].weight
            i -= 1

        value = tab[-1][-1]
        return value, taken
    
    value, taken = backtrace(build_tab(items, capacity), items)
    
    return 1, value, taken

def solve_greedy(items, capacity):
    value = 0
    weight = 0
    taken = [0]*len(items)
    
    items = sorted(items, key=lambda x: x.value/x.weight, reverse=True)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return 0, value, taken

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    if item_count * capacity <= 1000*100000:
        perfect, value, final_result = solve_dp(items, capacity)
    else:
        perfect, value, final_result = solve_greedy(items, capacity)
        
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(perfect) + '\n'
    output_data += ' '.join(map(str, final_result))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

