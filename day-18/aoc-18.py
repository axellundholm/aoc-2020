import operator

OPS = {'+': operator.add, '*': operator.mul}

def is_num(number):
	try:
		int(number)
		return True
	except ValueError:
		return False

def cleanup(eq):
	clean = []
	i = 0
	while i < len(eq):
		print("clean = " + str(clean))
		current = eq[i]
		if is_num(current):
			print("num")
			clean.append(int(current))
			if i == len(eq)-1: 
				print("Last!")
				return clean, i

		elif current == "(":
			print("front")
			print("eq[i+1:] = " + str(eq[i:]))
			sub_clean, sub_i = cleanup(eq[i+1:-1])
			print("sub_clean = " + str(sub_clean))
			clean.append(sub_clean)
			i += sub_i

		elif current == ")":
			print("back")
			return clean, i

		else:
			print("ops")
			clean.append(current)

		i += 1


def calc(eq):
	stack = []
	res = 0
	print eq
	for i in eq:
		print("Current char :", i)
		if isinstance(i, list):
			stack.insert(0, calc(i))
		
		elif is_num(i):
			stack.insert(0, i)

		elif i in ["+", "*"]:
			stack.insert(0, i)

		if len(stack) == 3:
			print("Pre op stack: ", stack)
			n1 = stack.pop(0)
			n2 = stack.pop(1)
			res = OPS[stack.pop(0)](n1, n2)
			stack.insert(0, res)
			print("Post op stack: ", stack)
		
	return res

if __name__ == "__main__":

	f = open('input-18.txt', 'r')

	l = f.readlines()
	l = [cleanup(x.strip().replace(" ", ""))[0] for x in l]
	
	# ltest = ["2 * 3 + (4 * 5)",								# 26
	# 	"5 + (8 * 3 + 9 + 3 * 4 * 3)",						# 437
	# 	"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",		# 12240
	# 	((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]	# 13632
	
	ltest = ["(1 + 2) + 3"]
	
	ltest = [cleanup(x.strip().replace(" ", ""))[0] for x in ltest]
	
	print ltest[0]
	# print ltest[1]
	# print ltest[2]
	# print ltest[3]
	#print(calc(ltest[3]))
	
	# ans = [calc(x) for x in ltest]
	# print(ans)	

	
	# ltest = ["1 + 2 + 3 * 4 + (5 * 5)\n", "5 + 7\n"]
	# print(ltest)
	# ltest = [cleanup(x.strip().replace(" ", ""))[0] for x in ltest]
	# print(ltest)

	
	# ans = sum([calc(x) for x in l])
	# print("Ans = ", ans)