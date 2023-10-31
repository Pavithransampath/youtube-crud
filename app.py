from flask import Flask,render_template
import sqlite3 as sql

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    conn=sql.connect("user.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from list1")
    data=cur.fetchall()
    return render_template("index.html",datas=data)


if __name__ =="__main__":
    app.run(debug=True)