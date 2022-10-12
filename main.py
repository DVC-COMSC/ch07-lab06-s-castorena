# Sarah castorena
# SID 
inputvalues = input('Enter all elements: ')
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 
numbers2 = []
for i in range(len(numbers1)):
    x = numbers1.pop()
    numbers2.append(x)
print(numbers1)
print(numbers2)

# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
