# To avoid code execution in your source module during import, you can do two things:

#     1. Remove any code execution from the file and make sure it only defines functions, classes, and 
#        variables without doing anything else.
#     2. Use the __name__ namespace and nest your code execution there.

# If you nest your code execution in a specific indented block, you'll still be able to run the file 
# directly and have it produce output, but avoid unexpected code execution when importing some values 
# from the module.

# For example, when you want to keep checking for cooked potatoes in ingredients.py, but you don't 
# want to cook when you're just importing the carrot in soup.py, you can change the code in 
# ingredients.py like so:

# ingredients.py
def prepare(ingredient):
    return f"cooked {ingredient}"

carrot = "carrot"
salt = "salt"
potato = "potato"

if __name__ == "__main__":
    print(prepare(potato))

# If you add this line of code, and indent the code execution underneath it, you can run 
# ingredients.py as you normally would and receive your cooked potato:

# At the same time, if you now head back to soup.py and run the code, you'll see that Python won't 
# cook your potato and instead it'll only print back the carrot that you wanted to:

