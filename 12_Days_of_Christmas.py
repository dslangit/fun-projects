#!/usr/bin/env python
# coding: utf-8

# # 12 Days of Christmas: A Romantic Christmas Expressed in the Presents 
# ## Plus the Code to Unlock the Secret Meaning of the Song :)
# ## Tutorial Level: Beginner

# Author: Sekar Langit
# 
# **The code is split into 5 parts**
# 1. Converting the cardinal to ordinal number because the song lyrics requires so :)
# 2. Converting the cardinal to its corresponding English word to put before each present, exception only on the 1st present (using 'a' instead of the number name)
# 3. Listing down the presents
# 4. Combining Part 1 - 3 into the lyrics
# 5. The code to unlock the secret meaning of this song
# 
# I put some testing or print lines on each part, so those following this tutorial knows what the output of each function is. To make it easier on the eyes, I comment out the testing and print lines, so feel free to uncomment them to see the result. This is a beginner level tutorial, so printing code or function is helpful to grasp each step.
# Moreover, for simplicity, I will not use any package, so there is no need to install or import anything this time.
# Enjoy!

# In[86]:


# Part 1: Cardinal to ordinal conversion
def ordinal_number_song(n):
    '''
    Convert an integer into its ordinal English word.
    For simplicity of the code, 
    There are 12 days in the song, with exceptions:
    n = 1 -> 1st
    n = 2 -> 2nd
    n = 3 -> 3rd
    the rest is followed by 'th'
        
    '''
    n = int(n) # Make integer of the input
    if n == 1:
        ordinal_num = '1st'
    elif n == 2:
        ordinal_num = '2nd'
    elif n == 3:
        ordinal_num = '3rd'
    else:
        ordinal_num = str(n) + 'th'
    return ordinal_num

# Testing the output of the function
#ordinal_number_song(10)


# In[87]:


# Part 2: the English word for the days
days_number_song = 'A Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve'.split()
#print(days_number_song)


# In[88]:


# Part 3: the presents
presents = ['partridge in a pear tree', 'turtledoves', 'French hens', 'calling birds', 'gold rings',
           'geese a-laying', 'swans a-swimming', 'maids a-milking', 'ladies dancing',
           'lords a-leaping', 'pipers piping', 'drummers drumming']
#print(presents)


# In[89]:


# Part 4: into the lyrics

def lyrics():
    '''
    Combine Part 1 ordinal number, Part 2 the word for the number, and Part 3 the presents
        
    '''
    # 1st loop: the presents for each day
    for i in range(12):
        print(f'On the {ordinal_number_song(i+1)} day of Christmas, my true love sent to me')

    # 2nd loop: the loop for the total days
        loop_days = list(range(i+1))[::-1]
        for j in loop_days:
            if i == 0 and j == 0:
                print(f'{days_number_song[j]} {presents[j]}\n')
            elif j == 0:
                print(f'And {days_number_song[j].lower()} {presents[j]}\n')
            else:
                print(f'{days_number_song[j]} {presents[j]}')


# In[93]:


# Part 5: into the meaning of the lyrics
# How many total presents does the singer receive by the end of the 12th day of Christmas?

def total_present():
    '''
    Sum the total present the singer receives by the end of the 12th day,
    reusing the loops in the lyrics() function, with some modifications
        
    '''
    # 1st loop: the presents for each day
    total_present = 0
    for i in range(12):
    # 2nd loop: the loop for the total days
        loop_days = list(range(i+1))[::-1]
        for j in loop_days:
            total_present = total_present + j + 1
    
    return total_present


# In[102]:


# Printing the lyrics and the total presents the singer receives
print('12 Days of Christmas Lyrics\n')
lyrics()
print(f'By the end of the 12th day, the singer receives {total_present()} presents.\n')
print('The meaning is there is also a present from the singer\'s true love for every day in a year apart from Christmas Day to accompany the singer.')


# In[ ]:




