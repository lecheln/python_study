n = int(input())
dic = dict()
for i in range(0,n):
	li = input().split(' ')
	dic[li[0]] = li[1]
n = int(input())
for i in range(0,n):
	st = input()
	print(dic.get(st,"error message in here"))