# Instructions and Answers

# Create an empty list called my_list.

my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print(my_list) #printing my list to see if the values where appended correctly

# Insert the value 15 at the second position in the list.
my_list= [10, 20, 30, 40]
my_list.insert(1, 15)
#print(my_list)

# Extend my_list with another list: [50, 60, 70].
my_list = [10, 20, 30, 40]
new_list = [50, 60, 70]
my_list.extend(new_list)
#print(my_list)


# Remove the last element from my_list.

my_list.pop(-1)
#print(my_list)

# Sort my_list in ascending order.
my_list = sorted(my_list, reverse= True)
#print(my_list)

# Find and print the index of the value 30 in my_list.
print(my_list[3]) # please note that this code was written with the list in the reverse or ascending order of the previous question