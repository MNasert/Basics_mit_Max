import time
def test(x):
	q = 0
	n = 0
	for i in range(x):
		q += i
		n = n+q
	return q


if __name__ == "__main__":
	start = time.time()
	for _ in range(100000):
		test(1000)
	end = time.time()
	print(end-start)
