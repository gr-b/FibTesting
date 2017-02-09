from pylab import *

figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'recursive', 'iterative'
fracs = [58, 42]
explode = [0,5]

pie(fracs, explode=explode, labels=labels, 
		autopct='%1.1f%%', shadow=False, startangle=90)

title('Recursive vs. Iterative time: cumulative')

show()
