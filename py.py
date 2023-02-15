
x = 5
n = 1
for y in x:
	n = 2*n -1


a1 = int(52)
a2 = int(49)
d = a2 - a1
print(d)

a30 = a1 - d * 29
print(a30)

a50 = a1 - d * 49
print(a50)


a30 = 100
d  = 3

while a30 == 280:
	n280 = a30 + d

def fib2(num):
	a, b = 1, 1
	for _ in range(num - 1):
		a, b = b, a + b
	return a

print(fib2(10))