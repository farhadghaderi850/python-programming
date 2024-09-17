A = [1,5,8,4,9,16]
B = [11,12,16,14,1,7,5]
unique_elements = [element for element in A + B if (element not in A) or (element not in B)]
print("unique elements are : " , unique_elements)