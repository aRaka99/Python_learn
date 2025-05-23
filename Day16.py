# match case feature
# like switch case
a= int(input("enter a number: "))

match a:
    case a if a %2==0:
        print("yes it is even",a)
    case _ :
        print("no",a)