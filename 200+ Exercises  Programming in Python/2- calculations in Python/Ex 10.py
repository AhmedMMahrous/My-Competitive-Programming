from cmath import sqrt
# details ==> https://www.scribbr.com/statistics/geometric-mean/
import numpy
def calc_mean(*args):
    args_1 =  numpy.prod(args)   ## multiplying arguments
    mean = (args_1)**(1/len(args))

    print(f"Geometric average of the given numbers: {mean:0.2f}")

calc_mean(4, 3, 4.5, 5)
