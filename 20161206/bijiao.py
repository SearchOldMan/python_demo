# def bijiao(a,b,c):
# 	max = a;
# 	if a>b:
# 		if b>c:
# 			return max
# 		elif a>c:
# 			return max
# 		else:
# 			max = c
# 	elif a>c:
# 		if c>b:
# 			return max
# 		elif a>b:
# 			return max
# 		else:
# 			max= b
# 	else:
# 		if b>c:
# 			max=b
# 		else:
# 			max = c
# 	return max


# print bijiao(1444,335,444)

def bijiao(*t):
	l = list(t)
	return l


l = bijiao(123,345,444)
print l.sort()


