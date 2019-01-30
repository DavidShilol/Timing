import pymysql


def ConnectMysql(host='127.0.0.1', user='root', passwd='123456', db='timing'):
	con = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
	return con
