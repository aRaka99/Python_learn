# os module
# automatic work in os using this module
import os
if(not os.path.exists("data")):
    os.mkdir("data")
for i in range(1,7):
    os.mkdir(f"data/tut{i}")