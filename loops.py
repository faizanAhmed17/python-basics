fruits = ['Mango', 'Banana', 'Orange', 'Apple']

# demonstration of for loop
for fruit in fruits:
  print(fruit)



my_num = 0

# demonstration of while loop
while my_num < 10:
  print(my_num)
  my_num+=1



# range function
for i in range(5):
    print(i)

# another range example 
for i in range(0, 10, 3):
   print(i)

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])