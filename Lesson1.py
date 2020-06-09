# Program that takes a three digit number and reverses the order
# Author: Arya Shah
# A Input Project


num = int(input("Please enter a three digit number:"))  # This takes the user's input and uses it to form the number
a = int(num % 10)  # This gives us the ones digit in the number
temp = int(num // 10)
b = (temp % 10)  # This calculates the modulus to use to extract the second digit
c = (temp // 10)
number = str(a) + str(b) + str(c)  # These digits need to be converted into strings before going into the print
print("Your new number will be " + str(int(number)))

