"""array([[1, 0, 0],
          [2, 0, 0],
          [3, 0, 0]])"""
#hanoi nx3 problem
#numbers could jump from col1 to col3 and opposite
import numpy as np
i=0 ; j=0 ; k=0
def moveTower(height,fromPole, toPole, withPole):
    global i ,j, k
    if height >= 1:
     i+=1 ;print ('i:',i,str(height-1)); moveTower(height-1,fromPole,withPole,toPole,)
     j+=1 ; print ('j:',j); moveDisk(fromPole,toPole)
     k+=1 ;print ('k:',k,str(height-1)); moveTower(height-1,withPole,toPole,fromPole) 

def moveDisk(fp,tp):
 print("moving disk from",fp,"to",tp)
##output would be: 
moveTower(3,1,2,3)
i: 1 2
i: 2 1
i: 3 0
j: 1
moving disk from 1 to 2
k: 1 0
j: 2
moving disk from 1 to 3
k: 2 1
i: 4 0
j: 3
moving disk from 2 to 3
k: 3 0
j: 4
moving disk from 1 to 2
k: 4 2
i: 5 1
i: 6 0
j: 5
moving disk from 3 to 1
k: 5 0
j: 6
moving disk from 3 to 2
k: 6 1
i: 7 0
j: 7
moving disk from 1 to 2
k: 7 0


