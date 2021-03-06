import matplotlib.pyplot as plt

x = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
y = [13,14,47,16,16,30,26,26,8,7,25,11,30,9,7,14,21,34,84,53,98,65]

x2 = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
y2 = [9,12,20,13,20,17,20,21,7,20,1,3,2,4,6,37,40,49,75,68,91,90]

plt.bar(x, y, label='USA', color='blue')
plt.bar(x2 , y2, label='Canada', color='red')

plt.plot(x, y, label='USA', color='blue')
plt.plot(x2, y2, label='Canada', color='red')
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.title('Canada vs USA: Total Medals per Year')
plt.legend()
plt.show()