def fibo(n):
	i, j, cnt = 0, 1, 1
	while i < n:
		yield i
		i, j = j, i + j
		cnt += 1


p = sum(a for a in fibo(4000000) if a % 2 == 0)

print(f'The result is:\n{p}')
