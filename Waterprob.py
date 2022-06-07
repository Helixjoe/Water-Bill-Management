global total_price

def ALLOT_WATER(app,corp,bore): # function for ALLOT_WATER
    total_water = app * 10 * 30 #we find total water consumed by the appartment
    corp_price = (corp/(corp + bore)) * total_water * 1 # we find total price for corprate water
    bore_price = (bore/(corp + bore)) * total_water * 1.5 # we find total price for borewell water
    total_price = corp_price + bore_price # we find total price by finding sum of corprate and borewell water
    return total_price


option = input("Enter Option")

# First Function
if "ALLOT_WATER" in option: # to read the string recieved as input from user
    app = int(option[12])
    corp = int(option[14])
    bore = int(option[16])
    total_water = ALLOT_WATER(app,corp,bore)# storing it in the variable for calculating BILL
    print(total_water)
