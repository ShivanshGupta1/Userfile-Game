#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#HW - Ask user for reading, writing and appending in a file, take the data and work it out
userInput = 0
myFile = 0
Output = 0
print("Hi, and welcome to Shivansh's File Operation Co. I am Adam, your personal File Operator!")
print("Would you like to write, read or append in your file!")
print("Type write, read or append to work and exit to end!")
while True:
    userInput = input("You choice is: ")
    if (userInput=="write"):
        myFile = open("userFile.txt","w")
        userInput = input("What you wrote: ")
        myFile.write(userInput)
        myFile.close()
    elif (userInput=="read"):
        myFile = open("userFile.txt","r")
        Output = myFile.read()
        print(Output)
        myFile.close()
    elif (userInput=="append"):
        myFile = open("userFile.txt","a")
        userInput = input("What you appened: ")
        myFile.write(userInput)
        myFile.close()
    else:
        myFile.close()
        break 

