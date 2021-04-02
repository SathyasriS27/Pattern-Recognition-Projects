
from numpy import random 
import matplotlib.pyplot as plt
import numpy
import seaborn as sns
from decimal import Decimal 

date=Decimal(input("enter the date in dd format"))
month=Decimal(input("enter the month is mm format"))
year=Decimal(input("enter the year in yyyy format"))
print("the date entered is ",date,"-",month,"-",year)
upperlimit=max(date,month)
lowerlimit=min(date,month)

N=500
LL=[]
UL=[]
length = (upperlimit - lowerlimit)/N
i=0
while i<=N:
    if(upperlimit==lowerlimit):
        print("the upper and lower limits are same , so start again ")
        break
    LL.append(lowerlimit+(length*i))
    UL.append(LL[i]+length)
    print("I=",i,"   lowerlimit=",round(LL[i],3),"   upper limit=",round(UL[i],3))
    i=i+1

#question - 3 plotting the values of a 
#plt.figure(1)
#plt.stem(LL)
#plt.title("the plots for lower limits of uniform distribution")
#plt.grid()
#plt.show()
#plt.figure(2)
#plt.stem(UL)
#plt.title("the plots for the upper limits of uniform distribution")
#plt.grid()
#plt.show()

#question - 4 Probability density function of the data got 

x=random.uniform((lowerlimit,upperlimit))
sns.distplot(x,hist=True)
plt.title("the probability density function - of the uniform distributed data")
plt.show()
plt.grid()


import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x, 15, density=True)
plt.plot(bins, numpy.ones_like(bins), linewidth=2, color='r')
plt.show()