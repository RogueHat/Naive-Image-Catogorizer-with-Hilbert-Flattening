
from Tkinter import *
import hilbert_curve

side = 320
newshape = side * side
hidx = range(0,newshape)
hmap = map(lambda x: hilbert_curve.d2xy(newshape, x), hidx)

master = Tk()

w = Canvas(master, width=side, height=side)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
