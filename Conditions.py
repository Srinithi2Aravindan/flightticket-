# 1_to get the seats' number of rows and columns of the flight---------------
def rows_colums(x): 
    list1 = x.rsplit(",",1) #splits the string into two parts from right
    rows = list1[1]
    columns = list1[0]
    columns = columns[1:-1]
    columns = columns.replace(" ", "")
    columns = columns.split(",")
    return rows, columns



#2_to get the structure of the flight---------------------------------
def flight_structure(flight_no,class_type): 
 try:
  with open(flight_no) as f: #opens structure of flight
    x=f.readline() #reads the first line , x stands for business class(A101)
    rows_x,columns_x=rows_colums(x)
    y=f.readline() #reads the second line , y stands for economy class(A101)
    rows_y,columns_y=rows_colums(y)
    if(class_type == "b"):
        return rows_x,columns_x
    elif(class_type == "e"):
        return rows_y,columns_y
 #end of A101
#  elif(flight_no == "a102"):
#   with open("a102.txt") as f: #opens structure of flight A102
#     x=f.readline() #reads the first line , x stands for business class(A101)
#     rows_x,columns_x=rows_colums(x)
#     y=f.readline() #reads the second line , y stands for economy class(A101)
#     rows_y,columns_y=rows_colums(y)
#     if(class_type == "b"):
#         return rows_x,columns_x
#     elif(class_type == "e"):
#         return rows_y,columns_y

 except: print("Flight not available")



#3_to convert columns to type of seat
def convert_to_type(column):
 s = column
 res = []
 for idx, val in enumerate(s):
    cols = range(val)

    # for leftside columns
    if(idx == 0):
        res.append('W')
        for col in cols[1:-1]:
            res.append('M')
        res.append('A')

    # for rightside colums
    elif(idx == len(s)-1):
        res.append('A')
        for col in cols[1:-1]:
            res.append('M')
        res.append('W')

    #for middle columns
    else:
        res.append('A')
        for col in cols[1:-1]:
            res.append('M')
        res.append('A')
 return res


#4_to check if the seat exists or not
def seat_exist(row,col,flight_no,class_type):
    rows,columns = flight_structure(flight_no,class_type) #get the structure of the flight
    rows=int(rows)
    columns = [int(col) for col in columns]
    columns=convert_to_type(columns)
    print("Your column look like:",columns)
    if(row<=rows and col<=len(columns)): #check if the entered seat is in the range of the flight
        return columns #for example ['w','A','A','M','W']
    else:
        return False
