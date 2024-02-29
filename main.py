from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketIo = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
@app.route('/chat.html')
def chat():
    return render_template('chat.html')

@socketIo.on('message')
def handleMessage(msg):
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketIo.run(app, host='0.0.0.0', port='5000',debug=True)
