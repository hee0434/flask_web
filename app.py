from flask import Flask ,render_template #flask 라이브러리 가져옴

app = Flask(__name__)  #app이라는 flask객체를 생성 (이 안에는 member field와 method가 포함 되어있다)
app.debug=True


@app.route('/')
def index():
    print("Success")
    # return "TEST"
    return render_template('home.html', hello="GaryKim")

@app.route('/about')
def about():
    print("Success")
    # return "TEST"
    return render_template('about.html', hello="GaryKim")

@app.route('/articles')
def articles():
    print("Success")
    # return "TEST"
    return render_template('articles.html', hello="GaryKim")


if __name__=='__main__':      #서버 띄우는 명칭
    #app.run(host='0.0.0.0', port='8080')      #빈칸이면 5000
    app.run()


#서버를 띄우는 기본