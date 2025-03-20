from flask import Flask, render_template
from flask_socketio import SocketIO, send
from blockchain import Blockchain

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# create Blockchain
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")
    
    # save in blockchain
    block = blockchain.create_block(data=msg, sender="User")

    # send back msg to all client
    send({'message': msg, 'hash': block['hash'], 'sender': "User"}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
