import matplotlib.pyplot as plt

y = [0,0,0,0,1,2,1,1,0,1,3,2,0,1,1,5,4,23,6,2,2,5]
y2 = [0,0,0,0,1,0,0,2,0,1,0,1,0,0,0,5,2,7,23,23,27,31]
x = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

plt.scatter(x,y, label='USA', s=100, marker="*", color='blue')
plt.scatter(x,y2, label='Canada', s=100, marker="p", color='red')

plt.plot(x, y, color='blue')
plt.plot(x, y2, color='red')
plt.ylabel('Medals')
plt.xlabel('Year')
plt.title('Gold Medals Won by Women')
plt.legend()
plt.show()