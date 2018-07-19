import random
from copy import deepcopy
class Matrix:
    def __init__(self,rows,cols):
        self.t =[]
        self.rows=rows
        self.cols=cols
        self.t =[[random.randint(0,9) for j in range(self.cols)]for i in range (self.rows)]#由外向內執行
        pass

    def add(self, m):
        """return a new Matrix object after summation"""
        if self.rows==m.rows and self.cols==m.cols:
            for i in range (self.rows):                  
                for j in range(self.cols):
                    C.t[i][j]=self.t[i][j]+m.t[i][j]
            return C.t   
        else:
            print("Matrixs' size should be in same size")
        # except IndexError :
        #     print("Matrixs' size should be in same size")
        pass

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if self.rows==m.rows and self.cols==m.cols:
            for i in range (self.rows):                  
                for j in range(self.cols):
                    C.t[i][j]=self.t[i][j]-m.t[i][j]
            return C.t   
        else :
            print("Matrixs' size should be in same size")
        pass

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if self.cols==m.rows:
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
        pass

    def transpose(self):
        """return a new Matrix object after transpose"""
        for i in range (self.rows):                  
                for x in range(self.cols):
                    F.t[x][i]=D.t[i][x]
        return F
        pass
    
    def display(self):
        """Display the content in the matrix"""
        for i in range (self.rows):                  
            for j in range(self.cols):
                print (self.t[i][j],end=' ')
            print()
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
C=Matrix(arows,acols)
D=Matrix(arows,bcols)
F=Matrix(arows,bcols)
print("========== A+B ========== ")
A.add(B)
C.display()
print("========== A-B ========== ")
A.sub(B)
C.display()
print("========== A*B ========== ")
A.mul(B)
D.display()
print("===== THE Transpose of A*B ===== ")
D.transpose()
F.display()
