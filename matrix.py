import random
from copy import deepcopy
class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.t =[[random.randint(0,9) for j in range(self.cols)]for i in range (self.rows)]#由外向內執行
        pass

    def add(self, m):
        """return a new Matrix object after summation"""
        C=Matrix(arows,acols)
        if self.rows==m.rows and self.cols==m.cols:
            for i in range (self.rows):                  
                for j in range(self.cols):
                    C.t[i][j]=self.t[i][j]+m.t[i][j]
            return C
        else:
            print("Matrixs' size should be in same size")
            return None

    def sub(self, m):
        """return a new Matrix object after substraction"""
        C=Matrix(arows,acols)
        if self.rows==m.rows and self.cols==m.cols:
            for i in range (self.rows):                  
                for j in range(self.cols):
                    C.t[i][j]=self.t[i][j]-m.t[i][j]
            return C 
        else :
            print("Matrixs' size should be in same size")
            return None

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        
        D=Matrix(arows,bcols)
        if self.cols==m.rows and self.rows==m.cols:
            E=[]
            for i in range (self.rows):
                new_rows=[]
                E.append(new_rows)
                for x in range(m.cols):
                    new_sum=[]
                    for y in range (m.rows):
                        new_sum.append(self.t[i][y]*m.t[y][x])   
                    new_rows.append(sum(new_sum))
            for i in range (self.rows):
                for x in range (m.cols):
                    D.t[i][x]=E[i][x]          
            return D
        else:
            print("None")
            return None

    def transpose(self):
        """return a new Matrix object after transpose"""
        K=Matrix(bcols,arows)
        if not None:
            for i in range (self.rows):                  
                for x in range(self.cols):
                    K.t[x][i]=self.t[i][x]
            return K
        else:
            print("None")
            return None
    
    def display(self):
        """Display the content in the matrix"""
        for i in range (self.rows):                  
            for j in range(self.cols):
                print (self.t[i][j],end=' ')
            print('')
        pass

arows=int(input("Enter A matrixi's rows:"))
acols=int(input("Enter A matrixi's cols:"))
print ("Matrix A("+str(arows)+","+str(acols)+"):")
A=Matrix(arows,acols)
A.display()
brows=int(input("Enter B matrixi's rows:"))
bcols=int(input("Enter B matrixi's cols:"))
print ("Matrix B("+str(brows)+","+str(bcols)+"):")
B=Matrix(brows,bcols)
B.display()
print("========== A+B ========== ")
SUM=A.add(B)
if SUM==None:
    pass
else:
    SUM.display()
print("========== A-B ========== ")
MIN=A.sub(B)
if MIN==None:
    pass
else:
    MIN.display()
print("========== A*B ========== ")
F=A.mul(B)
if F==None:
    pass
else:
    F.display()
print("===== THE Transpose of A*B ===== ")
G=Matrix(arows,bcols)
if F == None:
    print("None")
    pass
else:
    G=F
    L=G.transpose()
    if L==None:
        pass
    else:
        L.display()
