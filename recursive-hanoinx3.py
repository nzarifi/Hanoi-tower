
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
 


