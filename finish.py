from datetime import datetime
import method


etime = datetime.now()
con = method.ConnectMysql()
table = 'timing'
try:
	cursor = con.cursor()
	sql = '''
			select * 
			from {}
			where id=(select max(id) from {}) 
			and etime='0000-01-01 00:00:00';
			'''.format(table, table)
	cursor.execute(sql)
	data = cursor.fetchall()
	if not data:
		print('not start a time')
	else:
		info = input('commit info:')
		sql = 'update {} set etime=\'{}\',info=\'{}\' where id={}'.format(table, etime, info, data[0][0])
		# print(sql)
		cursor.execute(sql)
		con.commit()
		print('finish studying at {}'.format(etime))
except Exception as e:
	print(e)
con.close()
