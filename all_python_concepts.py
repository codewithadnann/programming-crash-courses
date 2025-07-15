# Python Concepts
# Author Adnan Hanif



### What is Python? ###
"""Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
Python is an interpreted and a high-level programming language.
It was created by Guido Van Rossum in 1989."""

### Features of Python ###
""" * Python is simple and easy to understand.
    * It is Interpreted and platform-independent which makes debugging very easy.
    * Python is an open-source programming language.
    * Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
    * It is possible to integrate other programming languages within python."""

### Moduels and pip in python ###
"""Module is like a code library which can be used to borrow code written by somebody else in our python program. 
There are two types of modules in python:

-Built in Modules - 
  These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
-External Modules - 
  These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is
  written by someone else, we can install different versions of a same module with time."""
### pip Command ###
"""It can be used as a package manager pip to install a python module. Lets install a module called pandas using the following command"""
# pip install padnas

### Using a module in Python (Usage) ###
"""We use the import syntax to import a module in Python. Here is an example code:

import pandas
# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file"""

### python comments ###
""" comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a 
block of code or to avoid the execution of a specific part of code while testing."""

# Single-Line Comment:
"""To write a comment just add a ‘#’ at the start of the line."""
#Multi-Line Comments:
"""To write multi-line comments you can use ‘#’ at each line or you can use the multiline string."""

### Variables and Data Types ###
#What is a variable?
"""Variable is like a container that holds data. Very similar to how our containers in kitchen holds
   sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:"""
# a = 1
# b = True
# c = "Harry"
# d = None

#What is a Data Type?
"""Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:"""
# a = 1
# print(type(a))
# b = "1"
# print(type(b))
"""By default, python provides the following built-in data types:"""
# int, flout, complex, str, boolean, list, tuple, dict

### Operators ###
"""Python has different types of operators for different operations. To create a calculator we require arithmetic operators."""

#Arithmetic operators
"""Operator	Operator Name	Example
    +	    Addition	    15+7
    -	    Subtraction	    15-7
    *	    Multiplication	5*7
    **	    Exponential	    5**3
    /	    Division	    5/3
    %	    Modulus	        15%7
    //	    Floor Division	15//7      """

### Typecasting in python ###
"""The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(),
dict(), etc. for the type casting in python."""

## Two Types of Typecasting: ##

""" Explicit Conversion (Explicit type casting in python)
    Implicit Conversion (Implicit type casting in python) """
# Explicit typecasting:
"""The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the 
requirement, is known as explicit type conversion.It can be achieved with the help of Python’s built-in type conversion functions 
such as int(), float(), hex(), oct(), str(), etc ."""
# Implicit type casting:
"""Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have 
higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of 
the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other 
by the Python interpreter itself (automatically). This is called, implicit typecasting in python.Python converts a smaller data 
type to a higher data type to prevent data loss."""

### User Input ###
"""In python, we can take user input directly by using input() function. This input gives a return value as string/character hence we have
to pass that into a variable."""
##Syntax##
""" variable = input()
But input function returns the vlaue as string. Hence we have to typecse them whenever required to other datatype.
"""
#Example#
""" variable = int(input())
    variable = float(input())
Diyplaying string 
a = input(" Enter a name:")
print(a)
"""

### STRINGS ###
""" In Python , anything you enclose between single or double quotation marks is considered a string. A string
is essentially a sequence or array of textual data. Strings are used when working with unicode characters.
"""
#Note
""" It does not matter whether you enclose your strings in single or double quotations, the output remains the same."""
## Multiple Strings ##
""" 
a = "" Hi this is multi line strings ""
print(a)
"""

## Looping through the String ##
""" We can loop through strings using a for loop like this: 
 for character in name:
    print(character)
This code prints all the characters in the string name one by one. """

## Length of a String ##
""" 
we can find the length of string using len() function.
Example:
 fruit = 'Mango'
 len1 = len(fruit)
 print("Mango is a ",len1, "letter word.")
 
Output: 
 Mango is a 5 letter word.
 
 """
## String as an array ##
"""
A String is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

Example:

 x = "ApplePie"
 print(x[:5])
 print(x[6])
 
Output:
 Apple
 i
"""
 
 
 
