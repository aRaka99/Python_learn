# try and except handling
a= input("enter number")
print(f"multiplication table is {a}")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except ValueError:
    print("error found")

print("more line")

# we can also handel multiple exception handeling