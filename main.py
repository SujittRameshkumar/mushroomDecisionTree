import pandas as pd
import numpy as np
from DataReader import DataReader




def entropy(p_i):
    return -(p_i)*np.log2(p_i)


def calculateColumnEntropy(column_counts):

    probabilities = []

    #get total count for current column
    total = 0
    for column in column_counts:
        total += column
    # print("total",  total)

    #get list of probabilities for each possible attribute
    for item_count in column_counts:
        p = item_count/total
        probabilities.append(p)
    # print("probs", probabilities)

    column_entropy = 0
    for p_i in probabilities:
        column_entropy += entropy(p_i)
    # print("column_entropy", column_entropy)

    return column_entropy


#accessing training data and setting up data frame
train_data_url = 'https://raw.githubusercontent.com/jeniyat/CSE-5521-SP21/master/HW/HW1/Data/train.csv'
dr = DataReader(train_data_url)
dr.read()

df = pd.DataFrame(dr.data)

#CALCULATING ENTROPY OF PREDICTION COLUMN

#getting edible column's counts of values
edible_col = df[0].value_counts().to_list()

probabilities = []

#get total count for current column
total = 0
for column in edible_col:
    total += column

#get list of probabilites for each possible attribute
for item_count in edible_col:
    p = item_count/total
    probabilities.append(p)

pc_entropy = 0
for p_i in probabilities:
    pc_entropy += entropy(p_i)
    


#Doesn't work, total values are all wrong. Need to account of coefficient total (out of 6000) and smaller total (out of total for that specific attribute i.e 2693 for x)
first_attr_entropy = calculateColumnEntropy(df[1].value_counts().to_list())


attr_dict = {}

for data in df.iterrows():
    print(data[1])
