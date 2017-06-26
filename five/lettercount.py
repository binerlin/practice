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


