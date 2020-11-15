x = '1010101'

def tr(x):
	e=len(x)
	c=0
	while c!=e:
		n=x[c]
		c+=1
		f=n*2
	
	
def bin2dec(x):
	num = int(x[0])
	for i in range(1, len(x)):
		num = num*2+int(x[i])
	return num

if __name__ == "__main__":
	print(bin2dec(x))
