

import time # whenever I use time.sleep in the future I'm just pausing the program
from random import *

# Ask user for list of items
items_str = input("Please anter a list of items you would like to split into groups. Seperate items using spaces.")
# Split the string of items into a list
items_list = items_str.split(" ")

# Repeats until we get a usable number
while True:
    # Repeats until the user inputs a number
    while True:
        try:
            time.sleep(1)
            num_groups = int(input("How many groups do you want?"))
            time.sleep(1)
            break
        except ValueError:
            time.sleep(1)
            print("Please enter a number. No decimals")

    # make sure num_groups is valid
    if num_groups <= len(items_list):
        # if valid, checks if inputs will split evenly into num_groups
        if len(items_list)%num_groups == 0:
            print("Nice, I'll start randomly assigning your items into groups")
            break
        # else, if it wont split evenly we ask the user if they want to continue anyway
        else:
            ans = input("Your items wont split evenly into that amount of groups. Is that ok?")
            time.sleep(1)
            if str.lower(ans) == "yes" :
                print("Alright, I'll get sorting!")
                break
            elif str.lower(ans) == "no":
                print("Alright, then pick a different number.")
            # if they don't answer yes or no, I just assume they meant no
            else:
                print("I'll take that as a no. Pick a different number")
    else:
        print("You have more groups than items, Please input a different number")


time.sleep(2)

# create an empty list to store groups
groups = []
curr_group = 0

# create a new list to store each group
while curr_group < num_groups:
    # create title for group
    new_list = ["group " + str(curr_group + 1)]
    # add group to list of groups
    groups.append(new_list)
    curr_group += 1

curr_group = 0
rand = 0

# randomly remove inputs from array and add to groups
while len(items_list) > 0:
    rand = randint(0, len(items_list) - 1)
    # get an item from inputs based on the random nunmber and put it into a variable (because I use pop the item we
    # get is deleted from inputs)
    removed = items_list.pop(rand)
    # add removed item to group
    groups[curr_group].append(removed)
    # increment curr_group so it adds to a different group next time
    curr_group += 1
    if curr_group == num_groups:
        curr_group = 0

# so I found out that if you do for n in list it will run once for every item in the list, and in each run n = that
# item in the list

# so I go through the groups
for group in groups:
    # then in each group I go through the items
    for item in group:
        # and print them
        print(item)
        time.sleep(0.5)
    # after printing the contents of each group I print a space so the groups are seperated
    print(" ")