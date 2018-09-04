# -*- coding: utf-8 -*-
#imports
import GeneAlgo
#imports#

#variables

#variables#

#classes

#classes#

#functions
def test_Class_Instance():
    newinstance = GeneAlgo.geneAlgo(lambda x:x*x)
    assert isinstance(newinstance,GeneAlgo.geneAlgo)

def test_Class_Fitness_Method():
    fitnessFunc = lambda x:x*x
    newinstance = GeneAlgo.geneAlgo(fitnessFunc)
    assert (type(newinstance.fitnessFunction(3)) == float or type(newinstance.fitnessFunction(3)) == int)
#functions#

#main
def main():
    return None
#main#
