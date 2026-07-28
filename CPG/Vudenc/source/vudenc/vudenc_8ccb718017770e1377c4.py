def demo(n):...
switcher = {(1):
    'SELECT year,faculty, count(*) as N from hej where faculty=1 group by faculty,year;'
    , (2):
    'SELECT fulltimecontingent, count(*) from hej where year =2010 group by  fulltimecontingent'
    , (3):
    'SELECT parttimecontingent, count(*) from hej where year =2010 group by  parttimecontingent'
    , (4):
    'SELECT year,count(*) from hej where (tenured=1 or tenured_track=1) group by year;'
    , (5):
    'SELECT count(*) from hej where (tenured = 1 or tenured_track =1) and (year=2007 or year=2012 or year=2017) group by year'
    , (6):
    'SELECT count(*) as N, maintable.minimumedurequirements as R from hej,maintable where (hej.jobid=maintable.jobid) and (hej.faculty = 1) and (hej.year>= 2010) group by maintable.minimumedurequirements'
    }
z = queryAll(switcher.get(n, 0))
return z
