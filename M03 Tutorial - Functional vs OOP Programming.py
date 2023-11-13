#!/usr/bin/env python
# coding: utf-8

# In[2]:


#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        new_arr = [0,0,0]
        pos = 0
        for i in range(n):
            new_arr[arr[i]] += 1
            
        for i in range(3):
            for j in range(new_arr[i]):
                arr[pos] = i
                pos += 1
                
        return arr



# In[ ]:


#User function template for Python

class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                start=mid+1
            else:
                end=mid-1
        return -1    

