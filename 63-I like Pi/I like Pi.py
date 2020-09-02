#Given enough iterations this could do the job but my computer takes age to do it
#Therefore there is a speedy one below, however it is far less understandable
##pi=3
##num=2
##for index in range(1000000):
##    if(index%2==0):
##        pi+=4/((num)*(num+1)*(num+2))
##    else:
##        pi-=4/((num)*(num+1)*(num+2))
##    num+=2
##pi=round(pi,30)
##print(pi)

# This one would also technically work if MAX was high enough, just the problem is that calculating pi to 30dp
# takes a lot of computing power no matter what algorithm you are using. Especially when doing it not on a really
# high specs computer. With MAX=1000000 you get to about 17 dp before it becomes innaccurate
from __future__ import division
import math
from decimal import Decimal as D
from decimal import getcontext
#This sets how many places decimal numbers are set to. So integer and the 30 dp (1+30).
getcontext().prec = 31
MAX = 1000000
#Here we use the decimal module to get a number equal to exactly 0 instead of something like 0.000000001 due to overflow errors
pi = D(0)
#K is the iterator and we go for MAX rounds
for k in range(MAX):
    #Then we just plug in the chudnovsky algorithm
    pi += D(16** -k) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))

print(pi)

