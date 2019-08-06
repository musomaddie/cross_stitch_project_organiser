from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)
app.secret_key = "super_secret31415926535"
app.secret = "super_secret11111"


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/threads')
def threads_main():
    return render_template("threads_main.html")
