from flask import *
import first_task as ft
import json
app = Flask(__name__)

@app.route("/")
def jump():
   return render_template('jump.html')

@app.route('/user',methods=['POST'])
def user():
    ft.orijson()
    with open("static_json.json", "r") as read_file:
        user = json.load(read_file)
        return render_template('user.html',user = user)

@app.route('/result',methods = ['POST','GET'])
def result():
    user_id = request.form['user_id']
    user_profile = int(request.form['profile_id'])
    user_start_date = request.form['sd_user']
    user_end_date = request.form['ed_user']
    ft.calculate(user_id,user_profile,user_start_date,user_end_date)
    with open("static_json.json", "r") as read_file:
        result = json.load(read_file)
        return render_template('result.html',result= result)


if __name__=='__main__':
    app.run(debug=True)
    