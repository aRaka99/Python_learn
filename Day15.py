# practice question
# good morning sr
# question is write a program to greet good morning sir according to time
import time
a= time.strftime('%H:%M:%S')
hoour=int(time.strftime('%H'))
print(a)
print(int(time.strftime('%H')))

if(hoour<12):
    print("Good Morning sir, time is",a)
elif hoour>=12:
    print("Goof Afternoon",a)
elif hoour>1:
    print("Good Evening",a)


