word_list = input("Enter a list of words separated by spaces : ").split()
longest_word = 0
max_len = 0
for word in word_list:
    if len(word) > max_len:
        max_len = len(word)
        longest_word = word
print("The longest word is : " , longest_word , "and the number of its charactors are : " , max_len)