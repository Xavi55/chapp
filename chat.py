from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
app=Flask(__name__)

app.config['SECRET_KEY'] = 'omega001'
socketio = SocketIO( app )

@app.route('/')
def index():
	return render_template('chat.html')

@socketio.on('cEvent')
def handler(json):
	#print (str(json))
	#print '%s says, \" %s \"' % (json['user'],json['msg'])
	socketio.emit('reply',json)

if __name__=='__main__':
	#socketio.run( app,debug=False)
    # Fetch the environment variable (so it works on Heroku):
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
