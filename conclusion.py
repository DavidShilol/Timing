from datetime import datetime, timedelta
import method


con = method.ConnectMysql()
today = datetime.now().date()
eday = today-timedelta(days=today.weekday()+1)
sday = eday-timedelta(days=6)
data = []
try:
    sql = 'select * from timing where etime!=\'0000-01-01 00:00:00\';'
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
except Exception as e:
    print(e)
finally:
    con.close()

last_week_data = [x for x in data if sday <= x[2].date() <= eday]
res = []
for line in last_week_data:
    delta = line[2]-line[1]
    res.append((line[0], line[1], line[2], delta, line[3]))
res_day = {}
for x in res:
    date = x[2].date()
    res_day[date] = res_day.get(date, timedelta())+x[3]
print('Learning Record:')
sum_time = timedelta()
for k, v in res_day.items():
    print(k.strftime('%m-%d'), v)
    sum_time += v
print('Total time last week:{}'.format(sum_time))
print('Average time last week:{}'.format(sum_time/7))
