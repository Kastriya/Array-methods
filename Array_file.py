import ctypes

class Apunkalist:
    def __init__(self):
        self.n=0
        self.size=1
        self.A=self.make_ctypes(self.size)

        

    def make_ctypes(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def resize(self,new_cap):
        b=self.make_ctypes(new_cap)
        self.size=new_cap
        for i in range(self.n):
            b[i]=self.A[i]
        self.A=b
    

    def displayinfo(self):
        return self.A
   
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n==self.size:
            self.resize(self.size*2)
    
        self.A[self.n]=item
        self.n=self.n+1

    def __str__(self):
        result=""
        for i in range(self.n):
            result=result+str(self.A[i])+","

        return "["+result[:-1]+"]"    
    
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return "index error"
        
    def pop(self):
        if self.n==0:
            return "Empty list"
        
        self.n=self.n-1
        print(self.A[self.n])
        
    def clear(self):
        self.n=0
        self.size=1

    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
            
        return "Value Error"
    
    def sum(self):
        sum=0
        for i in range(self.n):
            if type(self.A[i])==int:
                sum=sum+self.A[i]

        print(sum)

    def insert(self,pos,item):
        if self.n==self.size:
            self.resize(self.size*2)

        

        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]

        if self.n>=pos:
            self.n=self.n+1
            self.A[pos]=item

        else:
            print( "Invalid index")

    def __delitem__(self,index):
        for i in range(index,self.n-1):
            self.A[i]=self.A[i+1]

        if self.n>=index:
            self.n=self.n-1
        else:
            print("Val error")

    def remove(self,item):
        pos=self.find(item)


        self.__delitem__(pos)



        

        
        
        

        
    

