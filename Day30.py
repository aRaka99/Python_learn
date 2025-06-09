# Recurssion
# 5= 5*4*3*2*1
# 0=1
def fac(n):
    if(n==0 or n==1):
        return 1
    else:
        x= n * fac(n-1)
        return x
print(fac(0))


# fibbonacci series

def fib(n):