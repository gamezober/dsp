# Learn Python

Read Allen Downey's [Think Python](	thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are similar in that they both are a collection of values of any type. The difference is that lists are mutable while tuples are immutable. Tuples work as keys in dictionaries because they are immutable and unordered.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and Sets are both a collection of values and are both mutable. Lists are sortable while sets are not. Lists allow for duplicate values while sets do not.

A list could be [0, 0, 1, 3, 4] and a set would be ([0, 1, 3, 4]).

It's tough to say which perform better (both have advantages and disadvantages), but values in sets are hashed so checking for membership is faster in sets.

Lists
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambdas are anonymous functions. They are expressions that can be applied to a list rather than having to loop a function through that list. They can also be used to filter lists. Lambdas are used in the key argument for sorted() as a more efficient way to call a function on a sequence and sort by its output. e.g.:

fruit = [('apples', 2.50),
    ('strawberries', 4.00),
    ('peaches', 2.25),
    ('figs', 6.00)]

sales_tax = .15

Code Below sorts fruit by the cost of their sales tax cost:

sorted(fruit, key = lambda f: f[1] * sales_tax)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a way to create lists with less code than traditional for loops. They are also another way to pass a sequence through a function.

For example, to create a list of factors for 500 I can run:

factor_500 = [x for x in range(1, 501) if 500%x == 0]

If I used filter() to produce the same list, the code would look like this:

factor_500 = list(filter(lambda x: 500%x == 0, range(1,501)))

def is_factor_500(x):
    if x == 0:
        print "Error: Divide by Zero"
    elif 500 % 0 == 0:
        return True
    else:
        return False

If I want to find the cube of a list of numbers I could use map(), or I could use a list comprehension.

With map():

cube_list = list(map(lambda x: x**3, range(5)))

With List comprehension:

cube_list = [x**3 for x in range(5)]

Since map() requires the use of lambda, it could perform slower if the sequence is large.

I can use comprehensions to create a dictionary of numbers and their roman numeral. I used the function to_roman() that I created when I applied to Metis:

roman = {x : to_roman(x) for x in range(1, 10)}

I can also create a set comprehension similar to a list comprehension but only with unique values since sets remove duplicates:

set_500 = [x for x in range(1, 501) if 500%x == 0]
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'

```

>> REPLACE THIS TEXT WITH YOUR RESPONSE 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 Days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
