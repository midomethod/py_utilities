class sci():
    def __init__(self,a,b):
        m=a
        e=b
        while m >= 10:
            m /= 10
            e += 1
        while m < 1:
            m *= 10
            e -= 1
        self.m = m
        self.e = e

    def __repr__(self):
        return repr("{:.3f} E {}".format(self.m,self.e))

    def __str__(self):
        return "{:.3f} E {}".format(self.m,self.e)

    def getME(self):
        return self.m, self.e

    def scalarMul(self, c):
        m = self.m*c
        e = self.e
        while m >= 10:
            m /= 10
            e += 1
        while m < 1:
            m *= 10
            e -= 1
        return sci(m,e)

def mul(sci1,sci2):
    m1, e1 = sci1.getME()
    m2, e2 = sci2.getME()
    newM = m1*m2
    newE = e1+e2
    if newM >= 10:
        newM /= 10
        newE += 1
    return sci(newM,newE)

def div(sci1,sci2):
    m1, e1 = sci1.getME()
    m2, e2 = sci2.getME()
    newM = m1/m2
    newE = e1-e2
    if newM < 1:
        newM *= 10
        newE -= 1
    return sci(newM,newE)

def numToSci(num):
    m = num
    e = 0
    while m >= 10:
        m /= 10
        e += 1
    while m < 1:
        m *= 10
        e -= 1
    return sci(m,e)

def sciToNum(me):
    m, e = me.getME()
    return m*(10**e)

def sciToInt(me):
    m, e = me.getME()
    num = m*(10**e)
    if num%1>=0.5:
        return int(num)+1
    else:
        return int(num)
    return

def sciFactorial(num):
    prod = numToSci(1)
    if num==0 or num==1:
        return prod
    i = 2
    while i<=num:
        mult = numToSci(i)
        prod = mul(prod,mult)
        i+=1
    return prod

def pow(base,power):
    newB = numToSci(base)
    powerDec = power%1
    powerInt = power//1
    result = numToSci(base**powerDec)
    i = powerInt
    while i>0:
        result=mul(result,newB)
        i-=1
    while i<0:
        result=div(result,newB)
        i+=1
    return result

def birthday(NumClass=1):
    probUnique = div(sciFactorial(365),mul(sciFactorial(365-NumClass),pow(365,NumClass)))
    Prob = sciToNum(probUnique.scalarMul(100)) # The percent probability
    return Prob
