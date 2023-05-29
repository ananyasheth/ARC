import numpy as np
from Task import *
from Pair import *
from Grid import *
from ImageMatrix import *
from Fill import *
from Shape import *
from GroupOfShapes import *

taskid = '445eab21'


task = Task(taskid)
task.load()
task.check_shapes()
