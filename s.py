#/usr/bin/env python3
# -*- coding: utf-8 -*-

# select all the letters in alphabetical order and put them together
s = 'zyxwvutsrqponmlkjihgfedcba'
a = ''
for i in range(len(s)-2):
	if not s[i] > s[i+1]:
		a = a + s[i]
		if s[i+1] > s[i+2]:
			a = a + s[i+1]

if not s[-1] < s[-2]:
	a = a + s[-2] + s[-1]

if len(a) == 0:
	l = s[0]
	print('Longest substring in alphabetical order is: %s' % l)

else:
	# split them as strings and put them in a list 
	n, d, L, L1 = 0, {}, [], []
	d[n] = ''
	for i in range(len(a)-1):
		d[n] = d[n] + a[i]
		if a[i] > a[i+1]:
			L.append(d[n])
			L1.append(len(d[n]))
			n = n + 1
			d[n] = ''	

	d[n] = d[n] + a[-1]
	L.append(d[n])
	L1.append(len(d[n]))

	# select the longest string and print
	n = max(L1)
	L2 = []
	for i in L:
		if len(i) == n:
			L2.append(i)

	l = max(L2)

	print('Longest substring in alphabetical order is: %s' % l)
