# Dictionary in Python
my_dict = {
  'month': 'full stack',
  'technology': 'Python',
  'head count': 10
  }

# Accessing the value from key
print(my_dict['month'])


# adding the key: value pair in the dict
my_dict['location'] = 'Audi'
print(my_dict)


# Deleting single key:value
del my_dict['month']
print(my_dict)


# Remove all entries
my_dict.clear()
print('my_dict: ',my_dict)


# Looping on dictionary
for k,v in my_dict.items():
      print(k,':',v)

# Delete entire dictionary
del my_dict
print('my_dict : ', my_dict)
