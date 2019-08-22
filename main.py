from flask import Flask, redirect, url_for, render_template, request, flash
import database as db

app = Flask(__name__)
app.secret_key = "super_secret31415926535"
app.secret = "super_secret11111"


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route("/threads", methods=["GET", "POST"])
def threads_main():
    if request.method == "GET":
        return render_template("threads_main.html",
                               all_threads=db.get_all_threads())
    dmc_thread = request.form['dmc']
    added_successfully = db.add_new_thread(dmc_thread,
                                           request.form['amount_have'])
    if not added_successfully:
        flash("Could not add {}".format(dmc_thread))
        return render_template("threads_main.html",
                               all_threads=db.get_all_threads())
    flash("{} added!".format(dmc_thread))
    return render_template("threads_main.html",
                           all_threads=db.get_all_threads())
