import matplotlib.pyplot as plt


USA = [269]
Canada = [351]

slices = [269, 351]
Countries = ['USA(269)', 'Canada(351)']
cols = ['blue', 'red']

plt.pie(slices, labels=Countries, colors=cols)

plt.title('Total Induvidual Hockey Medals')
plt.legend()
plt.show()
