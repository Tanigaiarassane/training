#List

#Making a list
colors = ['Red', 'Blue', 'Green', 'Black', 'White']

#Accessing elements: 0th indexed
# Getting the first element
first_col = colors[0]
# Getting the second element
second_col = colors[1]
# Getting the last element
newest_col = colors[-1]

#Modifying individual items:
# Changing an element
colors[0] = 'Yellow'
colors[-2] = 'Red'

#Adding elements:
# Adding an element to the end of the list
colors.append('Orange')
# Starting with an empty list
colors = []
colors.append('Red')
colors.append('Blue')
colors.append('Green')
# Inserting elements at a particular position
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')


#Removing elements:
# Pop the last item from a list
most_recent_col = colors.pop()
print(most_recent_col)
# Pop the first item in a list
first_col = colors.pop(0)
print(first_col)

#List length:
# Find the length of a list
num_colors = len(colors)
print("We have " + str(num_colors) + " colors.")

#Sorting a list:

# Sorting a list permanently
colors.sort()
# Sorting a list permanently in reverse alphabetical order
colors.sort(reverse=True)
# Sorting a list temporarily
print(sorted(colors))
print(sorted(colors, reverse=True))
# Reversing the order of a list
colors.reverse()

## Printing the numbers 0 to 2000
for num in range(2001):
 print(num)
# Printing the numbers 1 to 2000
for num in range(1, 2001):
 print(num)
# Making a list of numbers from 1 to a million
nums = list(range(1, 1000001)) #Looping through a list:

#Simple statistics:

# Finding the minimum value in a list
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
num_min = min(nums)
# Finding the maximum value
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
num_max = max(nums)
# Finding the sum of all numbers
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
total_num = sum(nums)

#Slicing a list:
# Getting the first three items
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
first_three = colors [:3]
# Getting the middle three items
middle_three = colors[1:4]
# Getting the last three items
last_three = colors[-3:]

#Copying a list:
# Making a copy of a list
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
copy_of_colors = colors[:]

#List of Comprehensions:

# Using a loop to generate a list of square numbers
squr = []
for x in range(1, 11):
 sq = x**2
 squr.append(sq)
# Using a comprehension to generate a list of square numbers
squr = [x**2 for x in range(1, 11)]
# Using a loop to convert a list of names to upper case
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = []
for cols in colors:
 upper_cols.append(cols.upper())
# Using a comprehension to convert a list of names to upper case
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = [cols.upper() for cols in colors]

