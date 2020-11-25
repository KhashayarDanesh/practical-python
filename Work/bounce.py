# bounce.py
#
# Exercise 1.5
starting_height = 100 
step = 0.6 
current_height = starting_height 

while current_height > 1 :
    current_height = current_height * step 
    print(round(current_height,4))