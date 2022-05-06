import json

def cancel(): #to cancel seats for a booking id
 print("Booking_ID(s)",list(dict_list.keys()))
 print("Already booked Seat(s)",list(dict_list.values()))

 cancel_id=input("Enter booking id in which a seat is to be cancelled from the above ids: ")
 print(dict_list[cancel_id])

 cancel_seat=input("Enter index of seat number to be cancelled from the above list: ")
#  print(data)

 del data[cancel_id]["Seat_prices"][cancel_seat]
 #updating the data file
 with open("DictFile.json","w") as f:
     json.dump(data,f)

#-----------------------------------------------------------------------

def existing(): #to know the booked seats
    # print("Existing bookings: ", dict_list)
    existing_Seats = list(dict_list.values())
    flat_list = [num for sublist in existing_Seats for num in sublist]
    # print(flat_list)
    return flat_list

#-----------------------------------------------------------------------

d={}
l=[]
l1=[]
tup1=()
with open("DictFile.json","r") as file: #extracting only the booking id and seat locations
    data = json.load(file)
    for key,value in data.items():
        l1.append(key)
        for keys in value.items():
                tup1=tup1+keys

for i in range(len(tup1)):
 if(type(tup1[i])==type(d)): 
  l.append(list(tup1[i].keys()))

dict_list=dict(zip(l1,l))
