
#Class Distribution
# edible: 4208 (51.8%)
# poisonous: 3916 (48.2%)
# total: 8124 instances

column_attr = ['cap-shape',
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


class shroom:
    def __init__(self, columnAttr, attributes):
        i = 0
        self.traits = {}
        for a in attribute:
            self.traits.update({columnAttr[i]: a})
            i+=1 

            


