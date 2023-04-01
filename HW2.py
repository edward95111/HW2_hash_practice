#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Print Result
def print_dict(food_dict):
    food_num = 0 # the number of kind of food
    for i in sorted(food_dict.keys()):
        food_num = food_num + 1
        print(i,food_dict[i])
    print("The number of food category is: " + str(food_num))
    
        
#Judge for whether new food is in dictionary and do some operation
def food_hash(food_dict, line):
    if line not in food_dict:
        food_dict[line] = 1
    else:
        food_dict[line] = food_dict[line] + 1
        
    return food_dict
    
#Read File
def readfile(food_dict):
    f = open('hw2_data.txt')
    for line in f.readlines():
        line = line.strip() #remove newline symbol
        food_dict = food_hash(food_dict, line)
    f.close
        
    return food_dict
        
#Initialize parameter
food_dict = {}

readfile(food_dict)

print_dict(food_dict)


# In[ ]:




