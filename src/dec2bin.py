n = 10

def dex2bin(x):
	str1 = ""
	while x!=0:
		y= x%2
		x= int(x/2)
		str1+=str(y)
	print(str1[::-1])

if __name__ == "__main__":
	dex2bin(n)
