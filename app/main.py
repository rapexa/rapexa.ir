from __future__ import barry_as_FLUFL
import email
from datetime import timedelta
import config
import MySQLdb
from flask import Flask , render_template,request , redirect,jsonify, flash, url_for, Response, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# config
app.config.update(
    SECRET_KEY = config.secret_key,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin"


# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return "%d" % (self.id)


# create some users with ids 1 to 20       
user = User(0)

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('sign_in')   
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)    

@app.errorhandler(404)
def page_not_found(e):
    '''this function is for 404 error'''
    ret = {'code':'404','message':'file not found !'}
    return jsonify(ret) , 200

@app.route("/ok")
def sys_check():
    '''this function tell that falsk server is ok and running!!'''
    ret = {'status':'ok','message':'server is running'}
    return jsonify(ret) , 200

@app.route('/', methods=["GET", "POST"])
def index(): 
    '''main page'''
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        title = request.form["title"]
        message = request.form["message"]
        write_msg_to_database(name,email,phone,title,message)
        return redirect('/')

    else:
        return render_template('index.html')


@app.route('/sign_up',methods=["GET", "POST"])
@limiter.limit("10 per minute")
def signup(): 
    '''main page'''
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        write_user_to_database(name,email,phone,password)
        return redirect('/')
    
    return render_template('sign_up.html')

@app.route('/97E0848778679DE516AEFF12986FF261CCEF0D692397B45017DDD62D492FCC64',methods=["GET", "POST"])
@limiter.limit("10 per minute")
def admin(): 
    '''admin page'''
    session.permanent = True
    error = None
    
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["Password"]
        if check_admin(username,password):
            #login_user(user)
            all_messages = reading_msg_from_database()
            messages = []
            for message in all_messages:
                name , email, phone, title , message = message
                messages.append({"name":name,"email":email,"phone":phone,"title":title,"message":message})
            
            all_users = reading_usr_from_database()
            users = []
            for user in all_users:
                usr_name, usr_email, usr_phone, password = user
                users.append({"name":usr_name,"email":usr_email,"phone":usr_phone,"password":password})
            
            return render_template('dashboard.html', data = {"messages" : messages,"users" : users})
        
        else:
            error = '!!!invalid user!!!'
        
    if current_user.is_authenticated:
        return redirect("/97E0848778679DE516AEFF12986FF261CCEF0D692397B45017DDD62D492FCC64") 
            
    return render_template('sign_in.html', error=error)
    

def check_admin(username,password):
    res = False
    if username == config.admin_user_name and password == config.admin_pass_word:
        res = True
    return res               

def check_user(username,password):
    res = False
    all_users = reading_usr_from_database()
    for user in all_users:
        usr_name, usr_email, usr_phone, usr_password = user
        if username == usr_email and password == usr_password:
            res = True
            break
    return res

def write_msg_to_database(name,email,phone,title,message):
    db = connect_to_database()
    cur = db.cursor()                       
    phonetxt = str(phone)
    qury = f'INSERT INTO messages VALUES ("{name}","{email}","{phonetxt}","{title}","{message}");'
    cur.execute(qury)
    db.commit()
    db.close()

def write_user_to_database(name,email,phone,password):
    db = connect_to_database()
    cur = db.cursor()                       
    phonetxt = str(phone)
    passwordtxt = password
    qury = f'INSERT INTO users VALUES ("{name}","{email}","{phonetxt}","{passwordtxt}");'
    cur.execute(qury)
    db.commit()
    db.close()
    
def reading_msg_from_database():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute("SELECT * FROM messages;")
    db.close()
    return cur.fetchall()

def reading_usr_from_database():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute("SELECT * FROM users;")
    db.close()
    return cur.fetchall()

def connect_to_database():
    db = MySQLdb.connect(host=config.MYSQL_HOST,
                       user=config.MYSQL_USER,
                       passwd=config.MYSQL_PASS,
                       db=config.MYSQL_DB,
                       charset=config.charset)
    return db

if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)
    