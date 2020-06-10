# # 6 : Write a Python program to add 'ing' at the end of a given string (length should be at least 3). #If the given
# string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged. #Sample String : 'abc' and Expected Result : 'abcing'. Another sample String : 'string' and
# expected result : 'stringly'

userInput = str(input("Dear user, please enter a string that is greater than 3 characters...."))

isChanged = False #this is a variable to determine if the string had to undergo a change or not...

# Determine if string ends with 'ing'. If it does, then please add 'ly'. Also need to ensure that if string is less
# than 3, then don't even change the value of the variable

if len(userInput) >= 3:
    isChanged = True
    if "ing" in userInput:
        userInput = userInput + "ly"  # then append ly
    else:
        userInput = userInput + "ing"

if isChanged:
    print("This is your new file with changes \n\n" + userInput)
else:
    print("Sorry, there was no change to the string you gave me...")