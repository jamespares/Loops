# Compulsory Task 1
'''
get user to input number
repeat until user enters -1
average all the values inputted excluding -1
'''

#define sum and count for average
sum_num = 0
count = 0

#get user to input number
num = int(input('Please enter a number between -10 and 10: '))

# create loop
while num != -1:
     sum_num += num # sum values for average
     count += 1 # count values for average

     num = int(input('Please enter a number between -10 and 10: ')) # get number again

if count > 0:  # will only be executed if the while loop breaks. excludes -1.
     avg_num = sum_num / count  # calculate average
     print('You got it. Average of values entered is ', avg_num,'(',sum_num,'/',count,')') # print average with calculation

else:
     print('Well done. You guessed first time!')


