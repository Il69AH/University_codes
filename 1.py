def h(q0, q1, x):
	return q0 + q1*x

def cost_func(x_arr, y_arr, q0, q1, proizvodnaya=True, x_mark=False):
	result = 0
	for i in range(len(x_arr)):
		if proizvodnaya:
			if x_mark:
				result += (h(q0, q1, x_arr[i]) - y_arr[i])*x_arr[i]
			else:
				result += (h(q0, q1, x_arr[i]) - y_arr[i])
		else:
			result += (h(q0, q1, x_arr[i]) - y_arr[i])**2
	return result/len(x_arr) if proizvodnaya else result/(2*len(x_arr))

def regression(file):
	x_arr, y_arr = [], []
	q0, q1 = 0, 0
	N = 1500
	a = 0.01
	list_of_3 = []
	f = open(file)
	for line in f:
		temp = line.split(',')
		x_arr.append(float(temp[0]))
		y_arr.append(float(temp[1]))
	for i in range(N):
		new_q0 = q0 - a*cost_func(x_arr, y_arr, q0, q1)
		new_q1 = q1 - a*cost_func(x_arr, y_arr, q0, q1, x_mark=True)
		if abs(cost_func(x_arr, y_arr, new_q0, new_q1, proizvodnaya=False)) < abs(cost_func(x_arr, y_arr, q0, q1,proizvodnaya=False)):
			q0, q1 = new_q0, new_q1
		else:
			new_q0 = q0 + a*cost_func(x_arr, y_arr, q0, q1)
			new_q1 = q1 + a*cost_func(x_arr, y_arr, q0, q1, x_mark=True)
			if abs(cost_func(x_arr, y_arr, new_q0, new_q1, proizvodnaya=False)) < abs(cost_func(x_arr, y_arr, q0, q1, proizvodnaya=False)):
				q0, q1 = new_q0, new_q1
		if i > N - 4:
			list_of_3.append(cost_func(x_arr, y_arr, q0, q1, proizvodnaya=False))
	return q0, q1, list_of_3
	f.close()

def main():
	q0, q1, last_3_res_of_cost_func = regression('regression.txt') 
	print(round(q0, 4), round(q1,4))
	print(' '.join([str(round(i, 8)) for i in last_3_res_of_cost_func]))


if __name__ == '__main__':
    main()