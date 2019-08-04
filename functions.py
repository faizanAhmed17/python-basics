# Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Prints a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# functions doc string
print(fib.__doc__)

# Now call the function we just defined:
fib(2000)

# FUNCTION ARGUMENTS

# Positional
def my_func_pos(x,y):
  print(x+y)

my_func_pos(3,2)


# Keyword
def my_func_key(name='', age=0):
  print('He is %s and his age is %s' % (name,age))

my_func_key(age=50, name='John')


# Positional + Keyword
def func(text, prefix):
  print('%s %s' % (prefix,text))

func('John', prefix='Mr.')

# Arbitrary Arguments

def some_func(*args, **kwargs):
    '''
    First print all arguments than all keyword arguments
    '''
    print('All Arguments')
    for arg in args:
        print(arg) 
    
    print('All Keyword Arguments with Values')
    for key, value in kwargs.items():
        print('%s: %s' % (key,value))


some_func(1,2,'lorem', month='full stack', localtion='Audi')