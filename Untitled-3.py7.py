def chech_string_len(input_str):
    lenth = len(input_str)
    if lenth % 2 == 0:
        print(input_str[:lenth//2])
    else:
        print(input_str[lenth//2:])
user_input = input("Enter a string : ")
chech_string_len(user_input)