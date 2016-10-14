from flask import Flask, render_template, redirect, request, jsonify
from flaskext.mysql import MySQL
import bcrypt
import urllib
import urllib2

mysql =  MySQL()
app = Flask(__name__)

# app.config['MYSQL_DATABASE_USER'] = 'x'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
# app.config['MYSQL_DATABASE_DB'] = 'baseball'
# app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# mysql.init_app(app)

# conn = mysql.connect()
# cursor = conn.cursor()

@app.route('/')
def index():
    response = urllib2.urlopen('http://www.espn.com/mlb/scoreboard')
    html = response.read()
    for line in response:
        print "Line Strip", line.rstrip()
    print "The Headers are: ", response.info()
    # print "The Server is: ", response.info()['server']

    return jsonify("The URL is: ", response.geturl(), "This gets the code: ", response.code,  "The Date is: ", response.info()['date'],  "Get all data: ", html, "Get the length :", len(html))

    # Showing that the file object is iterable
    

    # Note that the rstrip strips the trailing newlines and carriage returns before
    # printing the output.



if __name__ == '__main__':
    app.run(debug=True)
