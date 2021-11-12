from flask import Flask, render_template, request 
import hashlib as hl
import datetime 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQALCHEMY_DATABASE_URI"]='sqlite:///'+os.path.join(basedir, 'logfile.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app, db)
url_date=datetime.datetime.now()
class log(db.Model):
    __tablename__ = 'log'
    ID = db.Column('ID',db.Integer, primary_key = True)
    ORIGINAL_LINK = db.Column(db.String(100))
    SHORTEN_LINK = db.Column(db.String(50))
    DATE = db.Column(db.String(50))
    

    def __init__(self, ORIGINAL_LINK, SHORTEN_LINK, DATE):
        self.ORIGINAL_LINK = ORIGINAL_LINK
        self.SHORTEN_LINK = "http://127.0.0.1:5000/"+SHORTEN_LINK
        self.DATE = DATE

    def __repr__(self):
        pass
    
@app.route('/')
def home_get():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def home_post():
    original_url = request.form.get('in_1')
    shorten_url = hl.md5(original_url.encode("utf-8")).hexdigest()[:5][::-1]
    URL = log(ORIGINAL_LINK=original_url,SHORTEN_LINK=shorten_url, DATE=url_date.strftime("%Y-%m-%d"))
    db.session.add(URL)  
    db.session.commit()
    return render_template('index.html', shortenurl = "http://127.0.0.1:5000/"+shorten_url)
@app.route('/history')
def history_get():
    getHistory=db.session.execute("Select * from urllog")
    return render_template('history.html')
if __name__ == "__main__":
    app.run(debug=True)