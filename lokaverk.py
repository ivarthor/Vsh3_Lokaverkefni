import pymysql
from bottle import *

@get('/')
def index():
    return template('index.tpl')

@route('/doinnskra',method='POST')
def doinn():

    u = request.forms.get('user')
    p = request.forms.get('pass')
    
    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
    cur = conn.cursor()

    cur.execute("select count(*) from 0901013310_vsh3_lokaverk.ritari where u_nafn=%s and pass =%s",(u,p))
    result = cur.fetchone()
    if result[0] == 1:
        cur.close()
        conn.close()
        return template('admin.tpl')
    else:
        return "reyndu aftur <br><a href='/'>til baka</a>"

@route('/frettir')
def frett():
    
    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
    cur = conn.cursor()
    cur.execute("select f_nafn, f_desc from 0901013310_vsh3_lokaverk.frettir")
    frettirr = cur.fetchall()
    cur.close()
    return template("frettir.tpl",frett = frettirr)

@route("/frett/<id:int>")
def frettid(id):

    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
    cur = conn.cursor()
    cur.execute("select f_nafn, f_desc from 0901013310_vsh3_lokaverk.frettir")
    frettirr = cur.fetchall()
    cur.close()
    return template("frett.tpl",frett = frettirr[id], nr = id)


@route("/breyta", method = 'POST')
def edit_story():

    i = request.forms.get('ID')
    s = request.forms.get('story')
    a = request.forms.get('author')

    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
    cur = conn.cursor()

    takki = request.forms.get('breytan')

    if takki == 'Breyta':
        conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
        cur = conn.cursor()
        cur.execute('update 0901013310_vsh3_lokaverk.frettir set f_desc= "{}" where f_id = "{}"'.format(s,i))
        conn.commit()
        conn.close()
        redirect('/')
    else:
        conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
        cur = conn.cursor()
        cur.execute("delete from 0901013310_vsh3_lokaverk.frettir where f_id='{}'".format(i))
        conn.commit()
        conn.close()
        redirect('/')


@route("/nyfrett", method='POST')
def news():

    i = request.forms.get('ID')
    s = request.forms.get('story')
    a = request.forms.get('author')

    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vsh3_lokaverk")
    cur = conn.cursor()
    cur.execute("select count(*) from 0901013310_vsh3_lokaverk.ritari where author=%s",(a))
    result = cur.fetchone()

    if result[0] == 1:
        cur.execute("insert into 0901013310_vsh3_lokaverk.frettir(f_id,f_desc,author) values(%s,%s,%s", (i,s,a))
        print("insert into 0901013310_vsh3_lokaverk.frettir(f_id,f_desc,author) values(%s,%s,%s")
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        return "reyndu aftur <br><a href='/doinnskra'>til baka</a>"  


@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root = "./static")


try:
    run(host="0.0.0.0", port=os.environ.get('PORT'))
except:
    run(host="localhost", port=7000, debug=True)
    #run(debug=True)