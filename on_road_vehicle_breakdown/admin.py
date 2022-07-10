from flask import *
from database import *
import uuid

admin = Blueprint('admin', __name__)


@admin.route('/adminhome', methods=['get', 'post'])
def adminhome():
    if not session.get("lid") is None:
        return render_template("adminhome.html")
    else:
        return redirect(url_for("public.login"))


@admin.route('/admin_manage_mechanic', methods=['get', 'post'])
def admin_manage_mechanic():
    if not session.get("lid") is None:
        data = {}
        if 'submit' in request.form:
            shopname = request.form['shopname']
            lat = request.form['lat']
            lon = request.form['lon']
            place = request.form['place']
            phone = request.form['phone']
            email = request.form['email']
            uname = request.form['uname']
            password = request.form['password']
            q = "select * from login where username='%s'" % (uname)
            res = select(q)
            if res:
                flash('THIS USER NAME ALREADY TAKEN BY ANOTHER USER')
                return redirect(url_for('admin.admin_manage_mechanic'))
            else:
                q = "insert into login values(NULL,'%s','%s','mechshop')" % (uname, password)
                lid = insert(q)
                q = "insert into mechanicshop values(NULL,'%s','%s','%s','%s','%s','%s','%s')" % (
                lid, shopname, lat, lon, place, phone, email)
                insert(q)
            return redirect(url_for('admin.admin_manage_mechanic'))
        q = "select * from mechanicshop"
        res = select(q)
        if res:
            data['mechanicshop'] = res
            print(res)
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
            lids= request.args['lids']
        else:
            action = None
        if action == 'delete':
            p="delete from login where login_id='%s'"%(lids)
            delete(p)
            q = "delete from mechanicshop where shop_id='%s'" % (id)
            delete(q)
            return redirect(url_for('admin.admin_manage_mechanic'))
        if action == 'update':
            q = "select * from mechanicshop inner join login using(login_id) where shop_id='%s'" % (id)
            data['updater'] = select(q)
        if 'update' in request.form:
            shopname = request.form['shopname']
            lat = request.form['lat']
            lon = request.form['lon']
            place = request.form['place']
            phone = request.form['phone']
            email = request.form['email']
            uname = request.form['uname']
            passw = request.form['passw']
            p="update login set username='%s',password='%s' where login_id='%s'"%(uname,passw,lids)
            q = "update mechanicshop set shopname='%s',latitude='%s',longitude='%s',place='%s',phone='%s',email='%s' where shop_id='%s'" % (
            shopname, lat, lon, place, phone, email, id)
            update(q)
            return redirect(url_for('admin.admin_manage_mechanic'))
        return render_template('admin_manage_mechanic.html', data=data)
    else:
        return redirect(url_for("public.login"))


@admin.route('/admin_manage_servicecenter', methods=['get', 'post'])
def admin_manage_servicecenter():
    if not session.get("lid") is None:
        data = {}
        if 'submit' in request.form:
            center = request.form['center']
            place = request.form['place']
            lat = request.form['lat']
            lon = request.form['lon']

            phone = request.form['phone']
            email = request.form['email']
            q = "insert into servicecenter values(NULL,'%s','%s','%s','%s','%s','%s')" % (
            center, place, lat, lon, phone, email)
            insert(q)
            return redirect(url_for('admin.admin_manage_servicecenter'))
        q = "select * from servicecenter"
        res = select(q)
        if res:
            data['center'] = res
            print(res)
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
        if action == 'delete':
            q = "delete from servicecenter where servicecenter_id='%s'" % (id)
            delete(q)
            return redirect(url_for('admin.admin_manage_servicecenter'))
        if action == 'update':
            q = "select * from servicecenter where servicecenter_id='%s'" % (id)
            data['updater'] = select(q)
        if 'update' in request.form:
            center = request.form['center']
            lat = request.form['lat']
            lon = request.form['lon']
            place = request.form['place']
            phone = request.form['phone']
            email = request.form['email']
            q = "update servicecenter set centername='%s',latitude='%s',longitude='%s',place='%s',phone='%s',email='%s' where servicecenter_id='%s'" % (
            center, lat, lon, place, phone, email, id)
            update(q)
            return redirect(url_for('admin.admin_manage_servicecenter'))
        return render_template('admin_manage_servicecenter.html', data=data)
    else:
        return redirect(url_for("public.login"))


