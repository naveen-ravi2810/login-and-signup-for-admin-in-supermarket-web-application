from flask import *
from flask_mysqldb import *


app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'prolist'
 
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')  
def login():  
    return render_template("login.html")

@app.route('/validate', methods = ["POST"])  
def validate(): 
     
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        flash("LOGGED IN SUCCESSFULLY")  
    return redirect(url_for("login"))  

@app.route('/success')  
def success():  
    return "logged in successfully"

@app.route('/create', methods=['GET', 'POST'])
def product():
    #for adding
    
    if request.method == 'POST':
        userdetails=request.form
        cur=mysql.connection.cursor()
        name=userdetails['proname']
        code=userdetails['procode']
        price=userdetails['price']
        
        cur.execute("INSERT INTO products(proname,procode,price) values(%s, %s, %s)",(name, code, price))
        mysql.connection.commit()
        cur.close()
        return render_template('success.html')
    return render_template('create.html')

@app.route('/lists')
def list():
    cur=mysql.connection.cursor()
    rvalue=cur.execute("select * from products")
    if rvalue > 0:
        userdetails=cur.fetchall()
        return render_template('lists.html',userdetails=userdetails)


'''@app.route('/delete/<char:procode>')
def delete(procode):
    cur=mysql.connection.cursor()
    cur.execute('delete from products where procode= %s ',procode)
    mysql.connection.commit()
    cur.close()
    return render_template('okdeleted')'''
    





if __name__ == '__main__':
    app.run(debug=True)