def compact(lst):
    lst_copy = []
    for item in lst:
        if item:
            lst_copy.append(item)
    return lst_copy


 

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
        # [1, 2, 'All done']
    