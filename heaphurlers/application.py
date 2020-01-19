from flask import Flask, redirect, render_template, request, url_for, jsonify, send_from_directory
import os
# from flask_simple_geoip import SimpleGeoIP
# from twilio.rest import Client
# from twilio.twiml.messaging_response import MessagingResponse
# from helpers import lookup
# from tweetsearch import get_tweets
import io
# Imports the Google Cloud client library
# from google.cloud import vision
# from google.cloud.vision import types
# import base64
import urllib.request
import requests
# import shutil
# from word2number import w2n
# import time, threading
# import csv


app = Flask(__name__)


app = Flask(__name__,
            static_url_path='', 
#             static_folder='/templates/AudioRecorder',
#             # template_folder='/templates'
            )

@app.route("/")
def index():
    return render_template("Home.html")



@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
    
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route("/record")
def test():
    return render_template("record.html")

            
if __name__ == "__main__":

    app.secret_key = 'LOL MONEY'
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8000
    )