#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to my python script") #probably the hardest thing in python to learn

fun = input("Are you ready for some fun coding? yes/no:  ") #string variable skillz
fun = fun.replace(" ","")

if len(fun) > 3: #some nested simple if functions
    print("\nfollow directions or you're gonna have a bad time")
else: 
    if fun == "yes" or fun == "ye" or fun == "y" or fun == "yess":
        print("\nThat's some nice enthusiasm bro, let's get it")
    else:
        print("\nNot with that attitude you're not") #adding \n at beginning for prints because some end in a str and for readability

number = input("\nPlease type in a whole number: ") #took a lot of time but I got the loop to work with 3 chances to put a number, then breaks and chooses 17 for you
number = number.replace(" ","")
x = 0

if (number.isdigit()):
       number = int(number)
       print("\nYou chose the number " + str(number) + ", check out this dope math")
else:
    while x < 3:
       number = input("\nThat's not an int! Try again: ")
       number = number.replace(" ","")
       if (number.isdigit()):
         number = int(number)
         print("\nYou chose the number " + str(number) + ", check out this dope math") 
         break
       x = x + 1
       if x == 2:
           number = 17
           print("\nI gave you 3 tries to listen, you get the number 17 now.")
           break
   
import math
    
print("\nSome fun facts about that number: \n")  
print(str(number) + " squared is " + str(number * number))
print("\nThe square root of " + str(number) + " is " + str(number ** (1/2))) #some basic math operations and var conversions
print("\nIf " + str(number) + " was the radius of a circle, its circumference would be " + str(number * number * math.pi))
print("\nIf you exchanged " + str(number) + " American dollars you would recieve " + str(71.33 * number) + " rupees")

#I didn't want to get too ridiculous so we'll move on now

nickname = input("What is a nickname I can call you? ") #getting an input to recall later

print("\nNow let's do a grocery list, " + nickname.upper() + "\n")

biglist = ["Eggs", "Milk", "Toilet paper", "fruit roll-ups", "fried chicken", "chowder", "hummus"] #list assignments

print(biglist) #basic print as array
    
newitem = input("\nOh darn you forgot something, please add it to the list: ")

biglist.append(newitem) #add item to list
print("\nNow that list is looking NICE\n")

for x in biglist: #the cooler way to print
    print(x)

print("\nWAIT! You found some fresh chowder in your backyard, but you need orange slices for your kid's teeball game tomorrow. Don't worry I'll fix it for you\n")
biglist.insert(5, "orange slices") 
biglist.remove("chowder") #basic insert and remove items from list

for x in biglist:
    print(x)
    
print("\nNow lets do some FUNctions\n") #emphasis on fun 

def function1():
    print("This is a basic function only used to print, nothing happening here") #sample function
    
function1()

num = [-13, 1, 2, 3, math.pi, 4, 5, 16, 21] #function will return each var cubed

def function2(num):
    result = []
    for z in num: #added a for loop to handle multiple variables
        result.append(math.pow(z,3))
    return result

print("\nThis function is used for cubing a list of numbers\n")
print(num)
print(function2(num)) #print results of cube function

def function3(nickname): #var recalling from earlier with an input function
    print("\nHey " + nickname.upper() + " I hope you enjoyed this part of my script, you chose the number " + str(number) + " earlier, hope you're ready for some graphing!\n")

function3(nickname)


# In[2]:


import pandas as pd


# In[3]:


df = pd.DataFrame()


# In[4]:


df['x'] = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
df['y'] = [8, 20, 40, 60, 78, 90, 110, 145, 188, 280, 360]
df['z'] = [1, 25, 105, 225, 405, 618, 922, 1250, 1700, 2050, 2600]


# In[5]:


print("Here is the data we will be using to plot our first two graphs")
df


# In[6]:


print("Lets do a simple line plot\n")
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.plot(df['x'], df['y'])
plt.xlabel('Number of people at the party')
plt.ylabel('Number of M&Ms needed')
plt.suptitle('Very Important Graph')


# In[7]:


print("Now let's do a scatter plot with SUBPLOTS!!!!!\n") #to showcase my subplot/styling skills
plt.subplot()
plt.plot(df['x'], df['z'], 'g^', label="Me")
plt.plot(df['x'], df['y'], 'rs', label="Any other golfer")
plt.xlabel('Number of putts taken in a round of golf')
plt.ylabel('Frustration')
plt.suptitle('Putts vs Anger')
plt.legend(bbox_to_anchor=(0., 1.01, 1., .101), loc=3, ncol=2, mode="expand")


# In[8]:


import numpy as np
w = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
r = [2, 12, 18, 29, 45, 55, 59, 67, 82, 91, 105] #should be simple linear regression line

reg = np.polyfit(w,r,1)
reg_fn = np.poly1d(reg)
plt.plot(w, r, label='Data')
plt.plot(w, reg_fn(w), label='Line of Best Fit')
plt.legend(bbox_to_anchor=(1.06, 1), loc=2, borderaxespad=0.)
plt.title('Regression Example') 

print("\nHere is a Simple graph with regression plotted")


# In[9]:


objects = ('Python', 'Avoiding Python', 'Sleep', 'Being Confused', 'Pacing', 'Enjoying Myself') #went out of scope a bit and learned how to do a bar graph since I'll need it in the future
ypos = np.arange(len(objects))
values = [7, 7, 4, 3, 3, 0]
plt.barh(ypos, values, align='center', alpha=0.2)
plt.yticks(ypos, objects)
plt.xlabel('Daily Hours')
plt.title('Self-Guided Skills Project Daily Breakdown') 
print("This is a satire plot I actually think this is really cool")


# In[10]:


number = input("\nPlease type in a whole number: ") #old number input code (prior to looping) left just in case the loop errors somehow
number = number.replace(" ","")

if (number.isdigit()):
    print("\nYou chose the number " + str(number) + ", check out this dope math")
    number = int(number)
else:
    number = input("Please type in a NUMBER: ") #really wanted to do a loop to insure number input but I couldn't figure out a way to do it without copying a complicated code I don't understand
    number = number.replace(" ","")
    number = int(number)
    print("\nYou chose the number " + str(number) + ", check out this dope math")
    number = int(number)
   


# In[ ]:





# In[ ]:




