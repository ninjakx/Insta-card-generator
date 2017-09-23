from get_data import *
import time
from flask import Flask,jsonify,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/",methods=["GET","POST"])
def get_details():
    if request.method == 'POST':
        # Then get the data from the form
        username = request.form['user']

    profile_url,img_url,link,profile_name,detail,posts,followers,following=userprofile(username)

    return render_template("card.html",profile_url=profile_url,img_url=img_url,username=username,profile_name=profile_name,link=link,detail=detail,posts=posts,followers=followers,following=following)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
