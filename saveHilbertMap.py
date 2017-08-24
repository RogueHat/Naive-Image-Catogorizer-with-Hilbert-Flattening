import hilbert_curve
from multiprocessing.pool import ThreadPool

side = 320

arraysize = side * side


p = ThreadPool()


def func(x):
	(a,b) = hilbert_curve.d2xy(arraysize, x)
	return (x,a,b)

lst = p.map(func,range(arraysize))


with open("hilbertmap.txt",'w') as f:
	for (a,b,c) in lst:
		mystr = "{},{},{}\n".format(a,b,c)
		f.write(mystr)
