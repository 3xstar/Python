from func import getSum
from func import getLength
from func import getAge

def testSum():
    assert getSum(3, 5) == 8

def testLength():
    assert getLength("Са") >= 2

def testAge():
    assert getAge(18) >= 18