def sum_up_diagonals(matrix):
    sum = 0
    for index, row in enumerate(matrix):
        if index == 0 or index == len(matrix)-1 :
            for index, item in enumerate(row):
                if index == 0 or index == len(row)-1 :
                    sum = sum + item
        else:
            for index, item in enumerate(row):
                if index == 1:
                    sum = sum + item + item    
    return sum
        


print('running last')



    # """Given a matrix [square list of lists], return sum of diagonals.

    # Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

    #     >>> m1 = [
    #     ...     [1,   2],
    #     ...     [30, 40],
    #     ... ]
    #     >>> sum_up_diagonals(m1)
    #     73

    #     >>> m2 = [
    #     ...    [1, 2, 3],
    #     ...    [4, 5, 6],
    #     ...    [7, 8, 9],
    #     ... ]
    #     >>> sum_up_diagonals(m2)
    #     30
    # """