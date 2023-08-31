from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/three")
def three():
    return render_template('three.html')


@socketio.on('message')
def handle_message(data):
    print(data)



if __name__ == "__main__":
    socketio.run(app)
