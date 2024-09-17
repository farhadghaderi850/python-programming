def odd_or_even(number):    
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
def if_odd_or_even(number,result):
    if result == "even":
        return (number * 2)
    else:
        return (number ** 3)
user_number = int(input("Enter a number : "))
result = odd_or_even(user_number)
result = if_odd_or_even(user_number,result)
print(result)