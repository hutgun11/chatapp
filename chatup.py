from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_mysqldb import MySQL
import psycopg2 as p

app = Flask(__name__)
# app.config['MYSQL_HOST']='34.87.185.36'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='018034538'
# app.config['MYSQL_DB']='geography'
# mysql= MySQL(app)
app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  list_ex=[['User_Test1','cola'],['User_test2','cola2']]
  return render_template( './ChatApp.html' ,list_ex=list_ex)

def messageRecived():
  print( 'message was received!!!' )
# เรียกใช้โดยกำหนดตัว routeมาที่ 'my event'
@socketio.on( 'my event' ) 
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app,host='0.0.0.0',debug = True )