def ALLOT_WATER(app,corp,bore): # function for ALLOT_WATER
    if(app==2):
        total_water = 3*10*30 #we find total water consumed by the 2BHK appartment 
    elif(app==3):
        total_water = 5*10*30 #we find total water consumed by the 3BHK appartment
    return  total_water

def ADD_GUESTS(g):
    guest_water = g*10*30 # calculating tanker water used by guests
    return guest_water

run="YES"
total_guest_water = 0
while (run=="YES"):
    option = input("Enter Option")
    
    # OPTIONS
    if "ALLOT_WATER" in option: # to read the string recieved as input from user
        app = int(option[12])
        corp = int(option[14])
        bore = int(option[16])
        app_water = ALLOT_WATER(app,corp,bore)# storing it in the variable for calculating BILL
        guests_present = False
    if "ADD_GUESTS" in option:
        if(len(option)==12):
            guest_water = int(option[11])
        else:
            guest_water = int(option[11:13])
        guests_present = True
        total_guest_water += ADD_GUESTS(guest_water)

    if "BILL" in option:
        corp_price = (corp/(corp + bore)) * app_water * 1 # we find total price for corprate water
        bore_price = (bore/(corp + bore)) * app_water * 1.5 # we find total price for borewell water
        total_price = corp_price + bore_price # we find total price by finding sum of corprate and borewell water
        total_water = app_water + total_guest_water
        print(total_price)
        print(total_guest_water)
        if(guests_present==True):
            if( app_water in range(0,501)):
                g_price = total_guest_water * 2
            elif(app_water in range(501,1501)):
                g_price = total_guest_water * 3
            elif(app_water in range(1501,3001)):
                g_price = total_guest_water * 5
            elif(app_water >= 3001):
                g_price = total_guest_water * 8
            print(g_price)
            total_price += g_price
        print(total_water,int(total_price))
        run ='n'
    
    
