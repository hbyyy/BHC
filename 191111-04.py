def solutions(list_1, commands): 
     '''list_1 : the input list that will be sliced and sorted 
       commands : contains the parameter to set where to start slicing from and to'''
     
     if len(list_1) > 100 or len(list_1) < 0: 
          print("input list is out of range. length should be between 0 and 100") 
          # The length of the list input should be greater than or equal to 1. 
          # The length of the list input should be less than or equal to 100. 

          return
     else:
          for i in list_1:
               if i < 0 or i > 100:
                    print("list item should be in between 0 and 100")
                    return

     if len(commands) < 0 or len(commands) > 50:                           # Commands length should be greater or equal to 1. 
          print("commands length should be between 0 and 50.")  # Commands length should be less than or equal to 50.
          return                                                                                                  # If the commands does not meet up these two conditions, end function.
          


#     else:                   Each commands elements length shouold be 3. 
#          for                 Each commands elements length shouold be 3. 


     print("The input_list and commands are correct. List will be worked out from now on.")
     
     sliced_list1 = list_1[commands[0] - 1 : commands[1]]
     sorted_list = sorted(sliced_list1)
     nth_number = sorted_list[commands[2]]
     
     return sliced_list1, sorted_list, nth_number

first_list = solutions([1,5,2,6,3,7,4], [2,5,3])


print(first_list)
