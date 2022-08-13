from flask import Flask, request, render_template, session, redirect, url_for
import os
import pymysql

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {
    'guest': 'guest',
    'user': 'user1234',
    'admin': '1'
}

def comments(post):
    db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
    co_ = db.cursor()
    sql = "select * from comment where art_key = %d" %(post)
    co_.execute(sql)
    result = co_.fetchall()
    result = list(result)
    db.close()
    return result

def tag():
    db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
    tag = db.cursor()
    sql = "select * from tag"
    tag.execute(sql)
    result = tag.fetchall()
    db.close()
    return result

result = tag()

def userexist():
    try: 
        if session['id']: return True
    except : return False

@app.route('/')
def index():
    login = userexist()
    return render_template('index.html', username=session.get("id"), login=login)

@app.route('/login')
def login():
    if "id" in session:
        return render_template("login.html",username=session.get("id"), login = True)
    else:
        return render_template("login.html", login = False)

@app.route('/signin', methods = ["get"])
def signin():
    userid = request.args.get('id')
    passwd = request.args.get('pw')
    
    if passwd == users[userid]:
        session["id"] = userid
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("id")
    return redirect(url_for("login"))

@app.route('/question')
def question():
    login = userexist()
    return render_template('question.html', tag=result, username=session.get("id"), login=login)

@app.route('/answer')
def answer():
    login = userexist()
    db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
    article = db.cursor()
    sql = "select * from articles"
    article.execute(sql)
    articles = article.fetchall()
    articles = list(articles)
    db.close()
    return render_template('answer.html', article=articles, tag = result, username=session.get("id"), login=login)

@app.route('/answer/<string:cate>')
def answer_detail(cate):
    login = userexist()
    category = str(cate)
    db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
    article = db.cursor()
    sql = "select * from articles where tag = '%s'" %(category)
    article.execute(sql)
    articles = article.fetchall()
    articles = list(articles)
    db.close()
    return render_template('answer.html', article=articles, tag = result, username=session.get("id"), login=login)



@app.route('/user')
def user():
    login = userexist()
    return render_template('user.html', username=session.get("id"), login=login)

@app.route('/write/<string:tag_>')
def write(tag_):
    login = userexist()
    return render_template('write.html', username=session.get("id"), login=login, tag_ = tag_)

@app.route('/post/<string:tag_>', methods = ["get", "post"])
def post(tag_):
    login = userexist() 
    if login == False: return render_template('errorwrite.html')
    id = session.get("id")
    # tag = str(request.args.get('tag'))
    title = str(request.args.get('title'))
    content = str(request.args.get('content'))
    db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
    article = db.cursor()
    article.execute("INSERT INTO articles VALUES(%s, %s, %s, %s, %s)", [None, id, title, content, tag_])
    db.commit();
    return redirect(url_for('answer', login=login, tag=result))
    
@app.route('/detail/<int:post>', methods = ["get", "post"])
def detail(post):
    if request.method == 'GET':
        login = userexist() 
        db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
        article = db.cursor()
        sql="select * from articles where MYKEY = %d" %(post)
        article.execute(sql)
        article = article.fetchall()
        id = article[0][1]
        tag = article[0][4]
        title = article[0][2]
        content = article[0][3]
        db.close()
        return render_template('detail.html', key = post, id=id, tag=tag, title=title, content=content, co=comments(post),username=session.get("id"), login=login)
    elif request.method == 'POST':
        login = userexist() 
        id = session.get("id")
        content = request.form['comment']
        print(content)
        db = pymysql.connect(host='us-cdbr-east-06.cleardb.net', port=3306, user='bbc263342cae56', passwd='33c946ea', db='heroku_0a4b1cb2682c753', charset='utf8')
        comment = db.cursor()
        comment.execute("INSERT INTO comment VALUES(%s, %s, %s, %s)", [None, id, content, post])
        db.commit();
        return redirect(url_for('detail', post=post))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
