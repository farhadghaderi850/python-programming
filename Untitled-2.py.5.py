input_list = [1,3,7,[2,7],4,5,6,8,9]
outout_list = []
for num in input_list:
    if isinstance(num,list):
        outout_list.extend(num)
    else:
        outout_list.append(num)
print("output list is : " , outout_list)