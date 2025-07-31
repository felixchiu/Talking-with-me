from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' # Replace with a strong secret key
socketio = SocketIO(app, cors_allowed_origins="*")

# Track connected users
connected_users = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    connected_users.add(request.sid)
    emit('user_count', len(connected_users), broadcast=True)
    print(f'Client connected. Total users: {len(connected_users)}')

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    connected_users.discard(request.sid)
    emit('user_count', len(connected_users), broadcast=True)
    print(f'Client disconnected. Total users: {len(connected_users)}')

@socketio.on('message_from_client')
def handle_message(data):
    """Handle incoming messages from clients"""
    print(f'Received message: {data}')
    
    # Broadcast message to all connected clients
    emit('message_from_server', data, broadcast=True)
    
    # Log the message (optional)
    print(f'Broadcasted message to {len(connected_users)} users')

@socketio.on('join')
def handle_join(data):
    """Handle room joining"""
    room = data.get('room', 'default')
    join_room(room)
    emit('status', {'msg': f'Joined room: {room}'}, room=room)

@socketio.on('leave')
def handle_leave(data):
    """Handle room leaving"""
    room = data.get('room', 'default')
    leave_room(room)
    emit('status', {'msg': f'Left room: {room}'}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
