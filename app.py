from flask import Flask ,render_template
from data import Articles
app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    print("Success")
    # return "TEST"
    return render_template('home.html',hello="GaryKim")

@app.route('/about', methods =['GET', 'POST'])]
def about():
    print("Success")
    # return "TEST"
    return render_template('about.html',hello="GaryKim")

@app.route('/articles', methods =['GET', 'POST'])]
def articles():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html',articles=articles)


if __name__=='__main__':      #서버 띄우는 명칭
    #app.run(host='0.0.0.0', port='8080')      #빈칸이면 5000
    app.run()


#서버를 띄우는 기본