'''
Reference: https://www.w3resource.com/python-exercises/list/

1. Write a Python program to sum all the items in a list. Go to the editor


2. Write a Python program to multiplies all the items in a list. Go to the editor


3. Write a Python program to get the largest number from a list. Go to the editor


4. Write a Python program to get the smallest number from a list. Go to the editor


5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2


6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


7. Write a Python program to remove duplicates from a list. Go to the editor


8. Write a Python program to check a list is empty or not. Go to the editor


9. Write a Python program to clone or copy a list. Go to the editor


10. Write a Python program to find the list of words that are longer than n from a given list of words. Go to the editor


11. Write a Python function that takes two lists and returns True if they have at least one common member. Go to the editor


12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']


13. Write a Python program to generate a 3*4*6 3D array whose each element is *. Go to the editor


14. Write a Python program to print the numbers of a specified list after removing even numbers from it. Go to the editor


15. Write a Python program to shuffle and print a specified list. Go to the editor


16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). Go to the editor


17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). Go to the editor


18. Write a Python program to generate all permutations of a list in Python. Go to the editor


19. Write a Python program to get the difference between the two lists. Go to the editor


20. Write a Python program access the index of a list. Go to the editor


21. Write a Python program to convert a list of characters into a string. Go to the editor


22. Write a Python program to find the index of an item in a specified list. Go to the editor


23. Write a Python program to flatten a shallow list. Go to the editor


24. Write a Python program to append a list to the second list. Go to the editor


25. Write a Python program to select an item randomly from a list. Go to the editor


26. Write a python program to check whether two lists are circularly identical. Go to the editor


27. Write a Python program to find the second smallest number in a list. Go to the editor


28. Write a Python program to find the second largest number in a list. Go to the editor


29. Write a Python program to get unique values from a list. Go to the editor


30. Write a Python program to get the frequency of the elements in a list. Go to the editor


31. Write a Python program to count the number of elements in a list within a specified range. Go to the editor


32. Write a Python program to check whether a list contains a sublist. Go to the editor


33. Write a Python program to generate all sublists of a list. Go to the editor


34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. Go to the editor
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.


35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


36. Write a Python program to get variable unique identification number or string. Go to the editor


37. Write a Python program to find common items from two lists. Go to the editor


38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]


39. Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
Sample list: [11, 33, 50]
Expected Output: 113350


40. Write a Python program to split a list based on first character of word. Go to the editor


41. Write a Python program to create multiple lists. Go to the editor


42. Write a Python program to find missing and additional values in two lists. Go to the editor
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h


43. Write a Python program to split a list into different variables. Go to the editor


44. Write a Python program to generate groups of five consecutive numbers in a list. Go to the editor


45. Write a Python program to convert a pair of values into a sorted unique array. Go to the editor


46. Write a Python program to select the odd items of a list. Go to the editor


47. Write a Python program to insert an element before each element of a list. Go to the editor


48. Write a Python program to print a nested lists (each list on a new line) using the print() function. Go to the editor


49. Write a Python program to convert list to list of dictionaries. Go to the editor
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


50. Write a Python program to sort a list of nested dictionaries. Go to the editor


51. Write a Python program to split a list every Nth element. Go to the editor
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


52. Write a Python program to compute the difference between two lists. Go to the editor
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']


53. Write a Python program to create a list with infinite elements. Go to the editor


54. Write a Python program to concatenate elements of a list. Go to the editor


55. Write a Python program to remove key values pairs from a list of dictionaries. Go to the editor


56. Write a Python program to convert a string to a list. Go to the editor


57. Write a Python program to check whether all items of a list is equal to a given string. Go to the editor


58. Write a Python program to replace the last element in a list with another list. Go to the editor
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


59. Write a Python program to check whether the n-th element exists in a given list. Go to the editor


60. Write a Python program to find a tuple, the smallest second index value from a list of tuples. Go to the editor


61. Write a Python program to create a list of empty dictionaries. Go to the editor


62. Write a Python program to print a list of space-separated elements. Go to the editor


63. Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


64. Write a Python program to iterate over two lists simultaneously. Go to the editor


65. Write a Python program to access dictionary keys element by index. Go to the editor


66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. Go to the editor
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]


67. Write a Python program to find all the values in a list are greater than a specified number. Go to the editor


68. Write a Python program to extend a list without append. Go to the editor
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]


69. Write a Python program to remove duplicates from a list of lists. Go to the editor
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]


70. Write a Python program to get the depth of a dictionary. Go to the editor


71. Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False


72. Write a Python program to flatten a given nested list structure. Go to the editor
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


73. Write a Python program to remove consecutive duplicates of a given list. Go to the editor
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]


74. Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]


75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4.3, 5, 1]
List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
Original String:
automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]


76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]


77. Write a Python program to decode a run-length encoded given list. Go to the editor
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]


78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])


79. Write a Python program to remove the K'th element from a given list, print the new list. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After removing an element at the kth position of the said list:
[1, 1, 3, 4, 4, 5, 1]


80. Write a Python program to insert an element at a specified position into a given list. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1]


81. Write a Python program to extract a given number of randomly selected elements from a given list. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]


82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. Go to the editor
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]


83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. Go to the editor
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result:
243


84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. Go to the editor
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110


85. Write a Python program to create a multidimensional list (lists of lists) with zeros. Go to the editor
Multidimensional list: [[0, 0], [0, 0], [0, 0]]


86. Write a Python program to create a 3X3 grid with numbers. Go to the editor
3X3 grid with numbers:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
'''














