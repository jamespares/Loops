# Compulsory Task 1
'''
define variable (star = '*')
create for loop with range as big as lines/outputs (10)
	if the units in the loop are less than or equal to five
		print that many stars
	else
		deduct the larger units 6-9 numbers from 10 and create that many stars for the rest of the loop
'''

# get variables
star = '*'

for i in range(1, 10): # 1-10 so the loop iterates enough to cover the full pattern
    if i <= 5:
        print( star * i) # this will print iteratively more stars until there are 5
    else:
        print(star * (10 - i)) # this will iteratively deduct 6 to 9 from 10 and create that many stars leading to a decrease