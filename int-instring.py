import re
str = raw_input("enter a string")
numbers = re.findall('\d+', str)
numbers = map(int,numbers)
print numbers
print max(numbers)
