from flask import Flask, request, jsonify
from solutions.lazyDev import *
from solutions.greedyMonkey import *
from solutions.digitalColony import *
from solutions.railwayBuilder import *
from solutions.swissbyte import *
from solutions.airportCheckin import *
from solutions.calendarScheduling import *
from solutions.pieChart import *
from solutions.parkingLot import *

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

@app.route('/railway-builder', methods=['POST'])
def railwayBuilder():
   inputData = request.json
   return jsonify(railwayBuilderEntry(inputData))

@app.route('/swissbyte', methods=['POST'])
def swissByte():
  content = request.json
  return jsonify(runCode(content['code'], content['cases']))

@app.route('/airport', methods=['POST'])
def airportCheckin():
   inputData = request.json
   return jsonify(airportCheckinEntry(inputData))

@app.route('/calendar-scheduling', methods=['POST'])
def calendarScheduling():
   inputData = request.json
   return jsonify(schedule_lessons(inputData))

@app.route('/pie-chart', methods=['POST'])
def pieChart():
   inputData = request.json
   return jsonify(pieChartEntry(inputData))

@app.route('/digital-colony', methods=['POST'])
def digitalColony():
   content = request.json
   return jsonify(digitalColonyEntry(content))

@app.route('/parking-lot', methods=['POST'])
def parkingLot():
  content = request.json
  return jsonify(returnProfit(content))

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()