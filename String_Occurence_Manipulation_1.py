# Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself
tmpStr = input("Enter a phrase here: ")
tmpFirstChar = tmpStr[0]  # tmpFirstChar stores "e"
# correct the below line please...
tmpDollar = tmpStr.replace(tmpFirstChar, "$") #$llh$llh$llsss
tmpWandro = tmpDollar[1:len(tmpDollar)] #llh$llh$llsss
tmpFinal = tmpFirstChar + tmpWandro

print(tmpFinal)