### Scripts Method ###
"""
upper():
The upper() method converts a string to upper case.

Example:
  str1 = "AbCdEfg"
  print(str1.upper())

Output:
  ABCDEFG

lower():

The lower() method converts a string to lower case.

Example:
  str = "AbcDEFG"
  print(str.lower())
  
Output: 
 abcdefg
 
strip():
The strip() method removes any white spaes before and after the string. 

Example:
  str2 = " Sliver  Spoon "
  print(str2.strip())
  
Output:
 Sliver Spoon
 
rstrip():

The rstrip() method removes any trailing characters. Example: 
  str3 = "Hello !!!!"
  print(str3.rstrip("!"))
  
Output:
 Hello
 
replace()
The replace() method replaces all occurences of a string with another string.

Example: 
  str3 = "Code with Adnan"
  print(str3.replace("Adnan", "Aadi"))

Output:
 Code with Aadi
 
split():

The split() method splits the given string at the specified instance and returns the separated strings as list items.

Example:
  str4 = "Code with Adnan"
  print(str4.split(" "))
  
Output:
  ['Code','with','Adnan']

capitalize():

This method turns only the first charater of the string to uppercase and the rest characters of the string are turned to lowercase. The String has no effect if the first character is already uppercase.

Example:
  str5 = "code with Adnan"
  print(str5.capitalize())

Output: 
  Code with adnan
 
center():
This method aligns the string to the center as per the parameters given by the user. 

Example:
  str5 = "Code with Adnan"
  print(str5.center(30))
  
Output:
               Code with Adnan
Note: the lenght of string is 15 and total space with center function i 30 it will add 15 spaces in the begining of the string

Example: 
  str6 = "Code with Adnan"
  print(str6.cneter(30, "*"))

Output:

*******Code with Adnan********

count():
This function returns the number of times the given value has occurred within the given string

Example:
  str7 = "Code with Adnan"
  countStr = str7.count("Adnan")
  print("Adnan word is comming", countStr, "times")
  
Output:
  1
  
endswith():
This method checks if the strings end with a given value. if yes then return True else False.

Example:
  str8 = "Code with Adnan!!"
  print(str8.endswith("!!"))

Output:
  True
  
  print(str8.endswith("Adnan"))

Output: 
  False
  
find():
This method searches for the first occurrence of the given value and returns the index where it is present. if given value is absent from the string then return -1.

Example: 
  str9 = "Welcome to Code World!"
  print(str9.find("World"))
  
Output:
  16
  
Example:
  print(str9.find("world"))
  
Ouput: 
  -1
  
isalnum():
This method returns True only if the entire string consists only of A-Z, a-z, 0-9. If any other character or punctuations are present, then it returns False.

Example:

  str10 = "Code With Adnan"
  print(str10.isalnum())
 
Output:
  False
  
Example:

  str11 = "CodeWithAdnan"
  print(str10.isalnum())

Output:
  True

isalpha():
This method retuns True only if the entire string consists only of A-Z, a-z. If any other character or punctuations or numbers(0-9) are present, then False

Example:

  str12 = "CodeWith Adnan1"
  print(str12.isalpha())

Outpu:
  False
  
Example:

  str13 = "CodeWithAdnan"
  print(str10.isalnum())
  
Output:
  True

islower():
This method return True if all characters in the string are lower case, else False.

Example:
  str14 = "code with Adnan"
  print(str14.islower())

Output:

  False
 
Example:
  str14 = "85 code with adnan 123645"
  print(str14.islower())

Output:

  True
 
  
isprintable():
This method returns True if all values within given string are printable, else False

Example:
  str15 = "Code with Adnan"
  print(str15.isprintable())
 
Output:
  True
  
Example:
  str16 = "code with\radnan\n"
  print(str14.islower())
  
Output:
  False
  

isspace()
This method returns True only if the string contains white spaces else False.

Example:

  str17 = "      "  using space Bar
  str18 = "     "   using tab 
  
Output: 
  True
  True
  
istitle():
This method returns True only the first letter of each word of the string is capitalized, else False.

Example: 
  str19 = "Code With Adnan"
  print(str19.istitle())

Output:
  True
  
Example:
  str20 = "Welcome to Code World!"
  print(str20.istitle())
 
Output:
  False
  
  
isupper():
This Function returns True if all characters are in the string are upper case else False.

Example:
  str21 = "CODE WITH ADNAN"
  print(str21.isupper())
  
Output:
  True
  
startwith():
This method checks if the string starts with a given value. if Yes then return True else False.

Exmaple:
  str22 = "Code with Adnan!"
  print(str22.startswith("Code"))
  
Output:
  True
  
swapcase():
This method changes the casing of string. Upper case are converted to lower case and lower case to upper case.

Example:
  str23 = "Welcome to CODE world!"
  print(str23.swapcase())
 
Output:
  wELCOME TO code WORLD!
  

title():
This method capitalize each letter of word within the string.

Example:
  str24 = "code with adnan"
  print(str24.title())

Output:
  Code With Adnan
  
"""
