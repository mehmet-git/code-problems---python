"""

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""



import sys

# Given array <feel free to change> 
numbers = [10,2,3,7,8]

# The number that we look in the array. I want to input but you change that.
k = int(input("Number Enter  : "))

# Number for algorithm.
i = 1


# algorithm started here.
for n in range(int(k/2)):	
	for number in numbers:				
		if i == number:
			for number2 in numbers:
				if k-i == number2:
					print(f" FOUND !! {k} = {i} + {k-i}")
					sys.exit()
	i = i+1
print("NOT FOUND !!")

# algorithm finished here.