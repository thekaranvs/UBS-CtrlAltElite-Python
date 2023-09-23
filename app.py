from flask import Flask, request, jsonify
from solutions.lazyDev import *
from solutions.greedyMonkey import *
from solutions.digitalColony import *
from solutions.railwayBuilder import *

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

@app.route('/greedymonkey', methods=['POST'])
def greedyMonkey():
  text = request.get_data(as_text=True)
  return returnFruits(text)

@app.route('/evaluate', methods=['POST'])
def railwayBuilder():
   inputData = request.json
   return jsonify(railwayBuilderEntry(inputData))

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

@app.route('/digital-colony', methods=['POST'])
def digitalColony():
   content = request.json
   return jsonify(digitalColonyEntry(content))

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()