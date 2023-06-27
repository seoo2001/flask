from flask import Flask, request, render_template, redirect, abort
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'GET':
        num = request.args["num"]
        name = request.args.get("name")
        return "GET으로 전달된 데이터({} {})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        return "POST로 전달된 데이터({} {})".format(num, name)

@app.route('/hello')
def hellohtml():
    return render_template("hello.html")

@app.route('/hello/<name>')
def helloname(name):
    return "안녕{}".format(name)

@app.route('/hello/<int:num>')
def hellonum(num):
    if num==1:
        return '하나'
    elif num==2:
        return '둘'
    elif num==3:
        return '셋'
    else: return 'others'

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/google')
def google():
    return redirect("https://google.com")

@app.errorhandler(404)
def page_not_found(error):
    return "404 error", 404

@app.route('/nopage')
def nopage():
    abort(404)
    return "404로 보냅니다."


if __name__ == '__name__':
    app.run(debug=True)