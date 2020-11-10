import math

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