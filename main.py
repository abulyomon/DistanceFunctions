def validate_distance_function(f, x, y):
  if(f(x,y) >= 0 and f(x,x) == 0):
    print("function passes positivity")
    if(f(x,y) == f(y,x)):
      print("function is symmetric")
      #Triangle law test TBC
      return True
    else:
      print("function is asymmetic")
      return False
  else:
    print("function fails positivity test")
    return False
  
normal_distance = lambda x, y: pow(pow((y - x), 2), 0.5)
control_distance = lambda x, y: x + y

valid = validate_distance_function(normal_distance, 5, 7)

print ("The function: normal_distance validation as a distance function is:", valid)

valid = validate_distance_function(control_distance, 5, 7)

print ("The function: control_distance validation as a distance function is:", valid)