from random import seed, randint
from string import ascii_lowercase
from datetime import datetime
from acam import Acam as d
from time import time


letters = list(ascii_lowercase)  # Make list of lowercase letters


def createRandomString():
    s = ''
    for l in range(randint(1, 20)):
        s = s + letters[randint(0, len(letters)-1)]
    return s


def t():
    return str(datetime.now())


def elapsed(function):
    def wrapper(*args):
        t1 = time()
        function(*args)
        t2 = time()
        return (t2 - t1)
    return wrapper


@elapsed
def appendTest(toappend):
    for i in range(0, len(testStrings)):
        toappend.append(testStrings[i])


@elapsed
def accessTest(toAccess, nAccessTimes):
    for i in xrange(0, nAccessTimes):
        x = toAccess[i]


@elapsed
def indexTest(toIndex, nIndexTimes):
    for i in indexStrings:
        toIndex.index(i)


@elapsed
def insertTest(toInsert, insertInto):
    for x in toInsert:
        insertInto.insert(0, x)  # Insert x into first index


@elapsed
def popTest(toPop):
    for i in popIndexList[0:100]:
        toPop.pop(i)


@elapsed
def sortTest(toSort):
    s = toSort.sort()


@elapsed
def countTest(toCount, countIn):
    for x in toCount:
        countIn.count(x)

if __name__ == '__main__':
    s = seed('hashthis')  # Use same seed for each test run
    print "Setup [Start] => " + t()
    print "Creating List of 'random' strings values."
    n = 100000  # Number of items in testStrings
    nAccess = 10000  # Number of times to Access
    nIndex = 10000  # Number of index
    testStrings = []
    indexStrings = []
    popIndexList = []
    for i in xrange(n):  # Make random contents for list and Acam
        testStrings.append(createRandomString())
    for i in xrange(nIndex):  # Pick random elements for index speed test
        r = randint(0, len(testStrings))
        s = testStrings[r]
        indexStrings.append(s)
        popIndexList.append(r)
    print "Setup Done => " + t()

    print "\n###############################"
    # Test append speeds
    # list
    print "[Start] Python List Append " + str(n) + " elements => " + t()
    testlist = []
    listappendSpeed = appendTest(testlist)
    print "Elapsed time: " + str(listappendSpeed)
    print "Time/Element: " + str(listappendSpeed/n)
    print "[End]   Python List Append " + str(n) + " elements => " + t()
    # Acam
    print "\n"
    print "[Start] Acam Append " + str(n) + " elements => " + t()
    testAcam = d()
    AcamappendSpeed = appendTest(testAcam)
    print "Elapsed time: " + str(AcamappendSpeed)
    print "Time/Element: " + str(AcamappendSpeed/n)
    print "[End]   Acam Append " + str(n) + " elements => " + t()

    print "\n###############################"
    # Test access speeds
    print "[Start] Python List Access " + str(nAccess) + " elements => " + t()
    listAccessSpeed = accessTest(testlist, nAccess)
    print "Elapsed time: " + str(listAccessSpeed)
    print "Time/Element: " + str(listAccessSpeed/nAccess)
    print "[End]   Python List Access " + str(nAccess) + " elements => " + t()
    # Acam append speed test
    print "\n"
    print "[Start] Acam Access " + str(nAccess) + " elements => " + t()
    AcamAccessSpeed = accessTest(testAcam, nAccess)
    print "Elapsed time: " + str(AcamAccessSpeed)
    print "Time/Element: " + str(AcamAccessSpeed/nAccess)
    print "[End]   Acam Access " + str(nAccess) + " elements => " + t()

    # Test search speeds
    print "\n###############################"
    print "[Start] Python List Index " + str(nIndex) + " elements => " + t()
    listIndexSpeed = indexTest(testlist, nIndex)
    print "Elapsed time: " + str(listIndexSpeed)
    print "Time/Element: " + str(listIndexSpeed/nIndex)
    print "[End]   Python List Index " + str(nIndex) + " elements => " + t()
    # Acam append speed test
    print "\n"
    print "[Start] Acam Index " + str(n) + " elements => " + t()
    AcamIndexSpeed = accessTest(testAcam, nIndex)
    print "Elapsed time: " + str(AcamIndexSpeed)
    print "Time/Element: " + str(AcamIndexSpeed/nIndex)
    print "[End]   Acam Index " + str(nIndex) + " elements => " + t()

    # Test insert speeds
    print "\n###############################"
    toInsert = indexStrings[0:100]
    insertLen = len(toInsert)
    print "[Start] Python List Insert" + str(insertLen) + " elements => " + t()
    listInsertSpeed = insertTest(toInsert, testlist)
    print "Elapsed time: " + str(listInsertSpeed)
    print "Time/Element: " + str(listInsertSpeed/nIndex)
    print "[End]   Python List Insert" + str(insertLen) + " elements => " + t()
    print "\n"
    print "[Start] Acam Insert " + str(insertLen) + " elements => " + t()
    AcamInsertSpeed = insertTest(toInsert, testAcam)
    print "Elapsed time: " + str(AcamInsertSpeed)
    print "Time/Element: " + str(AcamInsertSpeed/nIndex)
    print "[End]   Acam Insert " + str(insertLen) + " elements => " + t()

    # Test pop speeds
    print "\n###############################"
    popLen = len(popIndexList[0:100])
    print "[Start] Python List Pop " + str(popLen) + " elements => " + t()
    listPopSpeed = popTest(testlist)
    print "Elapsed time: " + str(listPopSpeed)
    print "Time/Element: " + str(listPopSpeed/popLen)
    print "[End]   Python List Insert " + str(popLen) + " elements => " + t()
    print "\n"
    print "[Start] Acam Pop " + str(popLen) + " elements => " + t()
    AcamPopSpeed = popTest(testAcam)
    print "Elapsed time: " + str(AcamPopSpeed)
    print "Time/Element: " + str(AcamPopSpeed/popLen)
    print "[End]   Acam Insert " + str(popLen) + " elements => " + t()

    # Test sort speeds
    print "\n###############################"
    listLen = len(testlist)
    AcamLen = len(testAcam)
    print "[Start] Python List Sort " + str(listLen) + " elements => " + t()
    listSortSpeed = sortTest(testlist)
    print "Elapsed time: " + str(listSortSpeed)
    print "Time/Element: " + str(listSortSpeed/listLen)
    print "[End]   Python List Sort " + str(listLen) + " elements => " + t()
    print "\n"
    print "[Start] Acam Sort " + str(AcamLen) + " elements => " + t()
    AcamSortSpeed = sortTest(testAcam)
    print "Elapsed time: " + str(AcamSortSpeed)
    print "Time/Element: " + str(AcamSortSpeed/AcamLen)
    print "[End]   Acam Sort " + str(AcamLen) + " elements => " + t()

    # Test count
    toCount = []
    for i in popIndexList[0:100]:
        toCount.append(testStrings[i])
    print "\n###############################"
    countLen = len(toCount)
    print "[Start] Python List Count " + str(countLen) + " elements => " + t()
    listCountSpeed = countTest(toCount, testlist)
    print "Elapsed time: " + str(listCountSpeed)
    print "Time/Element: " + str(listCountSpeed/countLen)
    print "[End]   Python List Sort " + str(countLen) + " elements => " + t()
    print "\n"
    print "[Start] Acam Count " + str(countLen) + " elements => " + t()
    AcamCountSpeed = countTest(toCount, testAcam)
    print "Elapsed time: " + str(AcamCountSpeed)
    print "Time/Element: " + str(AcamCountSpeed/countLen)
    print "[End]   Acam Count " + str(countLen) + " elements => " + t()
