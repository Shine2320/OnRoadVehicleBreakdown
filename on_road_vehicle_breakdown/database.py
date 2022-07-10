import mysql.connector

password=""	
database = "on_road_vehicle_breakdown"
def select(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	result = cur.fetchall()
	cur.close()
	cnx.close()
	return result
def update(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount
	cur.close()
	cnx.close()
	return result
def delete(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount
	cur.close()
	cnx.close()
	return result
def insert(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.lastrowid
	cur.close()
	cnx.close()
	return result