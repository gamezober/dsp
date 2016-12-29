# Hint:  use Google to find python function

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

from datetime import datetime

make_date = lambda x: datetime.strptime(x, "%m-%d-%Y")

start, stop = map(make_date, [date_start, date_stop])

(stop - start).days

####b)
date_start = '12312013'
date_stop = '05282015'

from datetime import datetime

make_date = lambda x: datetime.strptime(x, "%m%d%Y")

start, stop = map(make_date, [date_start, date_stop])

(stop - start).days

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

from datetime import datetime

make_date = lambda x: datetime.strptime(x, "%d-%b-%Y")

start, stop = map(make_date, [date_start, date_stop])

(stop - start).days 
