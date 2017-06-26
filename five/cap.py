def cap_string(str):

	wordsList = str.split()
	capStringList = []
	for word in wordsList:
		word = word[0].upper() + word[1:]
		capStringList.append(word)

	capString = ' '.join(capStringList)

	return capString
