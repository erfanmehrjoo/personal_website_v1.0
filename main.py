from flask import Flask , render_template , request , redirect , session  , request 
from flask_mail import Mail , Message
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint, column, true
from hackernew import hackernews
import requests
from bs4 import BeautifulSoup as bs4
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite3:///personal.db'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '97e041d5e367c7'
app.config['MAIL_PASSWORD'] = 'cfaf5b99f8bafb'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
db = SQLAlchemy(app)

#main webapp landing page
@app.route("/" , methods=["POST" , "GET"])
@app.route("/home" , methods=["POST" , "GET"])
def main():
    return render_template("index.html")
#about page for more connrcting socilal media way
@app.route("/about" , methods=["POST" , "GET"])
def about():
    return render_template("about.html")
#showing the top 10 of the imdb movie
@app.route("/top10" , methods=["POST" , "GET"])
def top10():
    return render_template("top10.html")
#shoing my prodect for making the more money
@app.route("/imdb" , methods=["POST" , "GET"])
def imdb():
    url = "https://www.imdb.com/chart/top/"
    site = requests.get(url)
    soup = bs4(site.content, 'html.parser')
    result = soup.find_all("td" , class_="titleColumn")
    title = []
    for i in result:
        title.append(i.get_text())
    final_title = []
    for i in title:
        i = i.replace(" " , "")
        j = i.replace("\n" , "")
        final_title.append(j)
    
    result2 = soup.find_all("td" , class_="ratingColumn imdbRating")
    score = []
    for i in result2:
        score.append(i.get_text())
    final_score = []
    for i in score:
        i = i.replace("\n" , "")
        final_score.append(i)
        
    title = final_title
    score = final_score
    numbers = 0
    return render_template("imdb.html" , title=title , score=score , count=numbers)

@app.route("/contact" , methods=["POST" , "GET"])
def contact():
    name = request.form.get("name")
    return render_template("contact.html" , name=name)

@app.route("/test" , methods=["POST" , "GET"])
def test():
    return render_template("test.html")





if __name__ == "__main__":
    app.run(debug=True)
