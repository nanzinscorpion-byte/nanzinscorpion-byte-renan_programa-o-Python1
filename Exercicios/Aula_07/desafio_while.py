import os
os.system('cls')

import time

cont=1
acm=0

while (cont <=10):

    if(cont%2 ==0):
        acm+=cont
        print(cont)

    time.sleep(0.7)
    
    cont+=1
print(acm)        