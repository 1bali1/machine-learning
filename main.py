import numpy
from scipy import stats
import matplotlib.pyplot as plt

def getMedian(): # Dataset sorrendbe helyezett számok közepe (Ha 2 van, akkor a 2 szám átlaga a medián)
    dataset = [3, 5, 7, 1325, 4, 23, 52, 2345, 2, 0, 3]

    median = numpy.median(dataset)

    print(median)
    return median


def getMean(): # Átlag
    dataset = [3, 5, 7, 1325, 4, 23, 52, 2345, 2, 0, 3]

    mean = numpy.mean(dataset)

    print(mean)
    return mean


def getMode(): # Legtöbbet szerpelő szám
    dataset = [3, 5, 7, 3, 3, 3, 1325, 4, 23, 52, 2345, 2, 0, 3]

    mode = stats.mode(dataset)

    print(mode)
    return mode

def getDeviation(): # Szórás
    """
    dataset = [5, 5, 1, 1, 1]
    á = 2,6 -> átlag
    N = 5 -> adatok száma, hogy mennyi van egy datasetben
    , = alsó index mutató
    ' = felső index mutató
    
    példa: gyök(((5 - 2,6)'2 + (5 - 2,6)'2 + (1 + 2,6)'2 + (1 + 2,6)'2 + (1 + 2,6)'2)/5)
    eredmény = 1,96
    eredmény = 2 +- 1,96
    
    képlet = gyök((X,1 - á)'2 + (X,2 - á)'2/N)
    """
    dataset = [88, 87, 88, 89, 90, 85, 85, 86]
    
    deviation = numpy.std(dataset)
    mean = numpy.mean(dataset)
    
    print("Dev: " + str(deviation) + "\nMean: " + str(mean))
    return deviation
    
def getVariance(): # Eltérés
    dataset = [32,111,138,28,59,77,97]
    
    variance = numpy.var(dataset)
    sqrt = numpy.sqrt(variance)
    mean = numpy.mean(dataset)
    deviation = numpy.std(dataset)
    
    print("Var: " + str(variance) + "\n↑ SQRT: " + str(sqrt) + "\nMean: " + str(mean) + "\nDev: " + str(deviation))
    return variance

def getPercentilies(): # A dataset százalék -> hány szám van alatta és felette?
    dataset = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31] 
    # ↑ What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
    
    percentile = numpy.percentile(dataset, 75) # Szóval a dataset 75%-a 43-nál kevesebb vagy az
    
    print(percentile)
    return percentile
    

def createRandomDataset(): # Random dataset generálása
    dataset = numpy.random.uniform(0.0, 5.0, 100000)

    print(dataset)
    return dataset

def drawHistogram(): # Az átlag és szórás alapján generál grafikont
    dataset = createRandomDataset()
    
    plt.hist(dataset, 100)
    plt.savefig("histogram1.png")

    
def drawScatterPlot(): # Lineáris algebrához kelleni fog, pontokat rakunk le
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    plt.scatter(x, y)
    plt.savefig("scatterplot.png")
    
def drawScatterPlotWithRandomArrays(): # Ugyanaz mint a sima, de random adatokkal
    x = numpy.random.normal(5.0, 1.0, 1000) # Átlag, szórás, elemek száma
    y = numpy.random.normal(10.0, 2.0, 1000)

    plt.scatter(x, y)
    plt.savefig("scatterplot2.png")

# Linear algebra