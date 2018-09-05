# -*- coding: utf-8 -*-
#imports
import GeneAlgo
from random import randint
#imports#

#variables

#variables#

#classes

#classes#

#functions
def test_gene_Algo_Instance():
    newinstance = GeneAlgo.geneAlgo(lambda x:x*x)
    assert isinstance(newinstance,GeneAlgo.geneAlgo)

def test_individual_Instance():
    newinstance = GeneAlgo.Individual([1])
    assert isinstance(newinstance,GeneAlgo.Individual)

def test_Individual_Gene_Format():
    gene = [randint(0,1) for val in range(10)]
    newinstance = GeneAlgo.Individual(gene)
#functions#

#main
def main():
    return None
#main#
