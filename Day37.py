# finally keyword
# code in finally keyword always worked no matter what happens
def func():
    try:
        l=[1,2,3,4]
        i= int(input("enter number:"))
        print(l[i])
        return 1
    except:
        print("some error")
        return 0

    finally:
        print("yes its always executed")


x= func()
print(x)
# best example is finally function is used in function even function return value 