from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_name = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    character = db.Column(db.String(25), nullable = False)
    kills = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    supports = db.Column(db.Integer)
    role = db.Column(db.Integer)
    win = db.Column(db.String(7))

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def main():
    article = Article.query.order_by(Article.kills/Article.deaths).all()
    return render_template('main_page.html', article=article, best=Article.query.order_by(Article.kills/Article.deaths)[Article.query.count() - 1])

@app.route('/get_articles', methods = ['GET'])
def get_articles():
    articles = Article.query.all()
    to_send = []
    for i in articles:
        add = {
            'id': i.id,
            'title': i.title,
            'character': i.character,
            'kills': i.kills,
            'deaths': i.deaths,
            'supports': i.supports,
            'role': i.role,
            'win': i.win,
        }
        to_send.append(add)
    data = {'articles': to_send}
    return jsonify(data)

@app.route('/input', methods = ['POST', 'GET'])
def input():
    if request.method == 'POST':
        title = request.form['title']
        character = request.form['character']
        kills = request.form['kills']
        deaths = request.form['deaths']
        supports = request.form['supports']
        role = request.form['role']
        win = request.form['win']
        article = Article(title=title, character=character, kills=kills, deaths=deaths, supports=supports, role=role, win=win)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/summary')
        except Exception as error:
            return str(error)
    else:
        return render_template('input.html')
    
@app.route('/summary')
def posts():
    article = Article.query.order_by(Article.kills/Article.deaths).all()
    return render_template("summary.html", article=article)


if __name__ == '__main__':
    app.run(debug=True)