def intersection(list0, list1):
    new_list = [x for x in list0 if x in list1 ]
    return new_list

print intersection([1, 2, 3], [2, 3, 4])

def union(list0, list1):
    inter = intersection(list0, list1)
    new_list0 = [ x for x in list0 if x not in inter ]
    new_list = new_list0 + list1
    return new_list

print union([1, 2, 3, 2], [2, 3, 4])

def setdiff(list0, list1):
    new_list = [x for x in list0 if x not in list1 ]
    return new_list

print setdiff([1, 2, 3], [2, 3, 4])

def symdiff(list0, list1):
    un = union(list0, list1)
    inter = intersection(list0, list1)
    new_list = [ x for x in un if x not in inter ]
    return new_list

print symdiff([1, 2, 3], [3, 4])

def cartproduct(list0, list1):
    new_list = [ [x, y] for x in list0 for y in list1 ]
    return new_list

print cartproduct(["x", "y", "z"], [1, 2, 3])