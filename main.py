from flask import session
from flask_socketio import SocketIO
import time
from application import create_app
import config

# Setup

app = create_app()
socketio = SocketIO(app)


if __name__ == "__main__":  # Start the Web Server
    socketio.run(app, debug=True, host=str(config.Config.SERVER))