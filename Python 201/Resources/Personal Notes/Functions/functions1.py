def capitalize(text):
    text_list = []
    for word in text.split():
        word = word.capitalize()
        text_list.append(word)
    return " ".join(text_list) # Making a sentence from the list with a space between each letter

text = input("Enter your text: ")
print("This is your text capitalized:")
print(capitalize(text))