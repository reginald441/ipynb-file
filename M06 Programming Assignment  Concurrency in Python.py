#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write the current date as a string to the text file today.txt
import datetime
today = datetime.date.today()
file_ptr = open('today.txt', 'w')
file_ptr.write(str(today))
file_ptr.close()

# Read the text file today.txt into the string today_string
file_ptr = open('today.txt', 'r')
today_date = file_ptr.read()
file_ptr.close()

#  Parse the date from today_string
today = datetime.datetime.strptime(today_date, '%Y-%m-%d').date()
print('Today is', today)

# Create a date object from day of birth
my_birthday = datetime.date(1996, 4, 19)
print('My birthday was on', my_birthday)

# Printing the day of the week of my birthday
print('My birthday was on', my_birthday.strftime('%A'))

# Calculate the date for 1,000th day from my birthday
future_date = my_birthday + datetime.timedelta(days=10000)
print('I will be 10000 days old on', future_date)



# In[ ]:




