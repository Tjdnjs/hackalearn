from flask import Flask, request, render_template, session, redirect, url_for

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
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")