class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Lorem", 2000)
emp2 = Employee("Ipsum", 5000)

emp1.displayEmployee()
print("Total Employee %d" % Employee.empCount)

# setter and getter of python classes
setattr(emp1, 'designation', 'developer')
print(getattr(emp1, 'designation'))



# Class Inheritance

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


# Private Members
print('Private Members')
class JustCounter:
    __secretCount = 0
    counter = 0
    
    def privateCount(self):
        self.__secretCount += 1
        self.counter += 3
        print ('private = ', self.__secretCount)
        print ('counter = ', self.counter)

counter = JustCounter()
counter.privateCount()
counter.privateCount()
print (counter.counter)
# AttributeError: 'JustCounter' object has no attribute '__secretCount' of the below
#print (counter.__secretCount) 

