from multiprocessing.pool import ThreadPool as Pool
import fastf1
import datetime
import warnings

warnings.filterwarnings("ignore")
fastf1.Cache.enable_cache('D:/f1data')

pool_size = 10
pool = Pool(pool_size)

def loadGP(year, gp):
    for session in range(1,6,1):
        fastf1.get_session(year, gp, session).load()
    return None

for year in range(2018,datetime.date.today().year+1,1):
    schedule=fastf1.get_event_schedule(year, include_testing=False)
    for gp in schedule['Country']:
        pool.apply_async(loadGP, (year, gp,))

pool.close()
pool.join()