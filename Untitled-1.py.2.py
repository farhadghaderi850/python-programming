string = input("Enter some thing : ")
words = 0
numbers = 0
for i in string:
    if i in "123456789" :
        numbers += 1
    elif i.isalpha():
        words += 1
    else:
        print("unvalid")
print("words are: " , words , "numbers are : " , numbers)