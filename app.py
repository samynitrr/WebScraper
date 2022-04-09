from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route("/iNeuron", methods=['GET', 'POST'])
def iNeuron_scrape():
    return("whats up!")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)