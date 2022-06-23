from flask import Flask
import socket
import pymysql.cursors


app = Flask(__name__)

@app.route('/')
def index():
    try:
        container_name= socket.gethostname()
        # Connect to the database
        connection = pymysql.connect(host='db.local',
                             user='root',
                             password='password',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)
        if connection:
           return  f"{container_name}, DB Connection is established"
    except Exception as err:
        return container_name + " "+str(err) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)
        
