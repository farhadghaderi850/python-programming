"""
word = input("Enter your word pls : ")
if
"""
"""
string = input("Enter your string : ")
string2 = 0
while True:
    string2=string[0:len(string):-]
    print
"""
"""
string = input("Enter a word : ")
string2 = 0
for i in range(string):
    if i .lower():
        i .upper()
    else:
        i .lower()
    print(string)
"""
"""
string = input("Enter your word : ")
sum = 0
for ch in string:
    ch = int("1")
    sum += ch
print("sum is : " , sum)
"""
"""
String = input("Enter your string : ")
sumA = 0 
sumE = 0
sumI = 0
sumO = 0
sumU = 0
for ch in range(String):
    ch = int("1")
    if ch == "aA":
        sumA += ch
    elif ch == "eE":
        sumE += ch
    elif ch == "iI":
        sumI += ch
    elif ch == "oO":
        sumO += ch
    elif ch == "uU":
        sumU += ch
print("num of A")
"""
"""
str = input("Enter your word : ")
smaldig = 0
bigdig = 0
digit = 0
space = 0
for ch in str:
    if ch.islower():
        smaldig += ch
    elif ch.isupper():
        bigdig += ch
"""
"""
str = input("Enter your word : ")
for i in len(str/2) :
    i.index += 1 
"""
"""
pas = input("Enter your password : ")
for ch in pas:
    if ch > 8:
        break
    elif ch.isalpha():
        ch.isupper
    elif ch.isalpha():
        ch.islower
    elif ch 
"""
"""
your_list=input("Enter your number : ")
lista=[]
for i in your_list:
    your_list=lista
    lista.append[::2]
"""
"""
your_list=input("Enter your number : ")
lista=[]
print('Enter' , str(your_list) , 'elements')
for i in your_list:
    data = int(input())
    lista.append(data)
    lista.sort(data)
print[-1]
"""
"""
par = input("Enter your paragraph : ")
word = input("Enter your word : ")
lista=[]
par.split()
for i in par:
    par=lista
    lista.remove(word)
print(par)
"""
"""
#ماتریسی n*n از کاربر دریافت کرده حاصل جمع هر سطر رامحاسبه کند
i_matris = input("Enter your i : ")
j_matris = input("Enter your j : ")
sum_of_i = 0
row = []
matris = []
for n in i_matris:
    for j in j_matris:
"""
"""
#رشته با فرمتmm/dd/yyyyوخروجی march/12/2022
"""
"""
string = input("Enter your string : ")
d={}

for ch in string:
    if ch.islower():
"""
"""
list = input("Enter your list : ")
list2=[]
d = {}
list2.append(int(input()))
for num in list:
    if not num in d:
        d[num]=1
print(num)
"""
"""
name = input("What is your name : ")
age = input("How old are you ? ")
print(f"Hello {name} . ypu are {age} years old")
"""
"""
string = input("Enter your string : ")
result = ""
for i in range(len(string)):
    if i % 2 == 1:
        result = result+ string[i]
print("The answer is : " , result)
"""
"""
string = input("Enter your string : ")
print(string[1:len(string):2])
"""
"""
string = input("Enter your string : ")
reverse = ""
index = len(string)
while index > 0 :
    
    reverse += string[index - 1]
    index = index - 1
print(reverse)
"""
#string = input("Enter your string : ")
#print(string[len(string)::-1])
"""
string = 'abcefd'
print(string.replace('ab' , '12'))
"""
#word = "python programming"
#word1 = word.upper()
#word2 = word.lower()
#converted_word = ""
#for i in range(len(word)):
#    if i % 2 == 0:
#        converted_word += word2[i]
#    else:
#        converted_word += word1[i]
#print(converted_word)
"""
string = input("Enter your string : ")
result = ""
for i in range(len(string)):
    if string[i].isupper():
        result += string[i].lower()
    elif string[i].islower():
        result += string[i].upper()
    else:
        pass
print("The result is : " , result)
"""
"""
while True:
    names = input("Enter a name : ")
    salorry = int(input("Enter the salorry : "))
    c = input(" enter n to continue")
    for ch in c:
        if ch != 'n':
            break
    d = {}
    d [names] = salorry
print
"""
"""
nums = int(input("Enter your numbers : "))
while True:
    d = {}
    if len(nums) < 6:
        print("unvalid")
    else:
        nums = int(input("Enter your numbers : "))
    if nums % 2 == 0 :
        d []
"""
"""
text = input("Enter your text : ").split
d = {}
for el in text:
    if not el in d:
        d[el]=1
    else:
        d[el]+=1
for k in d:
    if d[k] == 1 :
        print(k, end=" ")
"""
"""
word = input("Enter your word : ")
d = {}
for ch in word:
    if ch in d:
        d[ch] +=1
    else:
        d[ch]=1
print(d)
"""
"""
import random
file = open("numbers.txt", "w")
for i in range(10):
    number = random.randint(1,100)
    file.write(str(number) + "\n")
file.close()
"""
"""
file = open("numbers.txt", "R")
"""
count = 0
def digit_count():
    nums = open("C:\Users\User\Desktop", "R")
    for i in nums:
        if i.isdigit():
            count += i