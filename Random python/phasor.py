import math
"""
It is now obsolete since I underestimated python's ability to work with complex numbers
"""

class phasor():
    def __init__(self,real,imag):
        self.re = real
        self.im = imag
        self.ma = math.hypot(real,imag)
        self.an = math.atan2(imag,real)

    def __repr__(self):
        return repr("{:.3f} + {:.3f}j".format(self.re,self.im))
    
    def __str__(self):
        return "{:.3f} + {:.3f}j".format(self.re,self.im)

    def __add__(self,other):
        if type(other) is float or type(other) is int:
            return add(self,phasor(other,0))
        return add(self,other)

    def __radd__(self,other):
        if type(other) is float or type(other) is int:
            return add(self,phasor(other,0))
        return add(self,other)

    def __sub__(self,other):
        if type(other) is float or type(other) is int:
            return sub(self,phasor(other,0))
        return sub(self,other)

    def __rsub__(self,other):
        if type(other) is float or type(other) is int:
            return sub(phasor(other,0),self)
        return sub(other,self)

    def __pow__(self,other):
        return pow(self,other)

    def __rmul__(self,other):
        if type(other) is float or type(other) is int:
            return scale(self,other)
        return mul(self,other)

    def __mul__(self,other):
        if type(other) is float or type(other) is int:
            return scale(self,other)
        return mul(self,other)

    def __rtruediv__(self,other):
        if type(other) is float or type(other) is int:
            return scale(div(phasor(1,0),self),other)
        return div(other,self)

    def __truediv__(self,other):
        if type(other) is float or type(other) is int:
            return scale(self,1/other)
        return div(self,other)

    def __eq__(self,other):
        if type(other) is float or type(other) is int:
            return math.isclose(self.re,other) and math.isclose(self.im,0) 
        return math.isclose(self.re,other.re) and math.isclose(self.im, other.im)

    def __ne__(self,other):
        return not self==other

    def real(self):
        return self.re
    
    def imag(self):
        return self.im

    def mag(self):
        return self.ma

    def ang(self):
        return self.an

def add(a,b):
    return phasor(a.re+b.re,a.im+b.im)

def scale(a,c):
    return phasor(a.re*c,a.im*c)

def sub(a,b):
    return phasor(a.re-b.re,a.im-b.im)

def phasor2(mg,ag):
    return phasor(mg*math.cos(ag),mg*math.sin(ag))

def phasor2d(mg,ag):
    return phasor(mg*math.cos(ag*math.pi/180),mg*math.sin(ag*math.pi/180))

def mul(a,b):
    return phasor2(a.mag()*b.mag(),a.ang()+b.ang())

def div(a,b):
    return phasor2(a.mag()/b.mag(),a.ang()-b.ang())

def pow(a,n):
    return phasor2(a.mag()**n,a.ang()*n)

i = phasor(0,1)