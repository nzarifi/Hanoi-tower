# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:30:15 2019

@author: nzarifi
"""
#in order to move number 5 times findpole() was called 8 times 5/8=62%  
import numpy as np
import random
#create empty 2D array
M = input("Pleae enter the matrix size: ")
it= input("Pleae enter the iteration number: ")

a=np.tile(0,(int(M),int(M)))

for T in range(0, int(M)): a[T,0]= 1+T
#a[7,1]=6 ; a[7,2]=7 ; a[7,4]=8 ; a[7,7]=10
print (a)

def findraw(x):
 n=0
 while a[n,x]==0:
  n=n+1
  if n == int(M) :break
 return n

R=np.tile(0,(int(M)))
for yy in range(0,int(M)):
    R[yy]=findraw(yy)    
R
#checks and only keeps location of non-empty col here!
def update_col():
    global allowed_col       
    allowed_col=[]
    for nope in range(0,len(R)):
        if R[nope]!=int(M):allowed_col.append(nope)  
    
update_col()


    

def findpole(): 
 h=random.choice(allowed_col) #random choice inside 
 while True:
     d=random.choice((-1, 1))
     if h+d==-1 or h+d==int(M):
         print ('wrong move, the %s col does not exist' % str(h+d))
         continue
     else:break
 if R[h+d]==int(M) or a[R[h],h] < a[R[h+d],h+d]:
    a[R[h+d]-1,h+d]=a[R[h],h] ; a[R[h],h]=0 ; print (a)
    R[h+d]=R[h+d]-1
    R[h]=R[h]+1
    update_col() 
 else:
    print (a[R[h],h], 'cannotmove on top of',a[R[h+d],h+d] )
    findpole()
                
     

for iteration in range(0, int(it)): findpole()




