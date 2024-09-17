def check_abc(input_string):
    positions = {}
    for index, char in enumerate(input_string):
        if char in ['a', 'b', 'c']:
            if char not in positions:
                positions[char] = [index]
        else:
                positions[char].append(index)
                return positions
def main():
    user_input = input("Enter a string : ")
    result = check_abc(int(user_input))
    for char, indices in result.items():
        print(f"characters '{char}' found at indices : {indices} ")
main()