def sort_big_to_min(list):
    k = 0
    while k+1 < len(list):
        if list[k] < list[k+1]:
            list[k], list[k+1] = list[k+1], list[k]
            k = 0
        else:
            k +=1
    return list
a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,88,114]
print(sort_big_to_min(a))