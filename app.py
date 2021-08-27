from flask import Flask,render_template,request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_employee():
    return render_template('employee.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO employee(name,addr,city,pin) VALUES(?,?,?,?)", (nm, addr, city, pin))
                con.commit()
                msg="Record Added Successfully"

        except:
            con.rollback()
            msg="error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con=sql.connect("database.db")
    con.row_factory=sql.Row

    cur=con.cursor()

    cur.execute("select * from employee")

    rows=cur.fetchall()

    return render_template("list.html",rows=rows)

@app.route('/update',methods=['POST','GET'])
def update():
     if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE employee SET addr=?,city=?,pin=? WHERE name=?", (addr, city, pin, nm))
            con.commit()
            msg= "Record Updated Successfully"

     return render_template("update.html")

@app.route('/delete/<string:nm>')
def delete(nm):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM employee WHERE name=?", nm)
        con.commit()
        msg = "Record Deleted Successfully"

if __name__ == '__main__':
    app.run(debug=True)




