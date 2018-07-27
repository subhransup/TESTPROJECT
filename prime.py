def is_prime(number):
	if number in (0, 1):
		return False
	if number < 0:
		return False
	for element in range (2, number):
		if number % element == 0:
			return False
	return True

#print is_prime(7)
def next_prime (number):
	index = number
	while True:
		index += 1
	 	if is_prime(index):
			print(index)
			break
#print is_prime(5)
#print next_prime(5)
