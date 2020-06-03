#require nltk 
#donwload nltk on nltk.org/install.html

import nltk
nltk.donwload('punkt')
nltk.donwload('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle   #install by pip install pickle-mixin
import numpy as np #install by pip install numpy
from keras.models import Sequential #install by pip install keras
from keras.layers import Dense, Activation, Dropout
from keras.optimizer import SGD 
import random 
