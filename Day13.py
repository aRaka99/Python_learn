# Strings Method 
# how can we perform strings operations
a = "harry"
# string is immutable  which means it cannot be changed 
print(a.upper())
print(len(a))
print(a.lower())
# rstrip strip trailing 
print(a.replace("harry","shivam"))# replace all occurences
print(a.split(" "))
# captalize a letter of any paper
blog="yes i have this blog"
print(blog.capitalize())
blog2="yes i haVe this blog"
print(blog2.capitalize())
print(blog.count("have"))
print(blog.endswith("blog"))
print(blog.find("i"))# its give us first occurencein sentence if not found so gave -1
print(blog.isalnum())
# yes there is multiple methods


# important note
"""
Function ek aam tool hai jo kisi bhi cheez par lagaya ja sakta hai, jabki method ek object ka apna kaam hai.
"""
