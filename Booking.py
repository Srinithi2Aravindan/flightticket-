# MAIN DRIVER CODE
import conditions as z1
import cancellation as c1
import secrets
import string
import json

def booking(j,flight_num,class_type,meal):

 no_of_seats = int(input("Enter number of seats: "))
 seat_price = {}
  
#  dicto= {}
 #FOR EACH SEAT BOOKING
 for i in range(no_of_seats): 
  print("\nSeat No: ",i+1)
  seat=input("Enter seat location:(row in number column in alphabet) ")
  alp = c1.existing()
                      # x=0
              # while(x<len(alp)):
              #   if(alp[x]==seat):
              #     print("Seat already booked")
              #   x=x+1   
              
  for k in alp:
    if(seat==k):
        print("Seat already booked")
        quit()
      
  print(seat)
  seat_location=list(seat.split("_"))

  #if user enters 5_f 5 is row and f is column then seat_location is 5th row 6th column
  row=int(seat_location[0]) 
  col=ord(seat_location[1]) - ord('a') + 1

  #TO CHECK THE SEAT IS THERE OR NOT 
  seat_column=z1.seat_exist(row,col,flight_no,class_type)
  seat_column=seat_column[col-1]
  print(seat_column)
  #TICKET PRICE
  if(class_type=='e'):  
   if(seat_column != False):
    if(seat_column == "W" or seat_column == "A"):
     price=j*100+1100
     print("Price for this seat is: ",price)
    else: 
     price=j*100+1000
     print("Price for this seat is: ",price)
  elif(class_type=='b'):
   if(seat_column != False):
    if(seat_column == "W" or seat_column == "A"):
     price=j*100+2100
     print("Price for this seat is: ",price)
    else: 
     price=j*100+2000
     print("Price for this seat is: ",price)

  seat_price[seat]=price

  if(meal=='y'): #meal price
    print(seat," meal ordered")
    meal_cost=200*no_of_seats
  elif(meal=='n'):
    meal_cost=0
    print("Price is INR: ",price)

 #saving data as DICTIONARY to a file
 dict={"Flight_no":flight_num,"class_type":class_type,"Seat_prices":seat_price,"meal":meal,"meal_cost":meal_cost}
 print("Meal cost for this booking is INR: ",meal_cost)
 return dict

#-----------------------------------------------------------------------
def display():
    with open("DictFile.json","r") as f:
        data=json.load(f)
        print(data)
print("WELCOME TO SRINI AIRLINES (CHENNAI TO MANGALORE)\n")
user_choice=int(input("Please enter your choice:(1 for booking,2 for cancellation): "))
if(user_choice==1):
 flight_num = input("Enter flight number:(a101.txt, a102.txt, a103.txt)[as of now] ")
 class_type = input("Enter class:(e-Economy or b-Business) ")
 no_of_bookings = int(input("Enter number of bookings: "))
 meal=input("Do you want a meals for this booking?(y/n)")
 print('\n')
 dicto={}
 id_list =[]

 for i in range(no_of_bookings):
  #id generator
  id = ''.join(secrets.choice(string.ascii_lowercase + string.digits)
                                                  for i in range(4))
  id_list.append(id)

  print("\nYour booking id is: ",str(id))
  dict=booking(i+1,flight_no,class_type,meal)
  dicto[id_list[i]]=dict

 with open("DictFile.json","w") as file:
   json.dump(dicto,file)
elif(user_choice==2):
 c1.cancel()
display()
print('\n')
