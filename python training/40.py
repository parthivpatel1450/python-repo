num=1000
print("prime factor for =", num)
d=2

while num>1:
	if num%d==0:
		print(d)
		num=num/d
		continue
	d=d+1