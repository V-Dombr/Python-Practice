char_list = []

user_word = raw_input("Please, enter a word: ")

# Create list containing separate letters
for char in user_word:
    char_list.append(char.lower())
else:
    print char_list

# Let's count letter 's'
