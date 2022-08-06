def print_num(i):
    if i >= 0:
        print_num(i - 1)
        print(i, end = ' ')

print_num(150)

def getMultiples(num, number_of_multiples):
	i = 0
	while i <= number_of_multiples:
		print(num*i)
		i += 1
getMultiples(5, 200)

def print_num1(i):
    for i in range(1, 100+1):
        print(i)
        if(i%5==0):
            print("Coding")
        elif(i%10==0):
            print("Coding Dojo")
print_num1(100)

maximum = 500000
Oddtotal = 0

for number in range(1, maximum+1):
    if(number % 2 != 0):
        Oddtotal = Oddtotal + number

print(Oddtotal) 


count = 2018
while count >= 0:
    print(count)
    count = count - 4

def findMultiples(x):
    for i in range(1, x + 1):
        if i % 3 == 0:
            print(i)

findMultiples(9)