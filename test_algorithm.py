import unittest
from algorithm import bmi

class TestSearch(unittest.TestCase):
    def setUp(self):
        #parameters for metric method
        self.weight = [70,30,100,71]
        self.height = [170,160,163,175]
        self.weightUnequalLength = [70,30]
        self.incorrectWeight = [50,-160, 0,7200]
        self.incorrectHeight = [0,16000,-100,176]

        self.solution = ["normal","underweight","obese","normal"]
        self.incorrectWeightResult = ["underweight","incorrect weight","incorrect weight","incorrect weight"]
        self.incorrectHeightResult = ["incorrect height","incorrect height","incorrect height","normal"]
        
        self.emptyArray = []

        #parameters for imperial (US) method
        self.weightPound = [150]
        self.heightInches = [64]
        self.imperialCorrectSolution = ["overweight"]

        #parameter for is_metric
        self.isMetric = 1
        self.isNotMetric = 0

    #check for the successful result for metric method
    def test_successfulMetric(self):
        self.assertEqual(bmi(self.weight,self.height,self.isMetric),self.solution)

    #check for the successful result for imperial (US) method
    def test_successfulImperial(self):
        self.assertEqual(bmi(self.weightPound,self.heightInches,self.isNotMetric),self.imperialCorrectSolution)

    #check what happens if the weight array is empty
    def test_emptyWeightArray(self):
        self.assertEqual(bmi(self.emptyArray,self.height,self.isMetric),self.emptyArray)

    #check what happens with different array length
    def test_notEqualArraySize(self):
        self.assertEqual(bmi(self.weightUnequalLength,self.height,self.isMetric),self.emptyArray)

    #check with incorrect weight measurements
    def test_incorrectWeightMeasurement(self):
        self.assertEqual(bmi(self.incorrectWeight,self.height,self.isMetric),self.incorrectWeightResult)

    #check with incorrect height measurements
    def test_incorrectHeightMeasurement(self):
        self.assertEqual(bmi(self.weight,self.incorrectHeight,self.isMetric),self.incorrectHeightResult)

if __name__ == '__main__':
    unittest.main()
