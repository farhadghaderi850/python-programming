class word_reverse:
    def __init__(self):
        self.string = ""
    def get_string(self):
        words = self.string = input("Enter a string : ")
    def reverse_words(self):
        words = self.string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words
    def revers_string(self):
        reversed_string = self.reverse_words()
        print("The result is : " ,  reversed_string)
reverser = word_reverse()
reverser.get_string()
reverser.revers_string()