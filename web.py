#!/usr/bin/env python
import os
import shutil
from flask import Flask, render_template, request, \
    Response, send_file, redirect, url_for
from camera import Camera

app = Flask(__name__)
camera = None
mail_server = None
mail_conf = "static/mail_conf.json"

def get_camera():
    global camera
    if not camera:
        camera = Camera()

    return camera

# def get_mail_server():
#     global mail_server
#     if not mail_server:
#         mail_server = Email(mail_conf)
#
#     return mail_server

@app.route('/')
def root():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_feed()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed/')
def video_feed():
    camera = get_camera()
    return Response(gen(camera),
        mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)