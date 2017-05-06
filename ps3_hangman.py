# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	with open(WORDLIST_FILENAME, 'r') as inFile:
		wordlist = inFile.readline()
	# wordlist: list of strings
	wordlist = wordlist.split()
	print(len(wordlist), "words loaded.")
	return wordlist

def chooseWord(wordlist):
	"""
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
	  False otherwise
	'''
	# FILL IN YOUR CODE HERE...
	for i in secretWord:
		if not(i in lettersGuessed):
			return False
	return True



def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
	  what letters in secretWord have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE...
	curstr = ''
	for i in secretWord:
		if i in lettersGuessed:
			curstr = curstr + i
		else:
			curstr = curstr + '_ '

	return curstr



def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	  yet been guessed.
	'''
	# FILL IN YOUR CODE HERE...
	# csl means that current strings left 
	# which are letters in alphabetical order 
	# between 'a' and 'z' have been not guessed
	csl = string.ascii_lowercase
	for i in lettersGuessed:
		csl = csl.split(i)[0] + csl.split(i)[1]

	return csl
	

def hangman(secretWord):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many 
	  letters the secretWord contains.

	* Ask the user to supply one guess (i.e. letter) per round.

	* The user should receive feedback immediately after each guess 
	  about whether their guess appears in the computers word.

	* After each round, you should also display to the user the 
	  partially guessed word so far, as well as letters that the 
	  user has not yet guessed.

	Follows the other limitations detailed in the problem write-up.
	'''
	# FILL IN YOUR CODE HERE...
	gnum = 8
	print('Welcome to the game, Hangman!')
	print('I am thinking of a word that is %s letters long.' % len(secretWord))

	# GAME START
	lettersGuessed = []
	csl = getAvailableLetters(lettersGuessed)
	curstr = getGuessedWord(secretWord, lettersGuessed)
	
	while True:

		# MISSION COMPLETED
		if len(curstr) == len(secretWord):
			print('Congratulations, you won!')
			break

		# MISSION FAILED
		if gnum == 0:
			print('Sorry, you ran out of guesses. The word was %s' % secretWord)
			break

		# MAIN BODY CODE
		print('You have %d guesses left.' % gnum)
		print('Available Letters: %s' % csl)
		guessletter = (str(input('Please guess a letter: '))).lower()
		
		if guessletter in lettersGuessed: # if guesses repeated
			print("Oop! You've already guessed that letter: %s" % curstr)
			print('------------')
		
		if not(guessletter in lettersGuessed):
			lettersGuessed.append(guessletter)
			if guessletter in secretWord: # if guesses rightly
				csl = getAvailableLetters(lettersGuessed) 
				curstr = getGuessedWord(secretWord, lettersGuessed)			
				print('Good guess: %s' % curstr)
				print('------------')

			if not(guessletter in secretWord): # if guesses wrongly
				gnum =  gnum - 1
				csl = getAvailableLetters(lettersGuessed)
				curstr = getGuessedWord(secretWord, lettersGuessed)
				print('Oop! That letter is not in my word: %s' % curstr)
				print('------------')




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
