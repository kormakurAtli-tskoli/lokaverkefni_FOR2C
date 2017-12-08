# Kormákur Atli Unnþórsson & Þröstur Haraldsson
# 8.12.2017
# Lokaverkefni

from bottle import *
from sanitize import sanitize
import pymysql
global username

#static files route
@route("/static/<filename>")
def staticFile(filename):
    return static_file(filename, root="./static/")

@get("/")
def index():
    return template("index.tpl")

@get("/nyskraning")
def nyskraningarsida():
    return  template("nyskraning.tpl")

@post("/")
def index():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                                 port=3306,
                                 user='1604002850',
                                 passwd='mypassword',
                                 db='1604002850_lokaverkfor',
                                 charset='utf8')
    global name
    username = sanitize(request.forms.get("username"))
    password = sanitize(request.forms.get("password"))
    passconf = sanitize(request.forms.get("passconf"))
    name = sanitize(request.forms.get("name"))
    address = sanitize(request.forms.get("address"))
    phone = sanitize(request.forms.get("phone"))
    email = sanitize(request.forms.get("email"))
    response.set_cookie('username',username)
    with connection.cursor() as cursor:
        sql = "SELECT user, pass FROM user WHERE user = '"+username+"'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            uttak = "Notandi er nú þegar til"
        else:
            sql = "INSERT INTO user (user, pass, name, addr, phon, emai) VALUES ('"+username+"', '"+password+"', '"+name+"', '"+address+"', '"+phone+"', '"+email+"')"
            cursor.execute(sql)
            connection.commit()
            uttak = "Notandi hefur verið stofnaður!"
    connection.close()
    return template("indexAfterSignup.tpl",uttak=uttak)

@post("/innskraning")
def nyskraning():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                             port=3306,
                             user='1604002850',
                             passwd='mypassword',
                             db='1604002850_lokaverkfor',
                             charset='utf8')
    global username
    username = sanitize(request.forms.get("username"))
    password = str(sanitize(request.forms.get("password")))
    response.set_cookie('username',username)
    with connection.cursor() as cursor:
        sql = "SELECT pass FROM user WHERE user = '"+username+"'"            
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print(result[0])
            print(password)
            if str(result[0]) == str(password):
                response.set_cookie("account",username, secret=password)
                return template("redirect.tpl")
            else:
                uttak = "Rangt lykilorð"
        else:
            uttak = "Notandinn er ekki til"
    connection.close()                
    if uttak == "Rangt lykilorð":
        return template("indexAfterSignup.tpl",uttak=uttak)
    elif uttak == "Notandinn er ekki til":
        return template("indexAfterSignup.tpl",uttak=uttak)

@route("/utskra")
def utskraning():
    response.set_cookie("account","", expires=0)
    return template("index.tpl")

@route("/thread",method=['GET','POST'])
def main():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                             port=3306,
                             user='1604002850',
                             passwd='mypassword',
                             db='1604002850_lokaverkfor',
                             charset='utf8')
    global username
    with connection.cursor() as cursor:
        if request.forms.get("text"):
            print(request.forms.get("titill"))
            print(request.forms.get("text"))
            sql = "INSERT INTO thread(title,text,writer) VALUES ('"+request.forms.get("titill")+"','"+request.forms.get("text")+"','"+username+"')"
            cursor.execute(sql)
            connection.commit()
        sql = "SELECT name FROM user WHERE user = '"+username+"'"
        cursor.execute(sql)
        name = cursor.fetchone()[0]
        sql = "SELECT count(*) FROM thread;"
        cursor.execute(sql)
        fjThrada = cursor.fetchone()[0]
        sql = "SELECT * FROM thread LIMIT 0,9999"
        cursor.execute(sql)
        threads = cursor.fetchall()
    connection.close()
    return template("leynisida.tpl",name=name,fjThrada=fjThrada,threads=threads)

@route("/thread/<tala>",method=['GET', 'POST'])
def main(tala):
    connection = pymysql.connect(host='tsuts.tskoli.is',
                             port=3306,
                             user='1604002850',
                             passwd='mypassword',
                             db='1604002850_lokaverkfor',
                             charset='utf8')
    global username
    with connection.cursor() as cursor:
        if request.forms.get("komment"):
            sql = "INSERT INTO comments(thread,comment,author) VALUES ("+tala+",'"+sanitize(request.forms.get("komment"))+"','"+username+"')"
            cursor.execute(sql)
            connection.commit()
        sql = "SELECT name FROM user WHERE user = '"+username+"'"
        cursor.execute(sql)
        name = cursor.fetchone()[0]
        sql = "SELECT * FROM thread WHERE thread_ID ='"+tala+"'"
        cursor.execute(sql)
        threads = cursor.fetchall()
        sql = "SELECT * FROM comments WHERE thread = "+tala
        cursor.execute(sql)
        komment = cursor.fetchall()
    connection.close()
    return template("thread.tpl",name=name,threads=threads,tala=tala,komment=komment)

@route("/newthread",method=['GET','POST'])
def new():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                             port=3306,
                             user='1604002850',
                             passwd='mypassword',
                             db='1604002850_lokaverkfor',
                             charset='utf8')
    global username
    with connection.cursor() as cursor:
        sql = "SELECT name FROM user WHERE user = '"+username+"'"
        cursor.execute(sql)
        name = cursor.fetchone()[0]
    connection.close()
    return template("newthread.tpl",name=name)
@error(500)
def custom500(error):
    uttak = "Þú verður að vera skráður inn. Ef þú ert ekki með aðgang, getur þú búið hann til"
    return template("indexAfterSignup.tpl",uttak=uttak)
run(host='0.0.0.0',  port=os.environ.get('PORT'))
