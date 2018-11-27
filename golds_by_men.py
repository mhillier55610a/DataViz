import matplotlib.pyplot as plt

y = [1,6,11,2,5,2,1,18,1,0,0,1,24,3,1,0,2,2,5,7,10,5]
y2 = [9,12,14,0,17,16,0,1,4,0,0,0,0,2,0,0,1,7,30,6,41,32]
x = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

plt.scatter(x,y, label='USA', s=100, marker="*", color='blue')
plt.scatter(x,y2, label='Canada', s=100, marker="p", color='red')

plt.plot(x, y, color='blue')
plt.plot(x, y2, color='red')
plt.ylabel('Medals')
plt.xlabel('Year')
plt.title('Gold Medals Won by Men')
plt.legend()
plt.show()