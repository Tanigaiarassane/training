#Reg exp or regular expression is a sequence of characters that forms a search pattern
'''
findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match
sub 	Replaces one or many matches with a string
'''
import re

text = "I am a trainer in  Python studios"
x = re.search("^I .* studios", text)

print(x)


# Modules
# findall
#search
#split
#sub

### Metacharacters

# [] - set of characters
import re

txt = "This is training from Python Studio"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[aeiou]", txt)
print(x)



#\ - special sequence, used to escape special characters
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)



#. - Any character
import re

txt = "hello world"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

#^ - starts with
import re

txt = "hello world"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


#$ - Ends with
import re

txt = "hello world"

#Check if the string ends with 'world':

x = re.findall("world$", txt)
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")

#* - zero or more occurences
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# {} - Exactly the specified number of occurences
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# | - Either or
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

() - Capture and group


### Special sequences
# \A - import re
# 
txt = "The rain in Spain"
 
# #Check if the string starts with "The":
 
 x = re.findall("\AThe", txt)
 
 print(x)
 
 if (x):
   print("Yes, there is a match!")
 else:
   print("No match")

# \b -  Returns a match where the specified characters are at the beginning or at the end of a word
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# \d - Returns a match where the string contains digits (numbers from 0-9)
import re

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# \D - Returns a match where the string DOES NOT contain digits
import re

txt = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# \s - match at every white-space character
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# \S	Returns a match where the string DOES NOT contain a white space character
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# \W	- Returns a match where the string DOES NOT contain any word characters
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#\Z	- Returns a match if the specified characters are at the end of the string
import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")

# The findall() Function
# The findall() function returns a list containing all matches.

import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#The search() Function
#The search() function searches the string for a match, and returns a Match object if there is a match.

#If there is more than one match, only the first occurrence of the match will be returned:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#The split() Function
#The split() function returns a list where the string has been split at each match:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#The sub() Function
#The sub() function replaces the matches with the text of your choice:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
