# **_BIL 588_** - HW 1 Mirun Akyuz

Program calculates The BMI Formula with metric formula

Takes two parameters

1. weight array
2. height array
3. is metric - metric is 1, imperial method is 0  



##How to calculate BMI:
* metric method: bmi = weight in kilograms /(height in meters * height in meters) 
* imperial (US) method: bmi = weight in pounds * 703  /(height in inches * height in inches)

##Evaluation

| BMI	Weight Range  |  Status       |
| :---:               | :---:         |
| (0,18]              | Underweight   |
| (18,25)             | Normal        |
| [25,30)             | Overweight    |
| [30,)               | Obese         |

##Output:
* Result array: calculates bmi for weight[i] and height[i]


##Travis-ci
[![Build Status](https://travis-ci.org/ma-quat/Hw1.svg?branch=master)](https://travis-ci.org/ma-quat/Hw1)

##Demo Site (HEROKU)
https://arcane-oasis-94216.herokuapp.com/bmi_calculator

[![Code Climate](https://codeclimate.com/github/ma-quat/Hw1/badges/gpa.svg)](https://codeclimate.com/github/ma-quat/Hw1)

[![Issue Count](https://codeclimate.com/github/ma-quat/Hw1/badges/issue_count.svg)](https://codeclimate.com/github/ma-quat/Hw1)