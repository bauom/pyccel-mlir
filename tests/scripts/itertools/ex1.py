# coding: utf-8

from pyccel.stdlib.parallel.openmp import omp_get_thread_num

#$ header class StopIteration(public, hide)
#$ header method __init__(StopIteration)
#$ header method __del__(StopIteration)
class StopIteration(object):

    def __init__(self):
        pass

    def __del__(self):
        pass

#$ header class Range(public, iterable)
#$ header method __init__(Range, int, int, int)
#$ header method __del__(Range)
#$ header method __iter__(Range)
#$ header method __next__(Range)
class Range(object):

    def __init__(self, start, stop, step):
        self.start = start
        self.stop  = stop
        self.step  = step

        self.i = start

    def __del__(self):
        print('> free')

    def __iter__(self):
        self.i = 0

    def __next__(self):
        if (self.i < self.stop):
            i = self.i
            self.i = self.i + 1
        else:
            raise StopIteration()

p = Range(-2,3,1)

#$ omp parallel private(i, idx)
#$ omp do
for i in p:
    idx = omp_get_thread_num()
    print("> thread id : ", idx, " working on ", i)
#$ omp end do
#$ omp end parallel
