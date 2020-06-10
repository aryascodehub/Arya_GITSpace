# 3 : Write a Python program to display the first and last colors from the following list.
# Example : color_list = ["Red","Green","White" ,"Black"].
# Your list should be flexible such that it displays any color that is part of the list.
from typing import List

color_list = ["Red", "Green", "White", "Black", "Pink", "Azure", "Brown"]
newColorlist = color_list[0]
finalColorlist = color_list[len(color_list) - 1]

print(newColorlist + finalColorlist)
