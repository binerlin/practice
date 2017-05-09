#!usr/bin/eny python3
# -*- coding: utf-8 -*-

def fastpay(balance, annualInterestRate, accuracy=0.01):
	'''
	Function to get the lowest payment that accuracy is 0.01

	Example:
	>>> fastpay(320000, 0.2)
	Lowest Payment: 29157.09
	>>> fastpay(999999, 0.18)
	Lowest Payment: 90325.03
	'''
	rate = annualInterestRate / 12
	min = balance / 12
	max = balance * (1+rate)**12 / 12
	while True:
		# get the outside balance after pay a annual year
		base = balance
		pay = (max+min) / 2
		for i in range(12):
			base = base - pay
			base = base * (1+rate)

		# list every condition
		if base > 0:
			min = (max+min) / 2

		if base < 0:
			max = (max+min) / 2
			if not(max - min) > accuracy:
				print('Lowest Payment: %.2f' % pay)
				break

		if base == 0:
			pay = round(pay, 2)
			print('Lowest Payment: %.2f' % pay)
			break

if __name__=='__main__':
	import doctest
	doctest.testmod()
