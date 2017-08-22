import numpy
import hilbert_curve
#~ from multiprocessing.pool import ThreadPool



side = 32
newshape = side*side
#~ p = ThreadPool()

hilbert_indexs = range(0,newshape)
hilbert_map = map(lambda x: hilbert_curve.d2xy(newshape, x), hilbert_indexs)

def arrange(img):
	hilbert_flat = map(lambda x: numpy.array(img[hilbert_map[x]]), hilbert_indexs)
	hilbert_flat = numpy.array(hilbert_flat)
	return hilbert_flat
	

