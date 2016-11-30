
def fact(n):
	return fact_ater(n,1)
def fact_ater(num,result):
	if num == 1:
		return result
	else:
		return fact_ater(num-1,num*result)


print(fact(5))