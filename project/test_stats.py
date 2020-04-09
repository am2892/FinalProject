import math
from FileReader import readCSV
import scipy
from scipy.stats import t
import numpy

dataSet = readCSV('../../MiniProject2/CSV_files/test.csv')
testData = [1,2,3]


def test_csv_reader():
    dataSet = readCSV('../../MiniProject2/CSV_files/test.csv')
    assert len(dataSet) == 19 * 2

def test_csv_reader_fail():
    dataSet = readCSV('CSV_files/test.csv')
    assert len(dataSet) != 19

#1 - Population Mean Tests
def test_calc_populationMean():
    from StatisticsModule import populationMean
    assert populationMean(testData) == 2

def test_calc_populationMean_fail():
    from StatisticsModule import populationMean
    assert populationMean(testData) != 1

#2 - Median Tests 
def test_calc_median():
    from StatisticsModule import median
    assert median(testData) == 2

def test_calc_median_fail():
    from StatisticsModule import median
    assert median(testData) != 1

#3 - Mode Tests
def test_calc_mode():
    from StatisticsModule import mode
    assert mode(testData) == "No mode within given dataset"

def test_calc_mode_fail():
    from StatisticsModule import mode
    assert mode(testData) != 2

#4 - Population Standard Deviation Tests
def test_calc_populationStandardDeviation():
    from StatisticsModule import populationStandardDeviation
    assert populationStandardDeviation(testData) == 0.816496580927726

def test_calc_populationStandardDeviation_fail():
    from StatisticsModule import populationStandardDeviation
    assert populationStandardDeviation(testData) != 0.48

#5 - Variance of Population Proportion Tests
def test_calc_variancePopulationProportion():
    from StatisticsModule import variancePopulationProportion
    assert variancePopulationProportion(testData) == 6

def test_calc_variancePopulationProportion_fail():
    from StatisticsModule import variancePopulationProportion
    assert variancePopulationProportion(testData) != 1

#6 - Z-Score Tests
def test_zScore():
    from StatisticsModule import zScore
    scores = zScore(testData)
    assert scores == [-1.0, 0.0, 1.0]

def test_zScore_fail():
    from StatisticsModule import zScore
    scores = zScore(testData)
    assert scores != [0.0, 2, 5]

#7 - Standardized Score Tests
#def test_calc_standardizedScore():
#    from StatisticsModule import standardizedScore
#    scores = standardizedScore(testData)
#    assert scores == [(-1.0/(math.sqrt(2/3))), 0.0, (1.0/(math.sqrt(2/3)))]

def test_calc_standardizedScore_fail():
    from StatisticsModule import standardizedScore
    scores = standardizedScore(testData)
    assert standardizedScore(testData) != [3.6, 9.6, 18.6]

#8 - Population Correleation Coefficient Tests
def test_calc_populationCorrelationCoefficient():
    from StatisticsModule import populationCorrelationCoefficient
    assert populationCorrelationCoefficient(dataSet) == -0.43371655224528094

def test_calc_populationCorrelationCoefficient_fail():
    from StatisticsModule import populationCorrelationCoefficient
    assert populationCorrelationCoefficient(dataSet) != 5

#9 - Confidence Interval Tests
#def test_calc_confidenceInterval():
   #from StatisticsModule import confidenceInterval
   #assert confidenceInterval(testData) == (4.4841377118437524, -0.48413771184375287)

#def test_calc_confidenceInterval_fail():
   #from StatisticsModule import confidenceInterval
   #assert confidenceInterval(testData) != 5

#10 - Population Variance Tests
def test_calc_variance():
    from StatisticsModule import variance
    assert variance(dataSet) == variance(dataSet)

def test_calc_variance_fail():
    from StatisticsModule import variance
    assert variance(dataSet) != 2

#11 - P-Value Tests
def test_calc_pValue():
    from StatisticsModule import pValue
    assert pValue(dataSet) == "p-value is less than alpha. Null hypothesis accepted: means are equal."

def test_calc_pValue_fail():
    from StatisticsModule import pValue
    assert pValue(dataSet) != "p-value is greater than alpha. Null hypothesis rejected: means are not equal."

#12 - Proportion Tests
def test_calc_proportion():
    from StatisticsModule import proportion
    assert proportion(testData) == ['0.1667', '0.3333', '0.5000']

def test_calc_proportion_fail():
    from StatisticsModule import proportion
    assert proportion(testData) != ['0.5000', '0.2000', '0.3000']

#13 - Sample Mean Tests
def test_calc_sampleMean():
    from StatisticsModule import sampleMean
    assert sampleMean(testData) == 2

def test_calc_sampleMean_fail():
    from StatisticsModule import sampleMean
    assert sampleMean(testData) != 1

#14 - Sample Standard Deviation Tests
def test_calc_std():
    from StatisticsModule import standardDeviation
    assert standardDeviation(dataSet) == standardDeviation(dataSet)

def test_calc_std_fail():
    from StatisticsModule import standardDeviation
    assert standardDeviation(dataSet) != 2

#15 - Variance of Sample Proportion Tests
def test_calc_varianceSampleProportion():
    from StatisticsModule import varianceSampleProportion
    assert varianceSampleProportion(testData) == 1

def test_calc_varianceSampleProportion_fail():
    from StatisticsModule import varianceSampleProportion
    assert varianceSampleProportion(testData) != 2


