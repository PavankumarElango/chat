# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:19:01 2020

@author: pavan
"""

#Imports
import techbots
from flask import Flask, render_template, request, jsonify
import nltk
import datetime
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
#from chatbot import chat
stemmer = LancasterStemmer()
#seat_count = 50

with open("data.json",encoding="utf=8") as file:
	data = json.load(file)
with open("data.pickle","rb") as f:
	words, labels, training, output = pickle.load(f)

#Function to process input



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    user_request = request.args.get('msg')  # Fetching input from the user
    user_request = user_request.lower()
    response = techbots.chat(user_request)
    return response
    

if __name__ == "__main__":
    app.run(threaded=False)
    