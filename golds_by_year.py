import matplotlib.pyplot as plt

x = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
y = [1,6,13,2,6,4,2,18,1,1,3,3,24,4,2,5,6,25,11,9,12,10]

x2 = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
y2 = [9,12,14,0,18,16,0,3,4,1,0,1,0,2,0,5,3,14,53,29,68,63]

plt.bar(x, y, label='USA', color='blue')
plt.bar(x2 , y2, label='Canada', color='red')

plt.plot(x, y, label='USA', color='blue')
plt.plot(x2, y2, label='Canada', color='red')
plt.xlabel('Year')
plt.ylabel('Gold Medals')
plt.title('Canada vs USA: Gold Medals per Year')
plt.legend()
plt.show()