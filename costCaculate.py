import matplotlib.pyplot as plt

lim = 100

cost = [((400*(i//3)) + (200*(i%3))) / (i*200) for i in range(1, lim)]

plt.plot(cost, range(1, lim))

plt.show()