# Write a Python program to get a string made of the first 2 and the last 2 chars from a given  string.
# If the string length is less than 2, return instead of the empty string.

intro = str(input('''Please enter a string that is at least more than 2 characters:'''))

if len(intro) <= 2:
    print('STOP IT SILLY BOY! - Be sure to enter more than 2 characters next time...')
else:
    print("...and the answer is...." + intro[0:2] + intro[-2:len(intro)])  # negative indexing and slicing is used in
    # this
    print("Thank you for using my program!")
