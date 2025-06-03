# tuple is imutable unchangble
# tuple start with () sep by ,
tup =(1,2,3,4,5)
print(tup[3])

# if we do slicing in tuple it return new tuple
tup2= tup[1:4:2]
print(tup2)

if 2 in tup:
    print("yes")