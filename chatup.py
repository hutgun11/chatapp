from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  list_ex=[['User_Test1','cola'],['User_test2','cola2']]
  return render_template( './ChatApp.html' ,list_ex=list_ex)

def messageRecived():
  print( 'message was received!!!' )
@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app,host='0.0.0.0',debug = True )