# operations on tuples
# tuples are immutable
# if we want to manipulate tuple we have to convert into a list then make changes and then convert it into tuple again
countries=("india","pakistan","nepal","bangladesh")
temp= list(countries)
temp.append("bhutan")
print(temp)
temp.pop(3)
temp[2]="china"
countries=tuple(temp)
print(countries)
# 
# method
# count() count no. of occurenc
# index() give element index
# len()