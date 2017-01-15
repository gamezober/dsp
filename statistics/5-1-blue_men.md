[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

First I define the parameters for the range of accepted heights in the Blue Man Group,
then identify the mean and standard deviation for the distribution I'll be using:

~~~
import scipy.stats

min_height = 177.8 # (5'10)
max_height = 185.42 # (6'1)

#mean and standard deviation for Males
mu = 178
sd = 7.7
~~~

Then I use to stats.norm.cdf to calculate the percentile rank for the min and max. Once I find the min and max, I can subtract the former from the latter to calculate the probability that a random male will be in the qualifying height range for the Blue Man Group:

~~~
min_percentile_rank = scipy.stats.norm.cdf(177.8, loc = 178, scale = 7.7)
max_percentile_rank = scipy.stats.norm.cdf(185.42, loc = 178, scale = 7.7)

bmg_chance = max_percentile_rank - min_percentile_rank
bmg_chance

#0.34274683763147368
~~~
34.2% of Men are in the height range to be in the Blue Man Group.
