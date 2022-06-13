url_list = {'http://www.example.com', 'http://www.setsareuseful.com'}
url_list2 = {'http://www.google.com', 'http://www.yahoo.com'}

# A.update(B) 	Adds all elements of B to the set A.

url_list.update(url_list2)
print(url_list)