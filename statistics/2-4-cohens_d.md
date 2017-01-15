[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Import Python Modules

`import math`
`from nsfg import ReadFemPreg`

First I create the function to compute Cohen's D:

~~~

def cohend(group1, group2):
     diff = group1.mean() - group2.mean()
     variance1 = group1.var()
     variance2 = group2.var()
     n1, n2 = len(group1), len(group2)
     pooled_var = (n1 * variance1 + n2 * variance2)/ (n1 + n2)
     return diff/ math.sqrt(pooled_var)
~~~

Next, I create my distributions of pregnancy weights, firsts and others:

~~~
data = ReadFemPreg()
live = data[data.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_wgt, others_wgt = firsts.totalwgt_lb, others.totalwgt_lb
~~~

Then I calculate the respective means of the distributions

`first_wgt.mean()`
7.201094430437772

`others_wgt.mean()`
7.325855614973262

First babies have a mean weight in pounds of 7.2, while other babies have a mean weight of 7.33. The mean weight for first borns is .13 lbs. lighter than the mean for others.

I then call cohend() on both distributions to factor in their variance when comparing the mean weight of first borns and others.

`cohend(first_wgt, others_wgt)`
-0.088672927072602

First babies' weight is 0.09 standard deviations (rounded up to nearest hundredth) lighter than other babies'. That's a little more than twice the amount of pregnancy length at 0.029 standard deviations. It is still much less than the difference in height of men and women at 1.7 standard deviations.
