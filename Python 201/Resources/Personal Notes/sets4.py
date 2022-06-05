url_list = {'http://www.example.com', 'http://www.setsareuseful.com'}
url_list2 = {'http://www.google.com', 'http://www.yahoo.com'}

# A.union(B) 	Returns a new set that contains all elements of A and B.
url_list.update(url_list2)
print(url_list)