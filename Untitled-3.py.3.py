def is_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def main():
    side1 = float(input("Enter the first side : "))
    side2 = float(input("Enter the second side : "))
    side3 = float(input("Enter the third side : "))
    if is_triangle(side1,side2,side3):
        print("triangle can be made")
    else:
        print("triangle cant be made")
main()