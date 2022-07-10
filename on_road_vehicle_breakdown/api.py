from flask import *
from database import *
import demjson
import uuid

api=Blueprint('api',__name__)


@api.route('/login')
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login  where username='%s' and password='%s'"%(username,password)
	r=select(q)
	if r:
		data['status']="success"
		data['data']=r
	else:
		data['status']="failed"
	return demjson.encode(data)

@api.route('/userregister')
def userregister():
	data={}
	firstname=request.args['fname']
	lastname=request.args['lname']
	place=request.args['place']
	phone=request.args['phone']
	em=request.args['email']
	username=request.args['username']
	password=request.args['password']
	latitude=request.args['latitude']
	longitude=request.args['longitude']
	q="select * from login  where username='%s' "%(username)
	r=select(q)
	if r:
		data['status']="duplicate"
	else:

		q="insert into login values(null,'%s','%s','user')"%(username,password)
		id=insert(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,place,latitude,longitude,phone,em)
		r=insert(q)
		print(r)
		data['status']="success"
	return demjson.encode(data)


@api.route('/publicviewmechanics')
def publicviewmechanics():
	data={}
	q="select * from mechanicshop"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/publicviewpetrolpump')
def publicviewpetrolpump():
	data={}
	q="select * from petrolpumps"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)




@api.route('/publicviewfeedback')
def publicviewfeedback():
	data={}
	q="select * from feedback"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)


@api.route('/publicaddfeedback')
def publicaddfeedback():
	data={}
	feedback=request.args['feedback']
	q="insert into feedback values(null,'%s',curdate())"%(feedback)
	insert(q)
	data['status']="success"
	return demjson.encode(data)




@api.route('/usermanagecomplaints')
def usermanagecomplaints():
	data={}
	lid=request.args['lid']
	complaint=request.args['complaint']
	q="insert into complaint values(null,(select user_id from user where login_id='%s'),'%s','pending',curdate())"%(lid,complaint)
	insert(q)
	data['status']="success"
	data['method']="usermanagecomplaints"
	return demjson.encode(data)


@api.route('/userviewcomplaints')
def userviewcomplaints():
	data={}
	lid=request.args['lid']
	q="select * from complaint where user_id=(select user_id from user where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewcomplaints"
	return demjson.encode(data)


@api.route('/userviewmechanics')
def userviewmechanics():
	data={}
	lati=request.args['lati']
	longi=request.args['longi']
	
	q="SELECT *,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM mechanicshop HAVING user_distance <40 ORDER BY user_distance ASC " %(lati,longi,lati)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  demjson.encode(data)



@api.route('/mechaniceditprofile')
def mechaniceditprofile():
	data={}
	lid=request.args['lid']
	name=request.args['name']
	place=request.args['place']
	phone=request.args['phone']
	email=request.args['email']
	latitude=request.args['latitude']
	longitude=request.args['longitude']
	q="update mechanicshop set shopname='%s',latitude='%s',longitude='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(name,latitude,longitude,place,phone,email,lid)
	update(q)
	data['status']="success"
	data['method']="mechaniceditprofile"
	return demjson.encode(data)

@api.route('/userupdate')
def userupdate():
	data ={}
	lid=request.args['lid']
	fname=request.args['fname']
	lname=request.args['lname']
	place=request.args['place']
	phone=request.args['phone']
	email=request.args['email']
	latitude=request.args['latitude']
	longitude=request.args['longitude']
	q="update user set firstname='%s', lastname='%s',latitude='%s',longitude='%s', place='%s' ,phone='%s' ,email='%s' where login_id='%s'"%(fname,lname,latitude,longitude,place,phone,email,lid)
	update(q)
	data['status']="success"
	data['method']="userupdate"
	return demjson.encode(data)

@api.route('/mechanicviewprofile')
def mechanicviewprofile():
	data={}
	lid=request.args['lid']
	q="select * from mechanicshop where shop_id=(select shop_id from mechanicshop where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="mechanicviewprofile"
	return demjson.encode(data)

@api.route('/userview')
def userview():
	data={}
	lid=request.args['lid']
	q="select * from user  where user_id=(select user_id from user where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userview"
	return demjson.encode(data)


@api.route('/userviewnearestpetrolpump')
def userviewnearestpetrolpump():
	data={}
	lati=request.args['lati']
	longi=request.args['longi']
	
	q="SELECT *,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM petrolpumps HAVING user_distance <40 ORDER BY user_distance ASC " %(lati,longi,lati)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  demjson.encode(data)

@api.route('/Mechviewpumps')
def Mechviewpumps():
	data={}
	q="select * from petrolpumps"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/userviewnearestservicecenter')
def userviewnearestservicecenter():
	data={}
	lati=request.args['lati']
	longi=request.args['longi']
	
	q="SELECT *,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM servicecenter HAVING user_distance <40 ORDER BY user_distance ASC " %(lati,longi,lati)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  demjson.encode(data)



@api.route('/usersendrequest')
def usersendrequest():
	data={}
	lid=request.args['lid']
	mid=request.args['mid']
	problem=request.args['problem']
	q="insert into request values(null,'%s',(select user_id from user where login_id='%s'),'%s','',curdate(),'pending')"%(mid,lid,problem)
	insert(q)
	data['status']="success"
	return demjson.encode(data)



@api.route('/userviewrequest')
def userviewrequest():
	data={}
	lid=request.args['lid']
	q="select * from request inner join mechanicshop using(shop_id) where user_id=(select user_id from user where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)


@api.route('/usermakepayment')
def usermakepayment():
	data={}
	rid=request.args['rid']
	amount=request.args['amount']
	q="insert into payment values(null,'%s','%s',curdate())"%(rid,amount)
	insert(q)
	q="update `request` set status='paid' where request_id='%s'"%(rid)
	update(q)
	data['status']="success"
	return demjson.encode(data)


@api.route('/mechanicviewrequest')
def mechanicviewrequest():
	data={}
	lid=request.args['lid']
	q="select * from request  where shop_id=(select shop_id from mechanicshop where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)


@api.route('/mechanicviewuserdetails')
def mechanicviewuserdetails():
	data={}
	uid=request.args['uid']
	q="select * from user  where user_id='%s'"%(uid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/mechanicenteramount')
def mechanicenteramount():
	data={}
	rid=request.args['rid']
	amount=request.args['amount']
	q="update request set status='accept', amount='%s' where request_id='%s'"%(amount,rid)
	update(q)
	data['status']="success"
	return demjson.encode(data)


@api.route('/updatepasslocation',methods=['get','post'])
def updatepasslocation():
	data={}

	latti=request.args['latti']
	longi=request.args['longi']
	logid=request.args['logid']
	q="select * from user where login_id='%s'"%(logid)
	res=select(q)
	if res:

	
		q="update `user` set `latitude`='%s',`longitude`='%s' where `login_id`='%s'"%(latti,longi,logid)
		id=update(q)
	else:
		q="update `mechanicshop` set `latitude`='%s',`longitude`='%s' where `login_id`='%s'"%(latti,longi,logid)
		id=update(q)

	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'updatepasslocation'
	return demjson.encode(data)