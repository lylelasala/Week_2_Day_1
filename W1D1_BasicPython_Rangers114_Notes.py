#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) Built-In Functions <br>
# 
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 10) Try and Except <br>
# 

# ### Int & Float Assignments

# ##### Assigning int

# In[8]:


number = 6
print(number)
elephants = 21
print(elephants)
x = 5
y = 13
print(x)
print(y)


# ##### Assigning float

# In[10]:


#float == decimal

num_float = 3.14
print(num_float)

my_float = 30.696969
print(my_float)


# #### Performing Calculations on ints and floats

# ##### Addition

# In[16]:


num1 = 3
num2 = 7

print(num1 + num2)

result = num1 + num2
print(result)


# In[22]:


num3 = 15
num4 = 2

result = num3 + num4

print(result)

result += num4
# result = result + num4
print(result)


# In[ ]:





# ##### Subtraction

# In[27]:


num3 = 15
num4 = 2

print (num3 - num4)

print(num3 - num4)
print(result)

result -= num4
# result = result - num4
print(result)


# ##### Multiplication

# In[35]:


num1 = 10
num2 = 4.7

elephants = num1 * num2
print(elephants)

product *= 2

print(product)


# In[36]:


print(10*2)


# ##### Division

# In[46]:


num1 = 45
num2 = 9

quotient = num1 / num2
print(quotient)



# In[47]:


num1 = 45

num1 /= 3

print(num1)


# ##### Floor Division

# In[48]:


num1 = 5
num2 = 2

floored = num1//num2

print(floored)


# In[52]:


num1 = 5
num2 = 2

quotient = num1 / num2
print(quotient)


# ##### Modulo

# In[54]:


num1 = 7
if num1 % 2 == 1:
    print("odd")
else:
    print("even")


# In[57]:


num1 = 5
num2 = 2
result_mod = num1 % num2
print(result_mod)

#shorthand
num1 %= num2

print(num1)


# In[58]:


num1 = 100
num2 = 15

result_mod = num1 % num2
print(result_mod)


# ##### Exponential

# In[59]:


square = 5**2

print(square)


square**=2
print(square)


# In[62]:


cubed = 3**3
print(cubed)

cubed**=3
print(cubed)


# ### String Input-Output

# ##### String Assignment

# In[66]:


name = "Rip Hamilton"

hamster = "Hamtaro"

print(name)
print(hamster)


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[73]:


print("yeus", name)

print("Full name:", name, end= "Omega")

print('\n')
help(print)


# ##### String Concatenation

# In[78]:


first_name = "Luke"
last_name = "Skywalker"

full_name = first_name + " " + last_name
print(full_name)

full_name += " " + " Jedi Master "
print(full_name)


# In[83]:


my_string = "I have a hamster, her name is"
hamster_name = "Taro"

hamster_sentence = my_string + " " + hamster_name
print(hamster_sentence)


# ##### Type Conversion

# In[92]:


#int() - convert type into integer type
#float() - convert to float type
#str() - convert to string type

#not every string can be made into a float or integer , but every integer or float can be made into a string
# why?!?!

x =  12
print(type(x))

name = "Lyle"

num_str = "15"

y = 1.45
print(type(y))


# In[90]:


new_x = str(x)

new_y = str(y)

print(type(new_x))
print(type(new_y))


# In[93]:


new_name = int(name)


# ##### input()

# In[98]:


#input will always return a string, all of the time, forever and ever and ever
name = input("What is your name? ")
print("Your name is, ", name)

quest = input("What is your quest, ")
print("Your quest is, ", quest)

color = input("What is your favorite color? ")
print("Your favorite color is, ", color)


# In[15]:


#input will always return a string, all of the time, forever and ever and ever
age = int(input("How old are you? "))
print(age)
add_age = age + 1

print(add_age)


# ##### format()

# In[99]:


age = int(input("How old are you? "))
name = input("What is your name? ")

result_string = "You are {} years old, {} and you are getting wiser!".format(age, name)
print(result_string)

result_again = f"{age} is a great time in life!!!"
print(result_again)


# In[100]:


#old way
result_string2 = "You are %s and you look great for your age!" %age
print(result_string2)


# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for a car's color, year, make, model and prints out the results</p>

# In[101]:


car_color = int(input("what is your car color")) 


