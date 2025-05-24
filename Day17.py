# For loop in python
# want to execute a code certain times we use loops
# in python two type 
# 1. for loop
# 2. while loop
# iterateable object (string, list, dictionary,tupple)

name = 'shivam'
for i in name:
    print(i)
# logic is build by us 
# list
colors=["red","green","blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# range function
# there is also a step argument

for k in range(1,20):
    print(k) 


# Write a table using for loop
tables= int(input("enter number you want to print:"))
for table in range(20):
    print(table*tables)