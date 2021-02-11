'''
Write a program that takes in two words as input and returns a list containing three elements, in the following order:

Shared letters between two words. Letters unique to word 1. Letters unique to word 2. 
Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations. 
The strings will always be in lowercase and will not contain any punctuation.

Example:

Input1>>> "sharp"

Input2>>> "soap"

Output>>> ['aps', 'hr', 'o']
'''
import string
first_word  = set(input("Please write your 1. word:      ").lower())
second_word = set(input("Please write your 2. word:      ").lower())
exclude = set(string.punctuation)

intersection = sorted(first_word & second_word)
intersection = ''.join(intersection)
unique1 = sorted(first_word - second_word)
unique1 = ''.join(unique1)
unique2 = sorted(second_word - first_word)
unique2 = ''.join(unique2)
first_word = ''.join(ch for ch in first_word if ch not in exclude)
second_word = ''.join(ch for ch in first_word if ch not in exclude)
'''yukarıdaki iki satır yerine bu şekilde de yazabilirdik:'''
# intersection.translate(str.maketrans('', '', string.punctuation))
# unique1.translate(str.maketrans('', '', string.punctuation))
# unique2.translate(str.maketrans('', '', string.punctuation))
second_word =  ''.join(ch for ch in second_word if ch not in exclude)
mylist = [intersection,unique1,unique2]
print(mylist)
