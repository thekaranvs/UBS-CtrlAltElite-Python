from flask import Flask, request, jsonify
from solutions.lazyDev import *

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/lazy-developer', methods=['POST'])
def lazyDev():
  content = request.json
  return jsonify(getNextProbableWords(content['classes'], content['statements']))