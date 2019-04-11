#This one shows how numbers move left and right

import numpy as np
import random
M = input("Pleae enter the matrix size: ")
it= input("Pleae enter the iteration number: ")
a=np.tile(0,(int(M),int(M)))

##data = numpy.arange(100).reshape((10,10))
#R=np.tile(0,16)
#R=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
for T in range(0, int(M)): a[T,0]= 1+T 
# extra values to test 
#a[0,14]=14; a[0,4]=2 ; a[6,6]=6 ;a[3,15]=315 ; a[1,3]=13;  a[5,3]=53 ; a[3,1]=31 ;a[4,2]=42  ;a[1,9]=19 ;a[15,8]=158 ; a[15,15]=15
print (a)
#create empty R:Row, right and left with size of 1xint(M)
for iteration in range(0, int(it)):
 R=np.tile(0,int(M)) 
 right=np.tile(0,int(M))
 left=np.tile(0,int(M))
##R[] shows full row index and when the col is empty it put int(M)-1 
 j=0
 i=0
 while i==0 and j <= (int(M)-1):
  for i in range(int(M)):
   if a[i,j]!=0  :  R[j]=i ;   j=j+1 ; i=0   ; break #non-empty row for each column
   if a[i,j]==0 and i==(int(M)-1) : R[j]=i ;i=0 ; j=j+1 ; break  #when col is empty   
 print (R)  
 
 
#right [1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
#left [ 0  0  0 -1 -1  0  0  0  0 -1  0  0  0  0  0  0]
# define 1xint(M) left and right move
 i=1 
 for j in range(1,int(M)-1):
  #number could move left:-1 or right:+1 or it is empty,0
  if a[int(R[j]),i] < a[int(R[j-1]),i-1] or a[int(R[j-1]),i-1]==0 : left[j]=-1  
  if a[int(R[j]),i] < a[int(R[j+1]),i+1] or a[int(R[j+1]),i+1]==0 : right[j]=+1 
  if a[int(R[j]),i]==0 : left[j]=0 ; right[j]=0
  i=i+1 #taking care of first and last column
  if a[int(R[int(M)-1]),(int(M)-1)] < a[int(R[int(M)-2]),(int(M)-2)] or a[int(R[int(M)-2]),(int(M)-2)]==0: left[(int(M)-1)]=-1
  if a[int(R[0]),0] < a[int(R[1]),1] or a[int(R[1]),1]==0 : right[0]=1
#when two left/right are zero, zero means 1. number AND 2. empty 
  if a[int(R[int(M)-1]),int(M)-1] == a[int(R[int(M)-2]),int(M)-2] or a[int(R[int(M)-1]),int(M)-1]==0  : left[int(M)-1]=0
  if a[int(R[0]),0] == a[int(R[1]),1] or a[int(R[0]),0]==0 : right[0]=0
 print (right  , left) 
# how left or right move replace numbers with empty or full col 
#  if j ==15 and a[i,j]==0 : print i,j ; R[j]=i; break 
 while True:
  i = random.choice(range(len(left)))
  if left[i]!=0 and a[int(R[i-1]) , i-1]!=0:print ('left') , i ; a[int(R[i-1])-1 , i-1]=a[int(R[i]) , i] ; a[int(R[i]) , i]=0 ;break 
  if left[i]!=0 and a[int(R[i-1]) , i-1]==0:print ('left') , i ; a[int(R[i-1]) , i-1]=a[int(R[i]) , i] ; a[int(R[i]) , i]=0 ;break
  i = random.choice(range(len(right)))
  if right[i]!=0 and a[int(R[i+1]) , i+1]!=0 : print ('right') , i ;a[int(R[i+1])-1 , i+1]=a[int(R[i]) , i] ; a[int(R[i]) , i]=0; break 
  if right[i]!=0 and a[int(R[i+1]) , i+1]==0 : print ('right') , i ;a[int(R[i+1]) , i+1]=a[int(R[i]) , i] ; a[int(R[i]) , i]=0; break
 
  else: continue
#print '"left" , i,  a[int(R[i-1]) , i-1] ,a[int(R[i+1]) , i-1] , a[int(R[i]) , i]'
 print (a)
