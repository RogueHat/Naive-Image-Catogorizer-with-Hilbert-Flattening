import numpy
import hilbert_curve

class hilbert_tool(object):
	def __init__(self, side):
		newshape = side * side
		self.hidx = range(0,newshape)
		self.hmap = map(lambda x: hilbert_curve.d2xy(newshape, x), self.hidx)
		
	def hilbert_flatten(self, img):
		hilbert_flat = map(lambda x: numpy.array(img[self.hmap[x]]), self.hidx)
		hilbert_flat = numpy.array(hilbert_flat)
		return hilbert_flat
