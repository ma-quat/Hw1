from flask import Flask
from flask import render_template
from flask import request
from algorithm import *

import yaml


app = Flask(__name__)

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

@app.route('/')
def demo():  
    return 'BMI Calculator'


@app.route('/bmi_calculator', methods=['GET', 'POST'])
def compute():
	if request.method == 'GET':
		    return render_template('bmi_calculator.html')
	
	weight_array = request.form['weight_array']
	app.logger.debug(weight_array)
	height_array = request.form['height_array']
	app.logger.debug(height_array)

	print ('weight_array: ' + weight_array)
	print ('height_array: ' + height_array)

	is_metric = request.form['is_metric']
	app.logger.debug(is_metric)
	print ('is_metric: ' + is_metric)

	yamlWeight = yaml.safe_load(weight_array)
	app.logger.debug(yamlWeight)
	print ('yamlWeight: ' + str(yamlWeight))
	print (yamlWeight)

	yamlHeight = yaml.safe_load(height_array)
	app.logger.debug(yamlHeight)
	print ('yamlHeight: ' + str(yamlHeight))
	print (yamlHeight)
        
	result = bmi(yamlWeight, yamlHeight,is_metric)
	print (result)
	
	printed_result = ("weight_array: " + str(yamlWeight) + " height_array: " + str(yamlHeight) + " method: " + str(is_metric) + " result: "+ str(result))
	return render_template('bmi_calculator.html', result=printed_result)
