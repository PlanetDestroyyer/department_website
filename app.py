from flask import Flask, render_template, request, redirect, session, url_for, flash
import pandas as pd
import os

app = Flask(__name__, static_url_path='/static')



@app.route("/")
def main():
    return render_template("index.html")

@app.route("/dashboard")
def getinvolved():
    df = pd.read_csv('static/data/new_df.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df = df.head(5)
    df = df.to_dict('records')  
    return render_template("dashboard.html", df=df)


@app.route("/staff")
def aboutus():
    return render_template("staff.html")

@app.route("/notes")
def contactus():
    return render_template("notes.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)
