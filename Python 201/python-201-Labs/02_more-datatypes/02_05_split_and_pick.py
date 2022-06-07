# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input("Enter your sentence: ")
user_list = user_input.split()
common_word = []
word_count1 = 0
word_count2 = 0

for i in user_list:
    for j in user_list:
        if i == j:
            word_count2 += 1
    if word_count2 > word_count1:
        common_word = []
        common_word.append(i)
        word_count1 = word_count2
    elif word_count2 == word_count1:
        common_word.append(i)
        word_count1 = word_count2
        
    word_count2 = 0

common_word = set(common_word)

if word_count1 <= 1:
    print("There are no repeating words in the sentence")
elif len(common_word) > 1:
    print(f"The most common words in the sentence are: ")
    [print(x) for x in common_word]
    print(f"They appear {word_count1} times each")
else:
    print(f"The most common word in the sentence is: ") 
    [print(x) for x in common_word]
    print(f"And it appears {word_count1} times")