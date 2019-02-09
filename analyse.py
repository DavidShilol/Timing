from datetime import datetime, timedelta
import method


con = method.ConnectMysql()
cursor = con.cursor()
table = 'timing'
data = []
try:
	sql = 'select * from {} where etime!=\'0000-01-01 00:00:00\';'.format(table)
	cursor.execute(sql)
	data = cursor.fetchall()
except Exception as e:
	print(e)
con.close()

# print(data)
today = datetime.now().date()
monday = today-timedelta(days=today.weekday())
sunday = monday+timedelta(days=6)
week_data = [x for x in data if monday <= x[2].date() <= sunday]
# print(week_data)
res = []
for line in week_data:
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
print('Total time this week:{}'.format(sum_time))
print('Average time this week:{}'.format(sum_time/len(res_day)))
