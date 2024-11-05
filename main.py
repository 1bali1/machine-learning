import numpy
from scipy import stats


def getMedian(): # Dataset sorrendbe helyezett számok közepe (Ha 2 van, akkor a 2 szám átlaga a medián)
    dataset = [3, 5, 7, 1325, 4, 23, 52, 2345, 2, 0, 3]

    median = numpy.median(dataset)

    print(median)


def getMean(): # Átlag
    dataset = [3, 5, 7, 1325, 4, 23, 52, 2345, 2, 0, 3]

    mean = numpy.mean(dataset)

    print(mean)


def getMode(): # Legtöbbet szerpelő szám
    dataset = [3, 5, 7, 3, 3, 3, 1325, 4, 23, 52, 2345, 2, 0, 3]

    mode = stats.mode(dataset)

    print(mode)

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
    a = numpy.square(deviation)
    
    print("Dev: " + str(deviation) + "\nMean: " + str(mean))
    
def getVariance(): # Eltérés
    dataset = [32,111,138,28,59,77,97]
    
    variance = numpy.var(dataset)
    sqrt = numpy.sqrt(variance)
    mean = numpy.mean(dataset)
    deviation = numpy.std(dataset)
    
    print("Var: " + str(variance) + "\n↑ SQRT: " + str(sqrt) + "\nMean: " + str(mean) + "\nDev: " + str(deviation))
    

def getPercentilies(): # A dataset százalék -> hány szám van alatta és felette?
    dataset = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31] 
    # ↑ What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
    
    percentile = numpy.percentile(dataset, 75) # Szóval a dataset 75%-a 43-nál kevesebb vagy az
    
    print(percentile)
    

def createRandomDataset(): # Random dataset generálása
    dataset = numpy.random.uniform(0.0, 5.0, 250)

    print(dataset)
    return dataset

def drawHistogram():
    print("folytatlás")