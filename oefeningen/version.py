"""
author: Ralph Mul
date: 13-08-2020
version 1.0
"""

#These are commandes to check versions

warning = "your library is not yet installed!"
installsuggestion = "Please use the following statement in command prompt: pip install -- upgrade "

#Define the set of liberaries to check versions
libraries = ["sklearn", "scipy", "numpy", "pandas", "matplotlib", "seaborn", "graphviz"]
print (libraries)
#try:
for library in libraries:
    libraryVersion = __import__ (library)
    #We test if the liberary is installed if not we print a waringing + suggestion
    try:
#    print(liberay)
        print((library) + ' ' + libraryVersion.__version__)
    except:
        print(warning + ' ' + installsuggestion + library)

""""
Hi all this simple program started with the following statements
import pandas as pd
import nltk as nltk
import sklearn as sklearn
import scipy as scipy
import numpy as numpy
import matplotlib as matplot
import seaborn as seaborn
import graphviz as graph


#pandas version
print("panda" + ' ' + pd.__version__)

#nltk version
print('nltk' + ' ' + nltk.__version__)

#sklearn_version
print('sklearn' + ' ' + sklearn.__version__)

#scipy version
print('scipy' + ' ' + scipy.__version__)

#numpy version
print('numpy' + ' ' + numpy.__version__)

#matplotlib version
print('matplotlib' + ' ' + matplot.__version__)

#seaborn version
print('seaborn' + ' ' + seaborn.__version__)

#graphviz version
print('graphviz' + ' ' + graph.__version__)
"""
