import numpy as np
import matplotlib.pyplot as plt 
#Importing tools required

rawData = np.loadtxt("data.dat")
x=rawData.transpose()[0]
y=rawData.transpose()[1]
#Reads input from data.dat file and transposes columns into rows


order = 9
#Order of the polynomial to get best fit. 
#Figure this out by trial and error

coeff=np.polyfit(x,y,order) #Returns a least squares fit and stores it in coeff
f=np.poly1d(coeff) #Creates a 1D polynomial class

plt.plot(x,y, "r*",label="data") #Plot x,y with red asterisks and label as data.
plt.xlabel('numbers')
plt.ylabel('their squares')
plt.savefig('figure.pdf', format='pdf') #Save the figure as a pdf
plt.show()


