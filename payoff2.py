#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Lowers Payment means that monthly payment are same per month.
# As while, the lowers payment is an interger and must be a multuple of $10.
# the parameters contain the initial balance and annual interest rate 
# At the end, balance should be less than total payment.

def lowest_pay(balance, rate):
	# 'i' is the multiples of $10 which equals payments divide 10 
	i = 0
	base = 0
	while True:
		if base < 0:
			break

		i = i + 1
		payment = i * 10
		base = balance
		for n in range(12):
			base = base - payment
			base = round(base * (1+rate/12), 1)

	print('Lowest Payment: %s' % payment)



