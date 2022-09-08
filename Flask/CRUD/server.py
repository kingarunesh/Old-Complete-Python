from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250))
    phone = db.Column(db.Integer)


db.create_all()

###############################################################
#
#           HOME PAGE
#
###############################################################
@app.route("/")
def home():
    return render_template("index.html")



###############################################################
#
#           ADD new ENTRY
#
###############################################################
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        new_entry = Student(name=name, email=email, phone=phone)

        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for("display"))

    return render_template("add.html")



###############################################################
#
#           DISPLAY
#
###############################################################
@app.route("/display")
def display():
    all_students = Student.query.all()
    return render_template("display.html", students=all_students)



###############################################################
#
#           PROFILE
#
###############################################################
@app.route("/profile/<user_id>")
def profile(user_id):
    data = Student.query.get(user_id)
    return render_template("profile.html", student=data)



###############################################################
#
#           UPDATE PROFILE
#
###############################################################
@app.route("/update-profile/<user_id>", methods=["GET", "POST"])
def update(user_id):
    # data = request.args.get("user_id")
    data = Student.query.get(user_id)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        data.name = name
        data.email = email
        data.phone = phone

        db.session.add(data)
        db.session.commit()

        return redirect(url_for("display"))

    return render_template("update.html", student=data)





###############################################################
#
#           DELETE
#
###############################################################
@app.route('/delete/<user_id>')
def delete(user_id):

    data = Student.query.get(user_id)

    db.session.delete(data)
    db.session.commit()

    return redirect(url_for("display"))




###############################################################
#
#           SEARCH PROFILE
#
###############################################################
@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":
        search_data = request.form["search"]
        filter_data = Student.query.filter_by(email=search_data).first()
        return render_template("search.html", student=filter_data)

    return render_template("search.html", student=None)




if __name__ == "__main__":
    app.run(debug=True)
