# Create an empty list
my_list = []

# Add items to the list

my_list.append("10")
my_list.append("20")
my_list.append("30")
my_list.append("40")


my_list.insert(1, "15")  # Insert "15" at index 1
my_list.extend(["50", "60","70"])  # Extend the list with multiple items

my_list.remove("70")  # Remove "70" from the list

my_list.sort()  # Sort the list in ascending order


my_list = [10, 15, 20, 30, 40, 50,60]

index_of_30 = my_list.index(30)  # Find the index of the item "30"

print("The index of 30 is at index:", index_of_30)

