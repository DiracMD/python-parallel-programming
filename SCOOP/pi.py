import math
from random import random
from scoop import futures
from time import time


def evaluate_points_in_circle(attempts):
    points_fallen_in_unit_disk=0
    for i in range(0,attempts):
        x=random()
        y=random()
        radius=math.sqrt(x*x+y*y)
        if radius <1:
            points_fallen_in_unit_disk=points_fallen_in_unit_disk+1
    return points_fallen_in_unit_disk

def pi_calculus_with_Montecarlo_method(workers,attempts):
    print("number pf workers %i - number of attempts %i"%(workers,attempts))
    bt=time()
    evaluate_task=futures.map(evaluate_points_in_circle,[attempts]*workers)
    taskresult=sum(evaluate_task)
    print("%i points fallen in a unit disk after" %(taskresult/attempts))
    piValue=(4.*taskresult/float(workers*attempts))
    computationalTime=time()-bt
    print("value of pi ="+str(piValue))
    print("error percentage="+str((((abs(piValue - math.pi)) * 100) / math.pi)))
    print("total time: " + str(computationalTime))


if __name__=="__main__":
    for i in range (1,4):
        pi_calculus_with_Montecarlo_method(i*10000,i*10000)
        print(" ")
