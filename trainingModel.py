import pandas as pd
import numpy as np
import decisionTree as dt 

class trainingModel:
    trainingData = pd.read_csv('./data/train.csv')
    
    rootNode: dt = none 