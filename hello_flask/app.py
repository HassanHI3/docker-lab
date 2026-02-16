
# This is a simple web application that uses flask framework to create a web server that listens on

# Built and containerized a hello world web application using flask framework

# now we will link this flask application to a my_sql database container

# port 5002 and responds with "Hello, World!" when the root URL ("/") is accessed.



from flask import Flask      # creating a Flask application instance and importing flask library.
import MySQLdb               # importing the MySQLdb library to interact with a MySQL database and able to use sql commands in python code


app = Flask(__name__)        # docker networking allows for name of containers to be used to connect to each other instead of using IP addresses.
@app.route('/')             # defines the route for the root URL
def hello_world():
    # Connect to the MySQL database with these credentials
    db = MySQLdb.connect(
        host="mydb",    # Hostname of the MySQL container we'll set up in the docker-compose file
        user="root",    # Username to connect to MySQL
        passwd="my-secret-pw",  # Password for the MySQL user
        db="mysql"      # Name of the database to connect to
    )
    cur = db.cursor() # simple query to get the MySQL version to confirm that the connection is working and we can execute SQL commands.
    cur.execute("SELECT VERSION()") # execute the SQL command to get the MySQL version on page load and display it on the webpage.
    version = cur.fetchone()
    return f'Hello, World! MySQL version: {version[0]}'

if  __name__ == '__main__':              # checking if the application is being run directly (as the main program)
    app.run(host='0.0.0.0', port=5002)   #localhost:5002 will be the URL used to access this application on a web browser.
