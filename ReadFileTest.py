# Python program to
# demonstrate readline()
MAX_LINE_COUNTS = 200
LINE_DIVIDER = 10

# Writing to a file
file1 = open('splitfile.csv', 'w')
file1.writelines((L))
file1.close()

# Using readline()
file1 = open('Recirkviz.CSV', 'r')
count = 0

temp = file1.read().splitlines()
write_iter = iter(temp)
for x in write_iter:

	count = count + 1
	if ((count % LINE_DIVIDER) == 0):
		print(count, " : ", x)


#while True:
#	count += 1

	# Get next line from file
#	line = file1.readline()

	# if line is empty
	# end of file is reached
#	if not line or count > MAX_LINE_COUNTS :
#		break

#	print("Line{}: {}".format(count, line))

file1.close()
