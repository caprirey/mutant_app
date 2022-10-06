import re

def invalid_data(data):
  size_rows = len(data)
  re_str = "[AGCT]"+"{"+str(size_rows)+"}"
  flag = True
  for x in range(size_rows):
    if(re.fullmatch(re_str,data[x]) == None):
      flag = False
      break      
  return flag

def mutant_chain(adn_chain):
  dict = {}
  for x in adn_chain:
    dict[x]=""
    if(len(dict)>=2):
      return False
  return True

def search_x_gene(list2d, list2d_size):
  count_flag = 0
  row = 0
  col = 0  
  visit_axis = {}

  def save_cordenates(row,col,cord):
    if cord == "x":    
        for i in range(4):
          visit_axis[str(row)+","+str(col+i)] = ""      
    if cord == "y":
        for i in range(4):      
          visit_axis[str(row+i)+","+str(col)] = ""            
    if cord == "rd":
        for i in range(4):      
          visit_axis[str(row+i)+","+str(col+i)] = ""  
    if cord == "ld":
        for i in range(4):     
          visit_axis[str(row+i)+","+str(col-i)] = ""

  while(count_flag<=1 and row<list2d_size):    
      #print("Axis: ", str(row) + "," + str(col))      
      if((col+3) < list2d_size):
          if (visit_axis.get(str(row)+","+str(col)) == None):
            if(mutant_chain(list(list2d[row][col]+list2d[row][col+1]+list2d[row][col+2]+list2d[row][col+3]))):
              save_cordenates(row,col,"x")                                    
              count_flag+=1
              # print("search x")
      if((row+3) < list2d_size): 
          if (visit_axis.get(str(row)+","+str(col)) == None):
            if(mutant_chain(list(list2d[row][col]+list2d[row+1][col]+list2d[row+2][col]+list2d[row+3][col]))):
              save_cordenates(row,col,"y")                        
              count_flag+=1
              # print("search y")            
      if((row+3)<list2d_size and (col+3)<list2d_size ):          
          if (visit_axis.get(str(row)+","+str(col)) == None):
            if(mutant_chain(list(list2d[row][col]+list2d[row+1][col+1]+list2d[row+2][col+2]+list2d[row+3][col+3]))):
              save_cordenates(row,col,"rd")
              count_flag+=1
              # print("search rd")                       
      if((row+3)<list2d_size and (col-3)>=0):                          
          if (visit_axis.get(str(row)+","+str(col)) == None):
            if(mutant_chain(list(list2d[row][col]+list2d[row+1][col-1]+list2d[row+2][col-2]+list2d[row+3][col-3]))):            
              save_cordenates(row,col,"ld")               
              count_flag+=1
              # print("search ld")            
      if(col>=(list2d_size-1)):
        row+=1
        col=0
      else:
        col+=1
  return True if(count_flag>1) else False