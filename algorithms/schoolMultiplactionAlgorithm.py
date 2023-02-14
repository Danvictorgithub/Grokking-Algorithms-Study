# School Multiplication Algorithm
def algorithm_multiply(num1_array,num2_array,results_array):
		if len(num2_array) == 0:
			return results_array
		else:
			constant = 0
			digit = num2_array.pop()
			total =[]
			# print(f"the digit is {digit}")
			for i in range(len(num1_array)):
				result = digit*num1_array[i]+constant
				constant = 0
				# print(f"{digit}x{num1_array[i]} = {result}")
				if i != len(num1_array)-1:
					if result >= 10:
						constant = [int(i) for i in str(result)][0]
						result = [int(i) for i in str(result)][1]
						# print(result)
						total.append(result)
					else:
						total.append(result)
				else:
					total.append(result)
			total.reverse()
			over_all_total = int("".join([str(i) for i in total]))
			results_array.append(over_all_total*10**len(results_array))
			return algorithm_multiply(num1_array,num2_array,results_array)

    # return result
def algorithm_multiply_add(results_array):
	result = 0
	for i in range(len(results_array)):
		print(results_array[i])
		result += results_array[i]
	print("-----------------")
	return result
def school_multiplication(num1, num2):
	print(f"  {num1}\nx {num2}\n-----------------")
	num1 = [int(i) for i in str(num1)]
	num2 = [int(i) for i in str(num2)]
	if (len(num1) < len(num2)):
		num1,num2 = num2,num1
	num1.reverse()
	results_array = []
	results_array = algorithm_multiply(num1,num2,results_array)
	result = algorithm_multiply_add(results_array)
	print(result)
	return result
school_multiplication(69,420)
# school_multiplication(num1,num2) => (integer) result
# 	:split num1
# 	:split num2
# 	:recursively multiply num1[i] to num2[j]
# 	:and if the result is greater than or equal 10
# 	:get the leading digit to a variable named constant
#   :if all number is exhausted and provided with a result
#   :add all result and return the value

#   1
#   25
# x 12
# ----
#  	50
#  250
# ----
#  300
