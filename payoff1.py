#!usr/bin/eny python3
# -*- coding: utf-8 -*-

# print your current balance per month and minimum monthly payment.
# parameter balance should be give and set two default parameters:
# annual interest rate, monythly payment rate 

def creditcard_pay_off(balance, annualInterestRate = 0.2, monthlyPaymentRate = 0.04):
	Month = 0
	Total_pay = 0
	for i in range(12):
		Month = Month + 1
		Mini_month_pay = balance * monthlyPaymentRate
		Total_pay = Total_pay + Mini_month_pay
		balance = balance - Mini_month_pay
		interest = annualInterestRate/12 * balance
		balance = balance + interest
		print('Month: %s' % Month)
		print('Minimum monthly payment: %.2f' % Mini_month_pay)
		print('Remaining balance: %.2f' % balance)
	print('Total paid: %.2f' % Total_pay)
	print('Remaining balance: %.2f' % balance)

creditcard_pay_off(4213)



