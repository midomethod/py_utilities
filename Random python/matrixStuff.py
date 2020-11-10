import math

def size(mat):
    return len(mat),len(mat[0])

def add(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        return [[a[col][row]+b[col][row] for col in range(len(a))] for row in range(len(a[0]))]

def sub(a,b):
    if size(a) != size(b):
        return "Dimensions must match"
    else:
        return [[a[col][row]-b[col][row] for col in range(len(a))] for row in range(len(a[0]))]

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
        val = [[not math.isclose(a[col][row],b[col][row]) for col in range(len(a))] for row in range(len(a[0]))][0]
        return not any(val)

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

