import numpy as np
import matplotlib.pyplot as plt


#qst 1 digramme de dispersion
def diagramme_dispersion():
    data = np.loadtxt("data1.txt")
    plt.scatter(data[:,0],data[:,1])
    plt.show()
