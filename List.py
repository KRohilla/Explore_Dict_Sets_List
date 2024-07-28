"""
*** Python lists ***
Lists are ordered collection of data items.
The items are separated by commas and enclosed within square brackets [].
Lists are mutables. A single list can contain items of different data types.
"""

details = ["Hello", 18, "World", 9.8]
print(details)

# List Methods
# 1. list.sort() --> This method sorts the list in ascending order. The original list is updated
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print("Sorted items --> ", num)

# 2. reverse() --> This method reverses the order of the list.
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print("Reversed list --> ", colors)

# 3. index() --> This method returns the index of the first occurrence of the list item.
print("Index of green in list --> ", colors.index("green"))

# 4. count() --> Returns the count of the number of items with the given value.
colors = ["voilet", "green", "indigo", "blue", "green"]
print("Count of Green Color in list", colors.count("green"))

# 5. append() --> This method appends items to the end of the existing list.
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print("After Append method --> ", colors)

# 6. insert() --> This method inserts an item at the given index. 
colors.insert(1, "green")   #inserts item at index 1
print("Adding Green in list at index 1 --> ", colors)

# 7. extend() --> This method adds an entire list or any other collection datatype(set, tuple, dictionary)to the existing list.
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print("Extending the rainbow to colors --> ", colors)