@admin.route('/admin_manage_pump', methods=['get', 'post'])
def admin_manage_pump():
    if not session.get("lid") is None:
        data = {}
        if 'submit' in request.form:
            pname = request.form['pname']
            place = request.form['place']
            lat = request.form['lat']
            lon = request.form['lon']
            phone = request.form['phone']
            email = request.form['email']
            q = "insert into petrolpumps values(NULL,'%s','%s','%s','%s','%s','%s')" % (
            pname, place, lat, lon, phone, email)
            insert(q)
            return redirect(url_for('admin.admin_manage_pump'))
        q = "select * from petrolpumps"
        res = select(q)
        if res:
            data['pump'] = res
            print(res)
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
        if action == 'delete':
            q = "delete from petrolpumps where pump_id='%s'" % (id)
            delete(q)
            return redirect(url_for('admin.admin_manage_pump'))
        if action == 'update':
            q = "select * from petrolpumps where pump_id='%s'" % (id)
            data['updater'] = select(q)
        if 'update' in request.form:
            pname = request.form['pname']
            lat = request.form['lat']
            lon = request.form['lon']
            place = request.form['place']
            phone = request.form['phone']
            email = request.form['email']
            q = "update petrolpumps set pumpname='%s',latitude='%s',longitude='%s',place='%s',phone='%s',email='%s' where pump_id='%s'" % (
            pname, lat, lon, place, phone, email, id)
            update(q)
            return redirect(url_for('admin.admin_manage_pump'))
        return render_template('admin_manage_pump.html', data=data)
    else:
        return redirect(url_for("public.login"))


@admin.route('/admin_view_request', methods=['get', 'post'])
def admin_view_request():
    if not session.get("lid") is None:
        data = {}
        q = "SELECT * FROM request INNER JOIN user USING(user_id) INNER JOIN mechanicshop USING(shop_id) "
        res = select(q)
        print(res)
        data['request'] = res
        return render_template("admin_view_request.html", data=data)
    else:
        return redirect(url_for("public.login"))


@admin.route('/admin_view_feedback', methods=['get', 'post'])
def admin_view_feedback():
    if not session.get("lid") is None:
        data = {}
        q = "SELECT * FROM feedback"
        res = select(q)
        data['feedbacks'] = res
        print(res)
        # if 'action' in request.args:
        # 	action=request.args['action']
        # 	id=request.args['id']
        # 	if action=="update":
        # 		q="select * from feedback inner join admins using(admin_id) where feedback_id='%s' "%(id)
        # 		res=select(q)
        # 		data['updater']=res
        # if 'update' in request.form:
        # 	reply=request.form['reply']
        # 	q="update feedback set reply='%s' where feedback_id='%s'"%(reply,id)
        # 	update(q)
        # 	return redirect(url_for('admin.admin_view_feedback'))
        return render_template('admin_view_feedback.html', data=data)
    else:
        return redirect(url_for("public.login"))


@admin.route('/admin_view_complaints', methods=['get', 'post'])
def admin_view_complaints():
    if not session.get("lid") is None:
        data = {}
        q = "SELECT * FROM user INNER JOIN complaint USING(user_id)"
        res = select(q)
        data['complaints'] = res
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
            if action == "update":
                q = "select * from complaint inner join user using(user_id) where complaint_id='%s' " % (id)
                res = select(q)
                data['updater'] = res
        if 'update' in request.form:
            reply = request.form['reply']
            q = "update complaint set reply='%s' where complaint_id='%s'" % (reply, id)
            update(q)
            return redirect(url_for('admin.admin_view_complaints'))
        return render_template('admin_view_complaints.html', data=data)
    else:
        return redirect(url_for("public.login"))
