from flask import Flask, render_template, Response
import sys
from server import Server

app = Flask(__name__)

server = Server("http://localhost")

@app.route('/')
def index():
    return render_template('index.js')

@app.before_first_request
def before_request_func():
    global client
    client = server.start()
    return "ok"
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/<path:path>')
def dir(path):
    print("called ",path)
    server.send_msg(path,client)
    #client.close()
    print("done")
    return "ok"

if __name__ == '__main__':

    app.run(host='localhost', port=5000, threaded=True, use_reloader=False)
    
    
    

