import matplotlib.pyplot as plt


USA = [3]
Canada = [9]

slices = [3, 9]
Countries = ['USA', 'Canada']
cols = ['blue', 'red']

plt.pie(slices, labels=Countries, colors=cols)

plt.title('Team Hockey Gold Medal Wins')
plt.legend()
plt.show()
