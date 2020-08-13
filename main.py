# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:33:18 2020

@author: dhk13
"""
from flask import Flask, jsonify, request
import tensorflow as tf
import numpy as np

# from config import basedir

# import requests

app = Flask(__name__)


@app.route('/')
def index():

    return "hello"



@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        print("0")
        result=request.json
        print(result)
        angles=[]
        angles.append(np.array([float(result['0']), float(result['1']), float(result['2'])]))
        angles=np.array(angles)
        print("1")
        print(angles)
        model = tf.keras.models.load_model("mymodel2.h5")
        print("model loaded")
        pred = model.predict(angles)
        print(pred)
        result={}
        result['0']=str(pred[0][0])
        result['1']=str(pred[0][1])
    return result


if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=5000)

