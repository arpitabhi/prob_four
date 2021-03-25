# Problem 4: Following the context of problem 3, set up an application server and do the following:
# 1.  List all employees with their first name and last name and their titles.
# 2.  Provide a list of checkboxes for each title (VP, Director, Manager, etc.) in a form, list the first name and last name of all employees whose titles are selected in the checkboxes.
# 3.  Bonus: Provide a form that could allow you to add Team D to to Manager B of Development under Studio B.

# Hint: You can use nginx as web server and either php7 or python3 as the programing language for the application. Attach the document that instructs how to install the web server, exact php version and python version and MySQL server version and where to put your code to the system. Or you can provide such code and the instruction via GitHub so we can download it from there.


import requests
from fastapi import FastAPI
import mysql.connector

app = FastAPI()


@app.get("/All")
async def get_domain():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="glu_mobile_org"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT EMP.first_name,EMP.last_name,TIT.title FROM employees EMP INNER JOIN titles TIT ON EMP.emp_no=TIT.emp_no")
    myresult = mycursor.fetchall()
    

    


