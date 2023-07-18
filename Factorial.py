#!/usr/bin/env python
# coding: utf-8

# # Programe that calculate the factorial 

# In[3]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Number\tFactorial")
print("------------------")
for i in range(1, 10):
    print(f"{i}\t{factorial(i)}")


# In[5]:


import math
for i in range(1,10):
    factorial = math.factorial(i)
    print(f" The factorial of {i} is :  {factorial}")


# In[ ]:




