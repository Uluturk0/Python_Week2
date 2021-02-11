'''
Developer: Ömer ULUTÜRK
Date: 10.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). 
Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

Example:

Inputs>>> [1, 2, 3, 4, 5], 2

Output>>> [4, 5, 1, 2, 3]

Inputs>>> [1, 2, 3, 4, 5], -2

Output>>> [3, 4, 5, 1, 2]
'''

mylist = list(input("Please enter one list:      "))
num = int(input("Please enter one number for shifting (+) or (-) :      "))
print(mylist, num)
mylist= ' '.join(mylist[-num:] + mylist[:-num])
print(mylist)
 
