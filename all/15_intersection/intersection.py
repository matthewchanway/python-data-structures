def intersection(l1, l2):
    lnew = []
    for item2 in l2:
        for item1 in l1:
            if item1 == item2:
                lnew.append(item1)
    return lnew

    
print(intersection([1, 2, 3], [2, 3, 4]))
        # [2, 3]
        
print(intersection([1, 2, 3], [1, 2, 3, 4]))
        # [1, 2, 3]
        
print(intersection([1, 2, 3], [3, 4]))
        # [3]
        
print(intersection([1, 2, 3], [4, 5, 6]))
        # []
    