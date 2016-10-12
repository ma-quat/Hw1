import unittest
from algorithm import bmi

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.weight = [70,30,100]
        self.weight2 = [70,30]
        self.height = [170,160,163]
        self.incorrectWeight = [50,-160,0]
        self.incorrectHeight = [0,16000,-100]
        self.solution = ["normal","underweight","obese"]


    def test_successful(self):
        self.assertEqual(bmi(self.weight,self.height),self.solution)

    def test_emptyWeightArray(self):
        self.assertEqual(bmi([],self.height),[])

    def test_notEqualArraySize(self):
        self.assertEqual(bmi(self.weight2,self.height),[])

    def test_incorrectWeightMeasurement(self):
        self.assertEqual(bmi(self.incorrectWeight,self.height),["underweight","incorrect weight","incorrect weight"])

    def test_incorrectHeightMeasurement(self):
        self.assertEqual(bmi(self.weight,self.incorrectHeight),["incorrect height","incorrect height","incorrect height"])



if __name__ == '__main__':
    unittest.main()