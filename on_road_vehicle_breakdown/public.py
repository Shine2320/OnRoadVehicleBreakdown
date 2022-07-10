from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/logout',methods=['get','post'])
def logout():
	session.clear()
	
	return redirect(url_for('public.home'))

@public.route('/',methods=['get','post'])
def home():
	session.clear()
	
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if 'submit' in request.form:
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			session['username']=res[0]['username']
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))
			else:
				flash('INCORRECT USERNAME OR PASSWORD')
		else:
			flash("COMPLETE REGISTRATION BEFORE LOGIN")
	return render_template('login.html')


@public.route('/userreg',methods=['get','post'])
def userreg():
	session.clear()
	data={}
	if 'submit' in request.form:
		print("^^^^^^^^^^^^^^^^^^^^^^^^")
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		ph=request.form['phone']
		email=request.form['email']
		dis=request.form['dis']
		street=request.form['street']
		gen=request.form['gen']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash('THIS USER NAME ALREADY TAKEN BY ANOTHER USER')
			return redirect(url_for('public.userreg'))
		else:
			q="insert into login values('%s','%s','user')"%(uname,password)
			insert(q)
			q="insert into customer values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(uname,fname,lname,place,ph,email,dis,street,gen)
			insert(q)
			return redirect(url_for('public.userreg'))
	return render_template('userreg.html',data=data)


# @public.route('/customerreg',methods=['get','post'])
# def customerreg():
# 	data={}
# 	if 'submit' in request.form:
# 		fname=request.form['fname']
# 		lname=request.form['lname']
# 		ph=request.form['phone']
# 		email=request.form['email']
# 		lat=request.form['lat']
# 		lon=request.form['lon']
# 		uname=request.form['uname']
# 		password=request.form['password']
# 		q="select * from login where username='%s' and password='%s'"%(uname,password)
# 		res=select(q)
# 		if res:
# 			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
# 			return redirect(url_for('public.customerreg'))
# 		else:
# 			q="insert into login values('%s','%s','customer')"%(uname,password)
# 			lid=insert(q)
# 			q="select * from customers order by customer_id desc limit 1"
# 			res=select(q)
# 			if res:
# 				s="c__"
# 				precid=res[0]['customer_id'].split("__")
# 				print(precid)
# 				cid=int(precid[1])+1
# 				cid="c__"+str(cid)
# 				print(cid)
# 			else:
# 				cid="c__1"
# 			q="insert into customers values('%s','%s','%s','%s','%s','%s','%s','%s')"%(cid,uname,fname,lname,ph,email,lat,lon)
# 			insert(q)
# 			return redirect(url_for('public.customerreg'))
# 	return render_template('customerreg.html',data=data)
