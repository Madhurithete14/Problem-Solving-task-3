# To find the sum of the first and last digit of an integer
number = 1274
 

number = str(number)
 

first_digit = int(number[0])
last_digit = int(number[-1])
 

addition = first_digit + last_digit
 

print('Addition of first and last digit of the number is', 
      addition)