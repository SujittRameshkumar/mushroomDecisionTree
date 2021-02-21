import pandas as pd
import numpy as np
from DataReader import DataReader


attributes = ['cap-shape',
              'cap-surface',
              'cap-color', 
              'bruises?', 
              'odor', 
              'gill-attachment', 
              'gill-spacing', 
              'gill-size', 
              'gill-color', 
              'stalk-shape', 
              'stalk-root', 
              'stalk-surface-above-ring', 
              'stalk-surface-below-ring', 
              'stalk-color-above-ring', 
              'stalk-color-below-ring', 
              'veil-type', 
              'veil-color', 
              'ring-number', 
              'ring-type', 
              'spore-print-color', 
              'population', 
              'habitat'
              ]


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
    
print(pc_entropy)

#Doesn't work, total values are all wrong. Need to account of coefficient total (out of 6000) and smaller total (out of total for that specific attribute i.e 2693 for x)
first_attr_entropy = calculateColumnEntropy(df[1].value_counts().to_list())



# df.iloc[0,0] first row first column 'e'


#this is a dictionary of dictionaries for each attribute. 
#Will be parsing this map to find entropy values for each attribute
all_attribute_dictionaries = {}



def attributeDict(x):
    attr_dict = {}
    for i in range (6000):
        row = df.iloc[i]
        pc = row[0]
        cap_shape = row[x]

        curr_attr = pc + "_" + cap_shape
        if (curr_attr in attr_dict):
            # increment count of that attribute pair by 1
            attr_dict[curr_attr] = attr_dict.get(curr_attr) + 1
        else:
            attr_dict[curr_attr] = 1  
    return attr_dict

# all_attribute_dictionaries[attributes[0]] = attributeDict(0)

for i in range(1,23):
    all_attribute_dictionaries[attributes[i-1]] = attributeDict(i)

print(all_attribute_dictionaries)

