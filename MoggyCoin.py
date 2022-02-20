from math import *

import random
from datetime import datetime

import hashlib

import binascii

import time


#_______________________________________________________
def hash1(msg):
    hash_object = hashlib.sha256(msg.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
#_______________________________________________________



# Generate MoggyCoin
#_______________________________________________________

def MineOre(signature,numOfZeros):    
    loop = True
    counter = 0
    random.seed(datetime.now())
    x = str(random.randint(1, 1180591620717411303424))
    while(loop):
        counter = counter + 1

        solution = True

        testHash = hash1(signature + ":" + x + ":" + str(counter))
        
        for i in range(0,numOfZeros):
            if ( testHash[i] != "0" ):
                solution = False
                break

        if (solution == True):
            loop = False

    print("")
    print("""     _/      _/    _/_/      _/_/_/    _/_/_/  _/      _/    _/_/_/    _/_/    _/_/_/  _/      _/  _/  _/   
    _/_/  _/_/  _/    _/  _/        _/          _/  _/    _/        _/    _/    _/    _/_/    _/  _/  _/    
   _/  _/  _/  _/    _/  _/  _/_/  _/  _/_/      _/      _/        _/    _/    _/    _/  _/  _/  _/  _/     
  _/      _/  _/    _/  _/    _/  _/    _/      _/      _/        _/    _/    _/    _/    _/_/              
 _/      _/    _/_/      _/_/_/    _/_/_/      _/        _/_/_/    _/_/    _/_/_/  _/      _/  _/  _/
  01001101 01001111 01000111 01000111 01011001 01000011 01001111 01001001 01001110 00100001 00100001 
....................................................................................................
                                                                                            ALPHA 1.0
IN BINARY WE TRUST!""")        
    print("")
    print("Ore (the raw Proof of work.)")
    print(signature + ":" + x + ":" + str(counter))
    print("")
    print("") 
    print("Validation (Converts Ore and Value into hash.)") 
    print(hash1(signature + ":" + x + ":" + str(counter)))
    print("")
    print("")
    print("It took " + "{:,}".format(counter) + " hashes to figure this out")


#_______________________________________________________About MoggyCoin
def AboutMC():
    print("")
    print("""     _/      _/    _/_/      _/_/_/    _/_/_/  _/      _/    _/_/_/    _/_/    _/_/_/  _/      _/  _/  _/   
    _/_/  _/_/  _/    _/  _/        _/          _/  _/    _/        _/    _/    _/    _/_/    _/  _/  _/    
   _/  _/  _/  _/    _/  _/  _/_/  _/  _/_/      _/      _/        _/    _/    _/    _/  _/  _/  _/  _/     
  _/      _/  _/    _/  _/    _/  _/    _/      _/      _/        _/    _/    _/    _/    _/_/              
 _/      _/    _/_/      _/_/_/    _/_/_/      _/        _/_/_/    _/_/    _/_/_/  _/      _/  _/  _/
  01001101 01001111 01000111 01000111 01011001 01000011 01001111 01001001 01001110 00100001 00100001 
....................................................................................................
                                                                                            ALPHA 1.0
IN BINARY WE TRUST!""")
    print("")
    print("Version Alpha 0.0.1")
    print("")
    print("Copyright (c) Squirrel Computers and Adam Rashid")

#___________________________________________________MintCoin
def MintCoin(Validation, ore):
    print("")
    print("""     _/      _/    _/_/      _/_/_/    _/_/_/  _/      _/    _/_/_/    _/_/    _/_/_/  _/      _/  _/  _/   
    _/_/  _/_/  _/    _/  _/        _/          _/  _/    _/        _/    _/    _/    _/_/    _/  _/  _/    
   _/  _/  _/  _/    _/  _/  _/_/  _/  _/_/      _/      _/        _/    _/    _/    _/  _/  _/  _/  _/     
  _/      _/  _/    _/  _/    _/  _/    _/      _/      _/        _/    _/    _/    _/    _/_/              
 _/      _/    _/_/      _/_/_/    _/_/_/      _/        _/_/_/    _/_/    _/_/_/  _/      _/  _/  _/
  01001101 01001111 01000111 01000111 01011001 01000011 01001111 01001001 01001110 00100001 00100001 
....................................................................................................
                                                                                            ALPHA 1.0
IN BINARY WE TRUST!""")
    print("")
    print("The coin will be saved as (its Validation).MC")
    print("You Now have a MoggyCoin, Yay!!")
    f = open(Validation + ".MC", "x")
    f.write("The ORE is: " + ore + " The Validation is " + Validation)
    
    
