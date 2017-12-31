import numpy as np
import matplotlib.pyplot as plt

rawData = np.loadtxt("data.dat")
x=rawData.transpose()[0]
y=rawData.transpose()[1]


order = 9

coeff=np.polyfit(x,y,order)
f=np.poly1d(coeff)


x_new=np.linspace(x[0],x[-1],101)
y_new=f(x_new)


fh=open("output.dat","wb")
np.savetxt(fh,np.c_[order],fmt="%10d")
np.savetxt(fh,coeff,fmt="%10.8e")
fh.close()

plt.plot(x,y, "r*",label="data")
plt.plot(x_new,y_new, "b-",label="fit")
plt.savefig('figure.pdf', format='pdf')
plt.show()


