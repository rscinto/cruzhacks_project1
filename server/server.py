from flask import Flask, redirect, render_template, request, url_for, jsonify
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


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

            
if __name__ == "__main__":

    app.secret_key = 'LOL MONEY'
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8081
    )