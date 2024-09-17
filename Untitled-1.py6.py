string = input("Enter your string : ")
not_repeated_ch = 0
ch_count = 0
repeated_ch = 0
for ch in string:
    if ch.count == 1:
       not_repeated_ch +=1
    else:
        repeated_ch += 1
print("The number of repeated charactors in your string is : " , repeated_ch)