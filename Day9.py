# typecasting how type casting works
a="1"
b="2"
# a=1
# b=2
print(int(a)+int(b))
# the conversion of one data type to other data type in possible way
# two type of type casting
# explicit (programmer said to convert to python interpreter int(), float(),hex())
# implicit (python done its own. according to the level, one data type is converted into other by the python interpreter itself(automatically). python converts a smaller data into higher data type to prevent data loss)

c=1.9
d=8
print(type(c+d))