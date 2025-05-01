import matplotlib.pyplot as plt
import numpy as np
#Setting up plot
figure = plt.figure(figsize= (10,10), facecolor= 'white')
graph= figure.add_subplot(1,1,1)
# this anonymous function represents the function that will be graphed
equation = lambda x: (np.cos(x) + (.05)*x*x)
# createing list from -10 -> 9.8 with step of .2
rangeAndDomain = np.arange(-10,10,.2)
graph.plot(rangeAndDomain, equation(x = rangeAndDomain))
#setting axis labels
graph.set_ylabel("V(x) / $E_0$", fontsize = 20)
graph.set_xlabel("$\hat{\Phi} -\pi$", fontsize = 20)
plt.show()
