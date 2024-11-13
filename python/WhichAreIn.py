def in_array(array1, array2):
    a=[]
    for i in array1:
        for j in array2:
            if str(i) in str(j):
                if i not in a:
                 a.append(i)


    return sorted(a)