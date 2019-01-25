import pylab
principle = 10000
interest_rate = 0.05
years = 20
values = []

for i in range (years + 1):
    values.append(principle)
    principle += principle + interest_rate

pylab.plot(values,'r-',linewidth=2)
pylab.title('5% Growth . compund Anually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('values of Principle')
pylab.savefig('first')
pylab.show()
