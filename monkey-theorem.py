# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:25:45 2019

@author: Maria

Infinite Monkey Theorem
"""
from __future__ import division
import random
import time

start_time = time.time()

# generate list of alphabet letters
alphabet = [chr(letter) for letter in range(97, 123)]
alphabet.append(' ')


def genString(n):
    # n - number of characters in string
    seq = []
    for i in range(n):
        seq.append(alphabet[random.randrange(len(alphabet))]) 
        
    return seq

def scoreString(genStr, testStr):
    testList = list(testStr)
    compareList = [testList[i] == genStr[i] for i in range(len(testList))]
    score = sum(compareList)/len(compareList)
    
    return score

def updateChar(genStr, inds):
    # only update the characters that are wrong
    for i in inds:
        genStr[i] = alphabet[random.randrange(len(alphabet))]
        
    return genStr
    
def genRandomString(n, testString):
    testList = list(testString)
    genStr = genString(n)
    score = scoreString(genStr, testString)
    it = 0
    bestScore = score
    bestString = genStr
    
    while score != 1:
        compareList = [testList[i] == genStr[i] for i in range(len(testList))]
        wrongChar = [i for i, x in enumerate(compareList) if not x] # find wrong characters
        genStr = updateChar(genStr, wrongChar)
        score = scoreString(genStr, testString)
        it += 1
        
        if score > bestScore:
            bestScore = score
            bestString = genStr
            
        if it % 1000 == 0:
            print(bestString)
            print(bestScore)
    
    print(genStr)
    print("The run took %d iterations and %1.8f seconds to complete" % (it, (time.time() - start_time)))
    
genRandomString(28, 'methinks it is like a weasel')

