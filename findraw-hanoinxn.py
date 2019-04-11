
#use findraw to find empty and non-empty row the findpole to move numbers
#The problem is 
#we call findraw function more than 9 times. It is not efficient 
#it calls many empty columns and wrong move. for example it calls findpole()
#more than 30 times to generate 5 arrays. efficiency is 16%!!
import numpy as np
import random

M = input("Pleae enter the matrix size: ")
it= input("Pleae enter the iteration number: ")

a=np.tile(0,(int(M),int(M)))


for T in range(0, int(M)): a[T,0]= 1+T
#a[1,1]=3 ; a[4,2]=2 ; a[3,4]=1
print (a)

def findraw(x):
 n=0
 while a[n,x]==0:
  n=n+1
  if n == int(M) :break
 return n
#create 1xint(M) array that shows full/empty rows
R=np.tile(0,(int(M)))
for yy in range(0,int(M)):
    R[yy]=findraw(yy)
    
    

def findpole():
 
 h=random.choice(range(0, int(M), 1)) 
 if findraw(h) == int(M):  
  print ('row %d and col %d is empty' % (findraw(h)-1, h))  #means pole is  empty
  findpole()   #so far, pole is not empty
 else:
     while True:
         d=random.choice((-1, 1))
         if h+d==-1 or h+d==int(M):
             print ('wrong move, number cannot move to -1 or %s' % str(h+d))
             continue
         else:break 
     #here number is allowed/not-allowed to move
     if findraw(h+d)==int(M) or a[findraw(h),h] < a[findraw(h+d),h+d]:
         a[findraw(h+d)-1,h+d]=a[findraw(h),h] ; a[findraw(h),h]=0 ; print (a)
     else:   
         print (a[findraw(h),h], 'cannotmove on top of',a[findraw(h+d),h+d] )
         findpole()
         
         
     

for iteration in range(0, int(it)): findpole()



