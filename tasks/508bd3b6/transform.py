from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    dline = group_of_shapes.fetch_shape(['DLine'])
    dline = dline[0]
    ((x1,y1),(x2,y2)) = dline.points
    hlines = vlines = None
    hlines = group_of_shapes.fetch_shape(['HLine'])
    vlines = group_of_shapes.fetch_shape(['VLine'])
    
    def add_bounce():
      lines = group_of_shapes.bounce((new_x1_l1,new_y1_l1),(new_x2_l1,new_y2_l1),(new_x2_l2,new_y2_l2),3)
      for line in lines:
        group_of_shapes.add_on_top(line)
    
    if hlines == []:            # Vertical Line
      min_y = max_y = None
      for each_line in vlines:
        if min_y is None and max_y is None:
          min_y = each_line.min_y
          max_y = each_line.max_y
          continue
        if min_y>each_line.min_y:
          min_y = each_line.min_y
        if max_y<each_line.max_y:
          max_y = each_line.max_y
    
    if vlines == []:            # Horizontal Line
      min_x = max_x = None
      for each_line in hlines:
        if min_x is None and max_x is None:
          min_x = each_line.min_x
          max_x = each_line.max_x
          continue
        if min_x>each_line.min_x:
          min_x = each_line.min_x
        if max_x<each_line.max_x:
          max_x = each_line.max_x
    

    if x1 < x2 and y1 < y2:      # Diagonal Down Right
      if hlines == [] and max_y>int(background.y_size/2):     # Vertical Line on the right
        new_x1_l1=new_x2_l1=x2+1
        new_y1_l1=new_y2_l1=y2+1
        while(new_y2_l1!=min_y-1):
          new_x2_l1+=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.max_x):
          new_x2_l2+=1
          new_y2_l2-=1
        add_bounce()
        
      
      if hlines == [] and max_y<int(background.y_size/2):      # Vertical Line on the left
        new_x1_l1=new_x2_l1=x1-1
        new_y1_l1=new_y2_l1=y1-1
        while(new_y2_l1!=max_y+1):
          new_x2_l1-=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.min_x):
          new_x2_l2-=1
          new_y2_l2+=1
        add_bounce()
      
      if vlines == [] and max_x>int(background.x_size/2):      # Horizontal Line on the bottom
        new_x1_l1=new_x2_l1=x2+1
        new_y1_l1=new_y2_l1=y2+1
        while(new_x2_l1!=min_x-1):
          new_x2_l1+=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.max_y):
          new_x2_l2-=1
          new_y2_l2+=1
        add_bounce()
        
      if vlines == [] and max_x<int(background.x_size/2):      # Horizontal Line on the top
        new_x1_l1=new_x2_l1=x1-1
        new_y1_l1=new_y2_l1=y1-1
        while(new_x2_l1!=max_x+1):
          new_x2_l1-=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.min_y):
          new_x2_l2+=1
          new_y2_l2-=1
        add_bounce()


    if x1 < x2 and y1 > y2:   # Diagonal Down Left
      if hlines == [] and max_y>int(background.y_size/2):     # Vertical Line on the right
        new_x1_l1=new_x2_l1=x1-1
        new_y1_l1=new_y2_l1=y1+1
        while(new_y2_l1!=min_y-1):
          new_x2_l1-=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.min_x):
          new_x2_l2-=1
          new_y2_l2-=1
        add_bounce()
        
      if hlines == [] and max_y<int(background.y_size/2):      # Vertical Line on the left
        new_x1_l1=new_x2_l1=x2+1
        new_y1_l1=new_y2_l1=y2-1
        while(new_y2_l1!=max_y+1):
          new_x2_l1+=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.max_x):
          new_x2_l2+=1
          new_y2_l2+=1
        add_bounce()
        
      if vlines == [] and max_x>int(background.x_size/2):      # Horizontal Line on the bottom
        new_x1_l1=new_x2_l1=x2+1
        new_y1_l1=new_y2_l1=y2-1
        while(new_x2_l1!=min_x-1):
          new_x2_l1+=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.min_y):
          new_x2_l2-=1
          new_y2_l2-=1
        add_bounce()
        
      if vlines == [] and max_x<int(background.x_size/2):      # Horizontal Line on the top
        new_x1_l1=new_x2_l1=x1-1
        new_y1_l1=new_y2_l1=y1+1
        while(new_x2_l1!=max_x+1):
          new_x2_l1-=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.max_y):
          new_x2_l2+=1
          new_y2_l2+=1
        add_bounce()

    if x1 > x2 and y1 < y2:      # Diagonal Up Right
      if hlines == [] and max_y>int(background.y_size/2):     # Vertical Line on the right
        new_x1_l1=new_x2_l1=x2-1
        new_y1_l1=new_y2_l1=y2+1
        while(new_y2_l1!=min_y-1):
          new_x2_l1-=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.min_x):
          new_x2_l2-=1
          new_y2_l2-=1
        add_bounce()
        
      if hlines == [] and max_y<int(background.y_size/2):      # Vertical Line on the left
        new_x1_l1=new_x2_l1=x1+1
        new_y1_l1=new_y2_l1=y1-1
        while(new_y2_l1!=max_y+1):
          new_x2_l1+=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.max_x):
          new_x2_l2+=1
          new_y2_l2+=1
        add_bounce()
        
      if vlines == [] and max_x>int(background.x_size/2):      # Horizontal Line on the bottom
        new_x1_l1=new_x2_l1=x1+1
        new_y1_l1=new_y2_l1=y1-1
        while(new_x2_l1!=min_x-1):
          new_x2_l1+=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.min_y):
          new_x2_l2-=1
          new_y2_l2-=1
        add_bounce()
        
      if vlines == [] and max_x<int(background.x_size/2):      # Horizontal Line on the top
        new_x1_l1=new_x2_l1=x2-1
        new_y1_l1=new_y2_l1=y2+1
        while(new_x2_l1!=max_x+1):
          new_x2_l1-=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.max_y):
          new_x2_l2+=1
          new_y2_l2+=1
        add_bounce()
 
    if x1 > x2 and y1 > y2:      # Diagonal Up left
      if hlines == [] and max_y>int(background.y_size/2):     # Vertical Line on the right
        new_x1_l1=new_x2_l1=x1+1
        new_y1_l1=new_y2_l1=y1+1
        while(new_y2_l1!=min_y-1):
          new_x2_l1+=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.max_x):
          new_x2_l2+=1
          new_y2_l2-=1
        add_bounce()
        
      if hlines == [] and max_y<int(background.y_size/2):      # Vertical Line on the left
        new_x1_l1=new_x2_l1=x2-1
        new_y1_l1=new_y2_l1=y2-1
        while(new_y2_l1!=max_y+1):
          new_x2_l1-=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_x2_l2!=background.min_x):
          new_x2_l2-=1
          new_y2_l2+=1
        add_bounce()
        
      if vlines == [] and max_x>int(background.x_size/2):      # Horizontal Line on the bottom
        new_x1_l1=new_x2_l1=x1+1
        new_y1_l1=new_y2_l1=y1+1
        while(new_x2_l1!=min_x-1):
          new_x2_l1+=1
          new_y2_l1+=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.max_y):
          new_x2_l2-=1
          new_y2_l2+=1
        add_bounce()
        
      if vlines == [] and max_x<int(background.x_size/2):      # Horizontal Line on the top
        new_x1_l1=new_x2_l1=x2-1
        new_y1_l1=new_y2_l1=y2-1
        while(new_x2_l1!=max_x+1):
          new_x2_l1-=1
          new_y2_l1-=1
        new_x1_l2=new_x2_l2=new_x2_l1
        new_y1_l2=new_y2_l2=new_y2_l1
        while(new_y2_l2!=background.min_y):
          new_x2_l2+=1
          new_y2_l2-=1
        add_bounce()
        
    return (GroupOfShapes([group_of_shapes]))
