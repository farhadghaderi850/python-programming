numbers = input("Enter a list of numbers separated by space : ")
numbers = list(map(int,numbers.split()))
posetive_numbers = [num for num in numbers if num >= 0]
print("posetive numbers are : " , posetive_numbers)