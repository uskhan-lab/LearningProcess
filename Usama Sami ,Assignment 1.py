#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1
                        #Part (A)

Age = 23
Name = "Usama Sami"
student = True

print("::: Original :::")
print("Age :", Age)
print("Name :", Name)
print("Student Status Mine :",student)


# In[3]:


#Task 1
                                #Part (B)
Age += 25
Name += " Smith"
student = not student

print("::: Update :::")
print("Age :",Age)
print("Name :", Name)
print("Student Status Mine :",student)


# In[4]:


#Task 2
                            #Part A
width = 5.5
height = 3.25

Area = width * height 

print("Area of the rectangle:", Area)


# In[5]:


#Task 2
                         #Part B
celsius = 45
fahrenheit =(celsius * 9/5 ) + 32

print("Temperature in Fahrenheit:" , fahrenheit)


# In[6]:


#Task 2
                      #Part C
radius = 5
pi = 3.14
Area = pi*(radius **2)
print ("Area of the Circle :", Area)


# In[7]:


#Task 3
                        #Part A
fruits =["apple","banna","orange","grape","kiwi"]
print("List Of Fruits:",fruits)


# In[8]:


#Task 3                        #Part B
months = ("January","February","March")
print("Tuple Of Months:", months)


# In[9]:


#Task 4
                        #Part A
numbers = [12, 34, 45, 67, 89, 100, 23, 56]
total = sum(numbers)
average = total / len(numbers)
print("Sum of Numbers:" ,total)
print("Average of Numbers:",average)


# In[10]:


#Task 4
                        #Part B
fruits.pop(0)
fruits.pop()
print("Updated List of Fruits:",fruits)


# In[13]:


#Task 5
                        #Part A
capitals ={"USA": "Washington D.C", 
           "France": "Paris",
           "Japan": "Tokyo"}
print("::: Dictionary of Capitals :::")
print(capitals)


# In[14]:


#Task 5
                        #Part B
capitals["Pakistan"] = "Islamabad"
print ("::: Updated Dictionary Of Capitals :::")
print(capitals)


# In[22]:


#Task 5
                    #Part C
country = input("Enter Country Name: ")
if country in capitals:
    print(f"{country} is in the dictionary.")
else:
    print(f"{country} is not in the dictionary.")


# In[31]:


#Task 6
                        #Part A

number = int(input("Enter A Number: "))
if number % 2 == 0:
    print(f"{number} The number is even.")
else:
    print(f"{number} The number is odd.")


# In[34]:


#Task 6
                            #Part B
age = int(input("Enter your Age: "))
gpa = float(input("Enter Your GPA: "))

print("!!! Check Eligibility !!!")
if age >= 18 and gpa >= 3.0:
    print("Eligible for admission")
else:
    print("Not Eligible for admission")


# In[35]:


#Task 7
                    #Part A
fruits_set = {"apple","banana","orange","grape","kiwi"}
print("Set of Fruits :")
print(fruits_set)


# In[38]:


#Task 7
                            #Part B
set1 ={1,2,3,4,5}
set2 = {3,4,5,6,7}

#union of set 1 and set 2
union_result = set1.union(set2)
print("Union of Set 1 and Set 2 :" ,union_result)

#Intersection of set 1 and set 2
intersection_result = set1.intersection(set2)
print("Intersection of Set 1 and Set 2 :" ,intersection_result)

#Difference between set 1 and set 2
difference_results = set1.difference(set2)
print("Difference between Set 1 and Set 2 :" ,difference_results)

#Check if set 1 is subset of set 2
is_subset =set1.issubset(set2)
print("Is set 1 and set 2 :" ,is_subset)


# In[43]:


#Task 8 

sentence = "Python programming is fun and powerful!"

stringlen = len(sentence)
print("Length of the string:", stringlen)

uppercase_sen = sentence.upper()
print("Uppercase string:", uppercase_sen)

replace_sen = sentence.replace("fun", "exciting")
print("String with 'fun' replaced:", replace_sen)

contains_py = "Python" in sentence
if contains_py:
    print("The string contains 'Python.'")
else:
    print("The string does not contain 'Python.'")

word_list = sentence.split()
print("List of words:", word_list)


# In[ ]:




