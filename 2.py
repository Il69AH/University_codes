from functools import reduce
from time import sleep
class Graph(object):
	def __init__(self):
		pass

	def loadfromfile(self, name):
		self.dictionary = dict()
		f = open(name)
		self.amountOfPoints = int(f.readline())
		self.massive = [[i for i in range(self.amountOfPoints)] for j in range(self.amountOfPoints)]
		string = f.readline().split(', ')
		for point in string:
			tempString = ''
			for i in range(len(point)):
				if i > point.index(':'):
					tempString += point[i]
			self.dictionary[str(string.index(point))] = tempString.strip()
		for i in range(self.amountOfPoints):
			temp = f.readline().split()
			for j in range(self.amountOfPoints):
				self.massive[i][j] = int(temp[j])
		f.close()

	def dijkstra_shortest_path(self, u):
		key = 0
		for x,y in self.dictionary.items():
			if y == u:
				key = int(x)
				break
		spisok = [[float('inf'), False] for j in range(self.amountOfPoints)]
		spisok[key][0] = 0
		new_spisok = filter(lambda x: x[1]==False, spisok)
		while len(list(filter(lambda x: x[1]==False, spisok)))!= 1:
			spisok[key][1] = True
			for v in range(len(self.massive[key])):
				if self.massive[key][v]!=0 and spisok[key][0] + self.massive[key][v] < spisok[v][0]:
					spisok[v][0] = spisok[key][0] + self.massive[key][v]
			new_spisok = list(filter(lambda x: x[1]==False, spisok))
			#print(new_spisok)
			m = reduce(lambda x,y: x if x < y else y, new_spisok)
			key = spisok.index(m)
			#print(key)
		new_spisok = list(map(lambda x: x[0], spisok))
		return new_spisok

	def dijkstra_get_path(self, u, v, l):
		result = ''
		res_list = []
		start, end = 0, 0
		# print(self.dictionary)
		# sleep(2)
		for x,y in self.dictionary.items():
			# print(y, u)
			if y == u:
				# print(x)
				start = int(x)
				break
		for x,y in self.dictionary.items():
			# print(y, v)
			if y == v:
				# print(x)
				end = int(x)
				break
		# print(start, end)
		res_list.append(end)
		# print(res_list)
		finally_end = end
		while end!=start:
			for i in range(self.amountOfPoints):
				# print(l[end], self.massive[i][end], l[i])
				# sleep(2)
				if self.massive[i][end] != 0 and l[end] - self.massive[i][end] == l[i]:

					end = i
					res_list.append(end)
					break
		# print(res_list)
		# sleep(2)
		for e in range(len(res_list)-1, -1, -1):
			result += self.dictionary[str(res_list[e])]
			if e != 0:
				result += '->'
			else:
				result += ' (' + str(l[finally_end]) + ')'
		print(result)


G = Graph()
G.loadfromfile('2.txt')
l = G.dijkstra_shortest_path('x1')
G.dijkstra_get_path('x1','x3',l)

# a = [[0,False],[1, True],[4, False],[3, True]]
# f = reduce(lambda x,y: x if x > y else y, a)
# k = a.index(f)
# print(k)