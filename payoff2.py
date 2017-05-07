#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Lowers Payment means that monthly payment are same per month.
# As while, the lowers payment is an interger and must be a multuple of $10.
# the parameters contain the initial balance and annual interest rate 
# At the end, balance should be less than total payment.

def lowers_pay(balance, annualInterestRate):
	# 'i' is the multiples of $10 which equals payments divide 10 
	i = 0
	totalpay = 0
	
	while True:
		# get the lowers payment
		if totalpay >= balance:
			return payment
			break
		# 'n' is the number that count of month
		n = 0
		i = i + 1
		payment = 10 * i
		totalpay = payment * 12
		 
		while True:
			# get the latest balance
			if n = 13:
				break
			
			n = n + 1
			balance = balance - payment
			balance = balance + balance * (annualInterestRate/12)
