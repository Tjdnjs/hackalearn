from flask import Flask, request, render_template, session, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = "hackalearn2022"

ID = "admin"
PW = "1"

@app.route('/')
def index():
    # html file은 templates 폴더에 위치해야 함
    return render_template('index.html')

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
    
    if userid == ID and passwd == PW:
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
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='qkrtjdnjsdb1!', db='hackalearn', charset='utf8')
    tag = db.cursor()
    sql = "select * from tag"
    tag.execute(sql)
    result = tag.fetchall()
    db.close()
    return render_template('question.html', tag=result)

@app.route('/answer')
def answer():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='qkrtjdnjsdb1!', db='hackalearn', charset='utf8')
    article = db.cursor()
    sql = """
        select * from articles
    """
    article.execute(sql)
    articles = article.fetchall()
    articles = list(articles)
    db.close()
    return render_template('answer.html', article=articles)

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/post', methods = ["get"])
def post():

    id = ID
    tag = str(request.args.get('tag'))
    title = str(request.args.get('title'))
    content = str(request.args.get('content'))

    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='qkrtjdnjsdb1!', db='hackalearn', charset='utf8')
    article = db.cursor()
    article.execute("INSERT INTO articles VALUES(%d, %s, %s, %s, %s)", [None, id, title, content, tag])
    db.commit();
    article.execute("select * from articles where content = %s" [content])
    key = article[-1]
    return redirect(url_for('detail'), idx=key[0])
    
@app.route('/detail', methods = ["get"])
def detail():
    idx = request.args.get('idx')
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='qkrtjdnjsdb1!', db='hackalearn', charset='utf8')
    article = db.cursor()
    article.execute("select * from articles where MYKEY = %d" [idx])
    result = article.fetchall()
    id = result[1]
    tag = result[4]
    title = result[2]
    content = result[3]
    db.close()
    return render_template('detail.html', id=id, tag=tag, title=title, content=content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
