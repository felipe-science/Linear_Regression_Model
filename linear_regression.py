from numpy import loadtxt, linspace
from pylab import scatter, plot, show, xlabel, ylabel, title, tick_params
from scipy.optimize import curve_fit

def func_fit(x, a, b):
    return a*x+b


data = loadtxt("data.dat",float)
xdata = data[:,0]
ydata = data[:,1]
xcurv = linspace(0,10,100)
ycurv = []

param,pcov = curve_fit(func_fit, xdata, ydata)
a = param[0]
b = param[1]

#Curve Fit
for x in xcurv:
    ycurv.append(func_fit(x, a, b))

print("============================")
print("Parameters:")
print("   a = ",a)
print("   b = ",b)
print("\n")
print("Covariance matrix: ")
print(pcov)
print("============================")

scatter(xdata, ydata, color='black')
plot(xcurv,ycurv, color='red')
xlabel("Independent variable (x)", fontsize = '15')
ylabel("Dependent variable (y)", fontsize = '15')
title("Linear Regression", fontsize = '20')
tick_params(labelsize='15')
show()


sumx = sum(xdata)
sumy = sum(ydata)    
medx = sumx/12.0
medy = sumy/12.0
sumx2 = 0
sumxy = 0

for i in range(12):
    sumx2 = sumx2 + (xdata[i])**2
    sumxy = sumxy + xdata[i]*ydata[i]

b = (sumxy - medy*sumx)/(sumx2 - medx*sumx)
a = medy - b*medx

print("\n\n angular coefficient: ",b)
print("Lienar coefficient: ",a)
