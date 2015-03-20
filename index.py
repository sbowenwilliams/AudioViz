import os

import beat_tracker
import chroma_amp

# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    chroma_amps = chroma_amp.getXXChromaAmps()
    beats = beat_tracker.getXXBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats, artist=1)

@app.route('/demoXX')
def demoXX():
    chroma_amps = chroma_amp.getXXChromaAmps()
    beats = beat_tracker.getXXBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats, artist=1)

@app.route('/demoDMX')
def demoDMX():
    chroma_amps = chroma_amp.getDMXChromaAmps()
    beats = beat_tracker.getDMXBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats, artist=2)

@app.route('/demoHAIM')
def demoHAIM():
    chroma_amps = chroma_amp.getHAIMChromaAmps()
    beats = beat_tracker.getHAIMBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats, artist=3)


if __name__ == '__main__':
  port = int(os.environ.get('PORT',5000))
  app.run(host='0.0.0.0', port=port)