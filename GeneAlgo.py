# -*- coding: utf-8 -*-
#imports

#imports#

#variables

#variables#

#classes
#Error handling
class Error(Exception):
    """Base Error Class"""
    pass

class GeneTypeError(TypeError):
    def __init__(self,object):
        self.object = object
    def __str__(self):
        return repr("'{}' is of type {}, {} required.".format(self.object,type(self.object),list))

class GeneFormatError(Error):
    def __init__(self,gene):
        self.gene = gene
    def __str__(self):
        return repr("'{}' contains invalid elements, supported elements are (0,1)".format(self.gene))
#Error handling#
class geneAlgo:
    """
    This class will be used with a high-order function as the fitness measurement method,
    working as the generation manipulation procedure, using various genetic algorithm methods
    taken letter-by-letter from the literature(For Genetic Algorithms).

    The function passed for fitness measurement should return a float or intenger.
    """
    def __init__(self,fitnessFunction):
        self.fitnessFunction = fitnessFunction
        return None

class Individual:
    """
    This class will be used to handle single individual operations for each generation.
    """
    def __init__(self,gene):
        if type(gene)!=list:
            raise GeneTypeError(gene)
        for gen in gene:
            if (gen!=0 and gen!=1):
                raise GeneFormatError(gene)
        self.gene = gene
        return None
#classes#

#functions

#functions#

#main
def main():
    return None
#main#
