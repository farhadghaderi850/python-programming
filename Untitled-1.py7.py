string = input("Enter your string : ")
repeated_ch=0
string2=0
for ch in string:
    if string.count(ch) > 1:
        repeated_ch = ch
        string2 = string.replace(repeated_ch,' ')
print("The answer is : " , string2)