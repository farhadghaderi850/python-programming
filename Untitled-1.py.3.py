string = input("Enter your string : ")
result = 0
if len(string) < 2 :
    print("Emty syring")
else:
    result = string[0] + string[-1]
    print("The answer is : " , result)