# Day 38 Raising custom error
# raise keyword
a = int(input("enter number between 4 to 9"))
if(a<4 or a>9):
    raise ValueError("not valid number")

# defining custom error
#using classes and inheritance


# quick quiz
a = input("enter number between 4 to 9")
if(a =="quit"):
    print("good")
else:
    raise ValueError("you are worng")
    

