[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>>

from random import random
import thinkstats2, thinkplot

random_dist = []
for i in range(1, 1001):
  random_dist.append(random())

#pmf
random_pmf = thinkstats2.Pmf(random_dist, label='Random Pmf')
thinkplot.Config(xlabel='Random Number', ylabel='PMF')
thinkplot.Pmf(random_pmf)

#recreate Cumulative distribution function for purpose of understanding
def cdf(dist, x):
  below_x = [y for y in dist if y <= x]
  return float(len(below_x))/len(dist)

#Plotting CDF

random_cdf = thinkstats2.Cdf(random_dist)
thinkplot.Cdf(random_cdf)
thiknplot.Show(random_cdf, xlabel='rand_num', ylabel='y')

When plotting the PMF of random_dist, it is hard to tell any patterns because there are so many values. When you plot the values and their percentiles using CDFs, however, the distribution is a straight line and therefore uniform