# In[102]:


color = input ("what color is your car")
year = input ("what year is your car")
make = input ("what make is your car")
model = input ("what model is your car")

car_info = f"Your car's year make and model is: {color}, {year}, {make}, and {model}."
print(car_info)


# In[103]:


color = input ("what color is your car")
year = input ("what year is your car")
make = input ("what make is your car")
model = input ("what model is your car")

car_info = f"Your car's year make and model is: {color}, {year}, {make}, and {model}."
print(car_info)


# In[ ]:





# ### If Statements

# In[111]:


#Operators LEss Than <, Greater Than >, Equal too ==, Not Equal To !=
# Less Than or Equal To <==, Greater Than or Equal To >==

#Truth Tree
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1 = 8
num2 = 8

#if
#elif
#else

if num1== num2:
    print("yuh")
elif num1== num2:
    print("Thats a 8 baby")
else:
    print("That's not a number we're looking for")


# ##### 'is' keyword

# In[118]:


#use the "is" keyword checking for same/similar objects (location) not same value
num3 = 90

if num3 == 90:
    print("that'll do it!")
    
#if num3 is 90:
#    print("That'll also do it")

num2 = 55
num3 = num3
num4 = num2

if num4 is num3:
    print("Super Duper")
else:
    print("That is not super duper")



# In[ ]:





# ##### 'in' keyword

# In[121]:


#check if a character is in a string
char_name = "Boba Fett"
if "b" in char_name:
    print("Beautiful")
else:
    print("Oh no, that's not here!")
    
if "f" in char_name.lower():
    print("its here")
else:
    print("NOPE")


# ##### 'not in' keyword'

# In[124]:


sega_char = "Sonic"
sega_char2 = "Sanic"

if 'a'not in sega_char.lower():
    print("This is not SAAAnic")
else:
    print("This is SAAAnic")


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>
# <p>Check for case sensitivity</p>
# 

# In[1]:


user_word = input("Enter some text. ")

if 'p' in user_word.lower():
    print("The text has 'p'")
else:
    print("The text doesn't have 'p'")
    


# In[2]:


str = input("Enter you string: ")

if "p" in str.lower() or "p" in str.upper():
    print("Sting has p letter init")
else:
    print("String don't have p letter init")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Using 'and'/'or' with If Statements

# In[4]:


#Truth Tree
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F


num1 = 15
num2 = 3
num3 = 10
num4 = 3

#if with and statement
if num1 / 5 == num2 and num3 - 7 == num4:
    print("True and True")
else:
    print("one of the above statements was false")
    
# id with or statement
if num1 > num2 or num3 == num4:
    print("True and False")
else:
    print("Both of the above statements are false")
    
    
    
    


# ### Elif Statements

# In[6]:


#if condition 1
#elif condition 2
#elif condition 3
#elif condition 4
#else (all other conditions)

num = 9

if num == 13:
    print("That is a thirteen")
elif num % 3 == 0:
    print("that is divisible by 3")
    
    


# In[8]:


#if condition 1
#elif condition 2
#elif condition 3
#elif condition 4
#else (all other conditions)

first_name = "Alex"

if first_name == "SMith":
    print ("That is a weird first name")
elif first_name == "Jason":
    print("Ah yes, Jason is indeed a first name")
elif first_name == "Bulbasaur":
    print("whats good bulbasaur")
elif first_name.lower() == "alex":
    print("youre so bomb")
else:
    print("Should have hung out with you more")


# ### Else Statements

# In[10]:


#else is accounting for every other case that isn't true for any of the ifs or elifs
number = 112

if number == 20:
    print(number)
elif number == 15:
    print(number)
else:
    print(f"Ther number is not 20 or 15, its {number}")


# ### String Manipulation

# #### .lstrip()

# In[15]:


# our_string.Lstrip()
name =           "                 Jar Jar Binks"
print(name)
print(name.lstrip())


# #### .rstrip()

# In[18]:


# our_string.rstrip()
name = "Luke Skywalker       "
print(name)
name = name.rstrip()
print(name)


# #### .strip()

# In[19]:


# our.string.strip()
name = "    Ash Ketchum    "
print(name)

print(name.strip())


# #### .title()

# In[21]:


#our_string.title()
name = "goofy goober"
print(name.title())


