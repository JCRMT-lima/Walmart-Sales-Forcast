import pandas

df = pandas.read_csv("ClusterExample2.csv")

from sklearn.cluster import OPTICS

### type your code here 

import numpy

space = numpy.arange(len(df))

from matplotlib import pyplot 
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(2, 1)
fig1 = pyplot.subplot(G[0, 0])
fig2 = pyplot.subplot(G[1, 0])

# Plot the reachability plot
colors = ['g.', 'r.', 'b.', 'y.', 'c.']
for klass, color in zip(range(0, 5), colors):
    Xk = space[labels == klass]
    Rk = reachability[labels == klass]
    fig1.plot(Xk, Rk, color, alpha=0.3)
fig1.plot(space[labels == -1], reachability[labels == -1], 'k.', alpha=0.3)
fig1.plot(space, numpy.full_like(space, 2., dtype=float), 'k-', alpha=0.5)
fig1.plot(space, numpy.full_like(space, 0.5, dtype=float), 'k-.', alpha=0.5)
fig1.set_ylabel('Reachability (epsilon distance)')
fig1.set_title('Reachability Plot')

# Plot the cluster assignment
colors = ['g.', 'r.', 'b.', 'y.', 'c.']
for klass, color in zip(range(0, 5), colors):
    Xk = df[optics.labels_ == klass]
    fig2.plot(Xk.iloc[:, 0], Xk.iloc[:, 1], color, alpha=0.3)
fig2.plot(df.iloc[optics.labels_ == -1, 0], df.iloc[optics.labels_ == -1, 1], 'k+', alpha=0.1)
fig2.set_title('OPTICS Clustering')

df = read