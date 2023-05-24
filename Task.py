import numpy as np
import requests
import json
from Pair import *
from Grid import *
from ImageMatrix import *

class Task:
  '''
  The Task class represents an ARC task. 
  
  Attributes
  ----------
  taskid : string
    ID of the task.
  train_pairs : list of Pair objects
    A list of training pairs for this ARC task.
  test_pairs : list of Pair objects
    A list of test pairs for this ARC task.
  transform_function : function
    A function for creating an output grid given an input grid.

  Methods
  -------
  self.check_shapes()
    Prints the results of pair.check_shapes() for every pair in train_pairs and
    test_pairs. 
  self.load()
     Populates train_pairs and test_pairs using the copy of ARC stored in 'ARC-master'.
     Updates the shapes attribute of each Grid and populates the transform_function
     attribute using the labelled data stored in 'tasks'. 
  self.loadFromGithub()
    Populates train_pairs and test_pairs using the copy of ARC stored on Github. 
    The shapes attribute of each Grid is set to None. 

  '''

  def __init__(self,taskid,train_pairs=None,test_pairs=None,transform_function=None):
    self.taskid = taskid
    self.train_pairs = train_pairs
    self.test_pairs = test_pairs
    self.transform_function = transform_function

  def check_shapes(self):
    print('\n')
    print(self.taskid+' ...')
    print('checking shapes for all pairs ...')
    for i in range(0,len(self.train_pairs)):
      print('train pair '+str(i))
      self.train_pairs[i].check_shapes()
    for i in range(0,len(self.test_pairs)):
      print('test pair '+str(i))
      self.test_pairs[i].check_shapes()
    print('\n')

  def load(self):
    f = open('ARC-master/data/training/'+self.taskid+'.json')
    self.__processOriginalJSON(f.read())
    f.close()
    self.transform_function = __import__('tasks.'+self.taskid+'.transform', fromlist=['transform']).transform
    for i in range(0,len(self.train_pairs)):
      input_grid_function = __import__('tasks.'+self.taskid+'.train_'+str(i)+'_input_grid',fromlist=['input_grid']).input_grid
      self.train_pairs[i].input_grid.group_of_shapes = input_grid_function()
      self.train_pairs[i].output_grid.group_of_shapes = self.transform_function(self.train_pairs[i].input_grid.group_of_shapes)
    for i in range(0,len(self.test_pairs)):
      input_grid_function = __import__('tasks.'+self.taskid+'.test_'+str(i)+'_input_grid',fromlist=['input_grid']).input_grid
      self.test_pairs[i].input_grid.group_of_shapes = input_grid_function()
      self.test_pairs[i].output_grid.group_of_shapes = self.transform_function(self.test_pairs[i].input_grid.group_of_shapes)

  def loadFromGithub(self):
    url = 'https://raw.githubusercontent.com/fchollet/ARC/master/data/training/'+self.taskid+'.json'
    response = requests.get(url)
    self.__processOriginalJSON(response.text)

  def __processOriginalJSON(self,raw_json):
    data = json.loads(raw_json)
    pairs = {}
    for testOrTrain in ('test','train'):
      pairs[testOrTrain] = []
      for pair_number in range(len(data[testOrTrain])):
        input_grid = Grid(ImageMatrix(np.array(data[testOrTrain][pair_number]['input'])))
        output_grid = Grid(ImageMatrix(np.array(data[testOrTrain][pair_number]['output'])))
        pairs[testOrTrain].append(Pair(input_grid,output_grid))
    self.train_pairs = pairs['train']
    self.test_pairs = pairs['test']
