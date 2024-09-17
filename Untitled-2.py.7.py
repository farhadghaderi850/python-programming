input = ((1,2,3),(5,5,6),(7,8,9))
output = tuple(sum(x) for x in zip(*input))
print("output is" , output )