import math 
import numpy 
from decimal import Decimal 
import matplotlib.pyplot as plt
import seaborn as sns

mean=Decimal(input("enter the value of the mean for the given data - here the mean is your birthday month "))
variance=(Decimal(input("enter the value of the variance for the data - here the variance is birthday month /4")))/4
standard_deviation=math.sqrt(variance)
print("the data given are:")
print("Mean = ",mean)
print("variance =",variance)
print("Standard deviation = ",standard_deviation)
gaussian_random=numpy.random.normal(mean,standard_deviation,500)
print("the gaussian normal distribution is ",gaussian_random)

#question 3 - plotting the values of b 
plt.figure(1)
plt.plot(gaussian_random)
plt.title("the gaussian array got")
plt.grid()
plt.show()

#question 4 - pdf of the gaussian random variable 
# Compute a histogram of the sample
x=numpy.random.normal((gaussian_random))
sns.distplot(x,hist=True)
plt.title("the probability density function ")
plt.show()
plt.grid()