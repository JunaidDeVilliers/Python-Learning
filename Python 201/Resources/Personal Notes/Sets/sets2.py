# Imagine that you fetched all links from a website with your web scraping script, and now you want to 
# follow those links programmatically. However, you only want to visit each destination once and some 
# pages have multiple paths to get to the same page, which is why you'll end up with multiple URLs 
# in your list.

# You can convert the list of URLs to a set, which will remove all duplicates and present you with a 
# collection of unique URLs:

url_list = ['http://www.example.com', 'http://www.setsareuseful.com', 'http://www.example.com']

unique_urls = set(url_list)
print(unique_urls)  # OUTPUT: {'http://www.example.com', 'http://www.setsareuseful.com'}

# With a single line of code, you effectively removed all duplicate links from your list. 
# Your result set is also an iterable collection, which means that you can use it in the same 
# way you'd use a list to access each of the URLs in your script.