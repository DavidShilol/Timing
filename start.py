from datetime import datetime
import method


stime = datetime.now()
con = method.ConnectMysql()
table = 'timing'
try:
	cursor = con.cursor()
	sql = '''
			select * 
			from {}
			where id=(select max(id) from {});
			'''.format(table, table)
	cursor.execute(sql)
	data = cursor.fetchall()
	if data and not data[0][2]:
		print('not finish')
	else:
		sql = 'insert into {}(stime) values(\'{}\')'.format(table, stime)
		cursor.execute(sql)
		con.commit()
		print('start studying at {}'.format(stime))
except Exception as e:
	con.rollback()
	print(e)
con.close()
