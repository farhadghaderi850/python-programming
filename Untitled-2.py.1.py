numbers = (input("Enter your list of numbers separated by spaces : "))
numbers = list(map(int,numbers.split()))
even_numbers = [num for num in numbers 
if num % 2 == 0]
odd_numbers = [num for num in numbers
if num % 2 != 0]
print("ODD" ,odd_numbers  , "even" , even_numbers)