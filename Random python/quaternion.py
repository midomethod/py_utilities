import math

class qt():
    def __init__(self,R,x,y,z):
        self.R = R
        self.x = x
        self.y = y
        self.z = z
        self.mg = math.hypot(R,x,y,z)

    def __str__(self):
        s0 = ""
        s1 = ""
        s2 = ""
        s3 = ""
        if self.R>=0:
            s0 = "+"
        if self.x>=0:
            s1 = "+"
        if self.y>=0:
            s2 = "+"
        if self.z>=0:
            s3 = "+"
        return "{}{:.2f}\t{}{:.2f}i\t{}{:.2f}j\t{}{:.2f}k".format(s0,self.R,s1,self.x,s2,self.y,s3,self.z)
    
    def mag(self):
        return self.mg

    def __add__(self,other):
        if type(other) is float or type(other) is int:
            return add(self,qt(other,0,0,0))
        return add(self,other)

    def __radd__(self,other):
        if type(other) is float or type(other) is int:
            return add(self,qt(other,0,0,0))
        return add(self,other)

    def __sub__(self,other):
        if type(other) is float or type(other) is int:
            return sub(self,qt(other,0,0,0))
        return sub(self,other)

    def __rsub__(self,other):
        if type(other) is float or type(other) is int:
            return sub(qt(other,0,0,0),self)
        return sub(other,self)

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
            return scale(oneOver(self),other)
        return div(other,self)

    def __truediv__(self,other):
        if type(other) is float or type(other) is int:
            return scale(self,1/other)
        return div(self,other)

    def __eq__(self,other):
        if type(other) is float or type(other) is int:
            return math.isclose(self.R,other) and math.isclose(self.x,0) and math.isclose(self.y,0) and math.isclose(self.z,0)
        return math.isclose(self.R,other.R) and math.isclose(self.x,other.x) and math.isclose(self.y,other.y) and math.isclose(self.z,other.z)

    def __ne__(self,other):
        return not self is other
    
def add(a,b):
    return qt(a.R+b.R,a.x+b.x,a.y+b.y,a.z+b.z)

def sub(a,b):
    return qt(a.R-b.R,a.x-b.x,a.y-b.y,a.z-b.z)

def unit(a):
    return qt(a.R/a.mg,a.x/a.mg,a.y/a.mg,a.z/a.mg)

def conj(a):
    return qt(a.R,-a.x,-a.y,-a.z)

def mul(a,b):
    return qt(
        a.R*b.R-a.x*b.x-a.y*b.y-a.z*b.z,
        a.R*b.x+a.x*b.R+a.y*b.z-a.z*b.y,
        a.R*b.y+a.y*b.R+a.z*b.x-a.x*b.z,
        a.R*b.z+a.z*b.R+a.x*b.y-a.y*b.x)

def scale(a,c):
    return qt(c*a.R,c*a.x,c*a.y,c*a.z)

def oneOver(a):
    return scale(qt(a.R,-a.x,-a.y,-a.z),1/math.hypot(a.R,a.x,a.y,a.z)**2)

def div(a,b):
    return mul(a,oneOver(b))

def co2qt(triple): # Cartesian coordinate to quarterion
    return qt(0,triple[0],triple[1],triple[2])

def qt2co(qrtr):
    if qrtr.R != 0:
        return "Has real part"
    else:
        return qrtr.x, qrtr.y, qrtr.z

def constructQr(axis,theta):
    unitAxis = unit(axis)
    ijk = scale(unitAxis,math.sin(theta))
    real = qt(math.cos(theta),0,0,0)
    return add(real,ijk)

def constructQd(axis,thetaD):
    theta = thetaD*math.pi/180
    return constructQr(axis,theta)

def rotateLH(pt,axis,thetaD):
    Q = constructQd(axis,thetaD)
    return mul(Q,pt)

def rotateRH(pt,axis,thetaD):
    Q = constructQd(axis,thetaD)
    Q_inv = oneOver(Q)
    return mul(pt,Q_inv)

def rotate(pt,axis,thetaD):
    Q = constructQd(axis,thetaD/2)
    Q_inv = conj(Q)
    pAfterL = mul(Q,pt)
    return mul(pAfterL,Q_inv)

i = qt(0,1,0,0)
j = qt(0,0,1,0)
k = qt(0,0,0,1)