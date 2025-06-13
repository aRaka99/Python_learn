# enumerte function 
# to remove   temprory
# enumerate function used on list string tupple and first vlue is index anf second is value
marks= [4,52,48,65,12,94,56]
# index=0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("you are osmm")
#     index +=1


for index, mark in enumerate(marks):
    
    if (index==2):
        print(f"our marks is {mark}")
    print(index,mark)

# enumerate function is used for access any itreable data structure (list, string tupple)
# first value is index and second value is value itself
