def two():
	for i in l:
		for n in l:
			if i + n == 2020:
				return i * n
def three():
	for i in l:
		for n in l:
			for m in l:
				if i + n + m == 2020:
					return i * n * m


if __name__=="__main__":
	f = open('input-1.txt', 'r')
	
	l = f.readlines()
	l = [int(x.strip()) for x in l]
	
	print(two())
	print(three())