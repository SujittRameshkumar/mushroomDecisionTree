import requests
from collections import Counter


class DataReader:
  def __init__(self, url):

    

    self.feature_set = []
    self.data = []
    self.list_of_most_common_value = []
    self.set_of_lines = []


    for i in range(22):
      feature_value_counter = Counter()
      self.feature_set.append(feature_value_counter)

    r = requests.get( url, stream=True )

    
    for line in r.iter_lines():
      line = line.decode('utf-8')
      self.set_of_lines.append(line)

    
  

  def find_most_common_values(self):

    
    for line in self.set_of_lines:
      line_values = line.split(',')
      
      if len(line_values) != 23: 
        continue
      

      y_label = line_values[0]
      x_atributes = line_values[1:]
      
      for i in range(22):
        attribute_val = x_atributes[i]
        if attribute_val !='?':
          self.feature_set[i][attribute_val]+=1

    

    for f in self.feature_set:
      most_frequent_value = f.most_common()[0][0]
      self.list_of_most_common_value.append(most_frequent_value)
     

    
  def read(self):

    self.find_most_common_values()

    
    for line in self.set_of_lines:
      
      line_values = line.split(',')
      
      if len(line_values) != 23: 
        continue

      y_label = [line_values[0]]
      x_atributes = line_values[1:]
      
      for i in range(22):
        attribute_val = x_atributes[i]
        most_common_attribute_value = self.list_of_most_common_value[i]
        if attribute_val =='?':
          x_atributes[i]=most_common_attribute_value
      
      updated_data = y_label + x_atributes
      self.data.append(updated_data)
      

    
    





