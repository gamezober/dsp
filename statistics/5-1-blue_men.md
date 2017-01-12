[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> REPLACE THIS TEXT WITH YOUR RESPONSE

import scipy.stats

min height (5'10) = 177.8
max height (6'1) = 185.42

Mu for Males = 178
SD for Males = 7.7

min_percentile_rank = scipy.stats.norm.cdf(177.8, loc = 178, scale = 7.7)
max_percentile_rank = scipy.stats.norm.cdf(185.42, loc = 178, scale = 7.7)

bmg_chance = max_percentile_rank - min_percentile_rank
bmg_chance

0.34274683763147368
34.2% of Men are in the height range to be in the Blue Man Group.
