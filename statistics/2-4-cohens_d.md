[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


>>def cohend(group1, group2):
     diff = group1.mean() - group2.mean()
     variance1 = group1.var()
     variance2 = group2.var()
     n1, n2 = len(group1), len(group2)
     pooled_var = ((n1 * var1) + (n2 * var2))/ (n1 + n2)
     return diff/ pooled_var

First babies have a mean weight in pounds of 7.2, while other babies have a mean weight of 7.33. The mean weight for first borns  .13 lbs. lighter than the mean for others.

Function cohend() can be called on both distributions to factor in their variance when comparing the mean weight of first borns and others. The output of cohend is 0.063 standard deviations. That's a little more than twice the amount of pregnancy length at 0.029 standard deviations. It is still much less than the difference in height of men and women at 1.7 standard deviations.