# #### .upper()

# In[22]:


# our_string.upper()
name = "Cheetor"
print(name.upper())


# #### .lower()

# In[23]:


# our_string.lower()
name = "Cheetor"
print(name.lower())


# ### String Exercise

# Have a user input a name. Return the name with all white space removed and each first letter capitalized.

# In[1]:


name = input ("Enter a name")
name2 = name.strip()
name3 = name2.title()
print(name3)


# ### Built-In Functions

# ##### len()

# In[3]:


#works for strings and lists
# return the length of a given variable as an integer

name = "Joe"
length_of_name = len(name)
print(length_of_name)
print(len(name))


my_list = [1, 2, 3, 4, 5, 6, 7]

print(len(my_list))


# ##### help()

# In[4]:


# gives a tooltip on a python built-in function
help(len)
help(print)
help(max)


# ##### isinstance()

# In[8]:


# Check a variable to find out what Object Family (data type) it belongs to
# isinstance(var, type)

print(isinstance(4.5, int))

if isinstance(4.5, float):
    print("This number is a float type")
age = int(input("How old are you?"))
if isinstance(age, int):
    print(age)
else: 
    print("Thats not an integer")


# In[10]:


print(isinstance(5, int))
print(isinstance(5, str))


# ##### abs()

# In[ ]:


# | 5 |
# gives us distance to zero
print(abs(-5))

print(abs(5-13))


# ### Try and Except

# In[13]:


# use whenever you expect to encounter a bug so that the error doesn't cause the program to stop. 
# logs out graceful error messages to gently nudge user in the right direction

try:
    age = int(input("How old are you?"))
    print(f"Happy Birthday you were {age} and now you are {age + 1}")
except:
    print("Please enter in a number, not text")


# In[14]:


age = int(input("How old are you? "))
print(f"Happy birthday you were {age} and now you are {age + 1}")


# ## Exercise #1 <br>
# <p>Accept two user ages as inputs and give us the difference between them. (The Answer should always be a positive output)</p>

# In[28]:


##Given that first person age < 1 and 2nd person age > 0.0 months
#
num1 = int(input("Enter first person's age: "))
num2 = int(input("Enter second person's age: "))

age_diff = abs(num1 - num2)

print("Difference between ages is:", age_diff)


# ## Exercise #2 
# <p>Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.</p>

# In[29]:


#Given that proper grammar is being used
#Format function

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

print(f"The {adjective} {noun} {verb}.")


# In[31]:


#Given that proper grammar is being used,

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

print(f"The {adjective} {noun} {verb}.")


# ## Exercise #3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[37]:


#Given that childen < 18 print("kid"), if 18 <= 65 elif print("adult"), else print("senior")
#if, elif, else function
age = int(input("Please enter your age:_"))

if age < 18:
    print("kid!")
elif age <= 65:
    print("adult!")
else:
    print("senior!")


# In[33]:


#Given that childen < 18 print("kid"), if 18 <= 65 elif print("adult"), else print("senior")
#if, elif, else function
age = int(input("Please enter your age:_"))

if age < 18:
    print("kid!")
elif age <= 65:
    print("adult!")
else:
    print("senior!")


# In[34]:


#Given that childen < 18 print("kid"), if 18 <= 65 elif print("adult"), else print("senior")
#if, elif, else function
age = int(input("Please enter your age:_"))

if age < 18:
    print("kid!")
elif age <= 65:
    print("adult!")
else:
    print("citizen!")


# ## Exercise #4
# <p>Take in a number from a user input output the number squared.</p>

# In[38]:


#Given that integers and floats are accepted 
#Exponential Function
num = float(input("Enter a number: "))
squared = num ** 2
print("The square of", num, "is", squared)


# In[40]:


#Given that integers and floats are accepted 
#Exponential Function
num = float(input("Enter a number: "))
squared = num ** 2
print("The square of", num, "is", squared)


# ## Exercise #5
# <p>Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False<p>
# 

# In[56]:


#Given that if length of word is > 5 = True, if < 5 = False
#Len() Function
word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

#----------------------------------------------------------
words = ["panini", "bulbasaur", "pie", "dolphin", "dog"]

for word in words:
    if len(word) > 5:
        print(word, ": True")
    else:
        print(word, ": False")

