import string


sentence = "This is my default user sentence. It is short, and to the point."
my_dict ={"lowercase": 0, "uppercase": 0, "punctuation": 0, "characters": 0}
my_dict["characters"] = len(sentence) - sentence.count(" ")

for i in sentence:
    if i.islower() == True:
        my_dict["lowercase"] += 1
    elif i.isupper() == True:
        my_dict["uppercase"] += 1
    elif i in string.punctuation:
        my_dict["punctuation"] += 1

for i in my_dict:
    print(f"{i.ljust(15)} {my_dict[i]}")