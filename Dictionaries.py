"""
Python Dictionaries
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
"""
info = {'name':'Kritika', 'age':19, 'student':True, 'graduated':True,
        'last_name':'Rohila'}
print("Dictionaries --> ", info)

# Dictionary Methods
# update() --> updates the value of the key provided to it if the item already exists in the dictionary,
# else it creates a new key-value pair.
info.update({'age':21})
info.update({'DOB':2003})
print("Dictionary after using the update() methods --> ", info)

# pop() --> removes the key-value pair whose key is passed as a parameter.
info.pop('student')
print("Removing the key-value pair from the dictionary using the pop() methods --> ", info)

# popitem() --> removes the last key-value pair from the dictionary.
info.popitem()
print("Removing the key-value pair from the dictionary using the popitem()  methods --> ", info)

# clear() --> removes all the items from the list.
info1 = info.copy()
info1.clear()
print("Clearing all the items of dictionary1 using the clear() methods --> ", info1)

# del --> del keyword to remove a dictionary item.
del info1
del info['age']  # deleting the key('DOB') from the dictionary
print("Deleting the key('age') from the dictionary using the del methods --> ", info)
