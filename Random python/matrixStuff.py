import math

def size(mat):
    return len(mat),len(mat[0])

def add(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        return transpose([[a[col][row]+b[col][row] for col in range(len(a))] for row in range(len(a[0]))])

def sub(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        return transpose([[a[col][row]-b[col][row] for col in range(len(a))] for row in range(len(a[0]))])

def scale(c,A):
    return [[c*A[i][j] for j in range(size(A)[1])] for i in range(size(A)[0])]

# Element by element operations
def mulE(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        return [[a[col][row]*b[col][row] for col in range(len(a))] for row in range(len(a[0]))]

def divE(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    elif any(0 in sub for sub in b):
        return "Zero division"
    else:
        return [[a[col][row]/b[col][row] for col in range(len(a))] for row in range(len(a[0]))]

def powE(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        return [[a[col][row]**b[col][row] for col in range(len(a))] for row in range(len(a[0]))]

def eq(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        m,n=size(a)
        matching = True
        for i in range(m):
            for j in range(n):
                if a[i][j]!=b[i][j]:
                    matching = False
        return matching

def transpose(a):
    #return [list(tup) for tup in zip(a)]
    return [list(x) for x in zip(*a)]

def skew(a):
    if size(a)!= (3,1):
        return "Only able to make skew for 3x1 row vector"
    else:
        return [[0,-a[2][0],a[1][0]],[a[2][0],0,-a[0][0]],[-a[1][0],a[0][0],0]]

def mul(A,B):
    rA, cA = size(A)
    rB, cB = size(B)
    if cA != rB:
        return "Incompatible Dimensions"

    mat = []
    for i in range(rA):
        tmpR = []
        for j in range(cB):
            rVec = row(A,i)
            cVec = col(B,j)
            prod = rxc(rVec,cVec)
            tmpR.append(prod)
        mat.append(tmpR)
    return mat

def col(mat,i):
    return [[row[i]] for row in mat]

def row(mat,i):
    return transpose([[mat[i][j]] for j in range(size(mat)[1])])

def rxc(row,col):
    rm, rn = size(row)
    cm, cn = size(col)
    if rm!=1 or cn!=1 or rn!=cm:
        return "Dimensions not compatible"
    else:
        cum = sum([row[0][i]*col[i][0] for i in range(rn)])
        return cum

def subEx(A,row,col):
    mat = []
    for i in range(len(A)):
        rv = []
        if i==row:
            continue
        for j in range(len(A[0])):
            if j==col:
                continue
            rv.append(A[i][j])
        mat.append(rv)
    return mat

def determinant(A):
    if len(A[0])!=len(A):
        return "Not a square matrix"
    if len(A)==1:
        return A[0][0]
    else:
        i_max, j_max = size(A)
        firstRow = row(A,0)
        sign = [[(-1)**j for j in range(j_max)]]
        det = [[determinant(subEx(A,0,j)) for j in range(j_max)]]
        coFacs = mulE(sign,det)
        result = mul(firstRow,coFacs)
        return result[0][0]

def inv(A):
    if determinant(A)==0:
        "Non-invertible"
    return transpose(scale(1/determinant(A),[[ ((-1)**(i+j))*determinant(subEx(A,i,j)) for j in range(size(A)[1])] for i in range(size(A)[0])]))

class mat():
    def __init__(self,val):
        self.arr = val
        return

    def __str__(self):
        result = ""
        m,n = size(self.arr)
        result = result + "["
        for i in range(m):
            result = result + "["
            for j in range(n):
                result = result + str(self.arr[i][j])
                if j<n-1: # Off by one error
                    result = result + ", "
            result = result + "]"
            if i<m-1:
                result = result + ", "
        result = result + "]"
        return result

    def __eq__(self,other):
        return eq(self.arr,other.arr)

    def __ne__(self,other):
        return not self==other

    def __add__(self,other):
        return mat(add(self.arr,other.arr))

    def __sub__(self,other):
        return mat(sub(self.arr,other.arr))

    def __mul__(self,other):
        if type(other) in [float,int,complex]:
            return mat(scale(other,self.arr))
        return mat(mul(self.arr,other.arr))

    def __rmul__(self,other):
        if type(other) in [float,int,complex]:
            return mat(scale(1/other,self.arr))
        return mat(mul(other.arr,self.arr))

    def __truediv__(self,other):
        if type(other) in [float,int,complex]:
            return mat(scale(1/other,self.arr))
        return mat(mul(self.arr,inv(other.arr)))

    def __rtruediv__(self,other):
        if type(other) in [float,int,complex]:
            return mat(scale(other,inv(self.arr)))
        return mat(mul(other.arr,inv(self.arr)))

    def arr(self):
        return self.arr
    
I1 = mat([[1]])
I2 = mat([[1,0],[0,1]])
I3 = mat([[1,0,0],[0,1,0],[0,0,1]])