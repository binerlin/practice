def prime_numbers():

	def remainder(num):
		if num % 2 == 0:
			return False

		elif num % 3 == 0:
			return False

		elif num % 5 == 0:
			return False

		elif num % 7 == 0:
			return False

		else:
			return True

	Primes = [2, 3, 5, 7]
	numberList = [i for i in range(2,101)]
	
	for i in numberList:
		if remainder(i):
			Primes.append(i)

	return Primes

