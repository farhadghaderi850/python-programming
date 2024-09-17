def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5) + 1):
        if number % i ==0:
            return False
        return True
def main():
    number_input = int(input("Enter a number : "))
    if is_prime(number_input):print("the number is prime")
    else:print("the number is not prime")
main()