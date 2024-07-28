"""
Sets are unordered collection of data items.
The items are separated by commas and enclosed within curly brackets {}.
Sets do not contain duplicate items.
"""
s1 = {"Kritika", 'A', True, 1,2,3,4.2,3}
print("Set --> ", s1)

set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}

# Set Methods
# isdisjoint() --> it checks if items of given set are present in another set.
print("isdisjoing -->  ",set1.issubset(set2))

# issuperset() --> checks if all the items of a particular set are present in the original set.
print("isuperset -->  ", set1.issuperset(set2))

# issubset() --> checks if all the items of the original set are present in the particular set..
print("issubset -->  ", set1.issubset(set2))

# add() --> add a single item to the set
set1.add("India")
print("add -->  ", set1)

# update() --> for adding more than one item in the set
set3 = {"F", "A", "G"}
set1.update(set3)
print("update --> ", set1)

# remove()/discard() --> methods to remove items from list.
set1.remove("G")
print("remove() --> ", set1)
set1.discard("F")
print("discard() --> ", set1)

# pop() --> removes the last item of the set
deleted = set1.pop()
print("Deleted Item --> ", deleted)
print("pop() --> ", set2)

# clear() --> clears all items in the set and prints an empty set.
set3.clear()
print("clear() :: ", set3)
