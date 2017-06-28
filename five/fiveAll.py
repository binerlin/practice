import string

def valid_password(pwd):
	lettersMatch = string.ascii_uppercase + string.ascii_lowercase
	digitsMatch = string.digits
	underline = '_'
	validRange = lettersMatch + digitsMatch + underline

	for letter in pwd:
		if not(letter in validRange):
			return False

	if len(pwd) < 2 or len(pwd) > 10:
		return False
	
	elif not(pwd[0] in lettersMatch):
		return False

	elif pwd[-1] == '_':
		return False

	else:
		return True


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


def letter_count(str):
	
	lettersDict = {}
	lowerStr = str.lower()
	
	for letter in lowerStr:
		if lettersDict.get(letter, -1) == -1:
			lettersDict[letter] = 1

		else:
			lettersDict[letter] = lettersDict[letter] + 1

	lettersCount = []
	
	for letter, count in lettersDict.items():
		tuple = (letter, count)
		lettersCount.append(tuple)

	return lettersCount

def cap_string(str):

	wordsList = str.split()
	capStringList = []
	for word in wordsList:
		word = word[0].upper() + word[1:]
		capStringList.append(word)

	capString = ' '.join(capStringList)

	return capString


class Queue(object):

	def __init__(self):
		self.Queue = []

	def enqueue(self, order):
		self.Queue.append(order)

	def dequeue(self):
		return self.Queue.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue()) 
print(q.dequeue()) 