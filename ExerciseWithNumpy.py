
import numpy as np
from scipy.special import factorial
np.random.seed(1)
# dataset=[]
# for i in range(100):
#     dataset.append(random.randint(1,15))

dataset=np.random.randint(low=1,high=15,size=100)

def computation():
    return factorial(dataset)


    
import timeit
print(timeit.timeit("computation()", setup="from __main__ import computation", number=10000))

for v,fv in zip(dataset,factorial(dataset)):
    print(f"factorial {v} is {fv}")