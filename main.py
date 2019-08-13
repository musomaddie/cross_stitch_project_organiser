from flask import Flask, redirect, url_for, render_template, request, flash
import database as db

app = Flask(__name__)
app.secret_key = "super_secret31415926535"
app.secret = "super_secret11111"


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/threads')
def threads_main():
    return render_template("threads_main.html")


@app.route("/threads/add", methods=["GET", "POST"])
def threads_add():
    if request.method == "GET":
        return render_template("threads_add.html")
    dmc_thread = request.form['dmc']
    added_successfully = db.add_new_thread(dmc_thread,
                                           request.form['amount_have'])
    if not added_successfully:
        flash("Could not add {}".format(dmc_thread))
        return render_template("threads_add.html")
    flash("{} added!".format(dmc_thread))
    return render_template("threads_add.html")
