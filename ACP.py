class Reverse:
    def __init__(self, text):
        self.text = text 

    def get_reversed(self):
        return " ".join(self.text.split()[::-1])

user_input = input("Enter a word: ")

rev = Reverse(user_input)

print("Reversed String:", rev.get_reversed())