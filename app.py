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
    chroma_amps = chroma_amp.getChromaAmps()
    beats = beat_tracker.getBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats)
@app.route('/demoDMX')
def demoDMX():
    chroma_amps = chroma_amp.getChromaAmps()
    beats = beat_tracker.getBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats)
@app.route('/demoHAIM')
def demoHAIM():
    chroma_amps = chroma_amp.getChromaAmps()
    beats = beat_tracker.getBeats()
    print "READY TO RENDER"	
    return render_template('demo.html', data_ca=chroma_amps, data_b=beats)



if __name__ == '__main__':
    app.run(
        debug=True
    )
