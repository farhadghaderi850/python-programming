list = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7]
newlist = [num for num in list if num != 0] + [num for num in list if num == 0 ]
print("The result is : " , newlist)