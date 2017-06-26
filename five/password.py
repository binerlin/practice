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
