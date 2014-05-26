#run either the while or the for-loop

i = 10 + 2
j = 1000
series = []

# while i < j:
# 	print 'We are counting up the amount of organisms genome we have sequenced this week. The most interesting experients are number: %d. Please check them out.' % i
# 	series.append(i)
# 	i += 5 ** 3
# 	print 'The numbers are now: ', series
# 	print 'At the bottom i is %d' % i

series1 = []
for k in range(i, j):
	print 'We are counting up the amount of organisms genome we have sequenced this week. The most interesting experients are number: %d. Please check them out now.' % k
	series1.append(k)
	print 'The numbers are now: ', series1
	print 'At the bottom i is %d' % k