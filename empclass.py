class Employee:
	'Common base class for all Employees'
	empCount = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	def dispalyCount(self):
		print "TOTALA EMPLOYEE %d" % Employee.empCount
	def displayEmployee(self):
		print "name:", self.name, "salary:", self.salary

class jobtype(Employee):
	def __init__(self,name, salary, jtype):
		Employee.__init__(self,name,salary)
		self.jtype = jtype
		Employee.displayEmployee(self)
	def displayjobtype(self):
		return "name:", self.name, "salary:", self.salary, "Job Type:" , self.jtype 

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

#emp1 = Employee("Subhransu", 5000)
typ1 = jobtype("biki", 3000, "Temp")
typ1.displayjobtype()
#emp1.displayEmployee()
print "Total Employee %d" % Employee.empCount
