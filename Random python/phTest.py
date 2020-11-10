import phasor as ph
import math

a = ph.phasor(3,4)
b = ph.phasor(2,-2)
c = ph.div(a,b)

j = ph.phasor(0,1)
neg1 = ph.pow(j,3)
print(neg1)