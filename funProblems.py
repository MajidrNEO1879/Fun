import math
from matplotlib.pyplot import *
rcParams.update({'font.size': 25, 'font.family': 'serif', 'lines.linewidth': 3})
figure(figsize=(20, 10))
xlabel("n")
max_n = 2000
x = range(1, max_n)
y = [100 * n * math.log(n, 2) for n in x]
plot(x, y, 'r', label='100n*log(n)')
y = [n ** 2 for n in x]
plot(x, y, 'g', label='n^2')
legend(loc=2)
show()
 