#cheapest price for all products
def cheapest_prices():
    import csv
    with open('products.csv', 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headers=next(filereader)
        data = []
        for row in filereader:
                data.append(row)
        
        filter = {}
        for item in data:
           if item[2] not in filter.keys():         #First check if dict already has an entry in dict
                   filter[item[2]] = item           #if no entry ad entry, the dict value is a list.
           #Filter Dict Value Explaination:        
           #Index 2 stores the Product Name
           #Index 6 stores the Price of that Product
           elif item[6] == filter[item[2]][6]:      #price is identical, add vendor details to dict
                  filter[item[2]].append(item)      #filter[Product Code]APPEND[New Vendor]

           #If a lower product rate has been found, then reset the value of the dict. 
           #And store new higher price, with it's corresponding vendor details.
           elif item[6] < filter[item[2]][6]:   
                   filter[item[2]] = item

        #Printing cheapest price for products
        for item in filter.keys():
                    print filter[item]

#expensive price for all products                    
def expensive_prices():
    import csv
    with open('products.csv', 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headers=next(filereader)
        data = []
        for row in filereader:
                data.append(row)
        
        filter = {}
        for item in data:
           if item[2] not in filter.keys():         #First check if dict already has an entry in dict
                   filter[item[2]] = item           #if no entry ad entry, the dict value is a list.
           #Filter Dict Value Explaination:        
           #Index 2 stores the Product Name
           #Index 6 stores the Price of that Product
           elif item[6] == filter[item[2]][6]:      #price is identical, add vendor details to dict
                  filter[item[2]].append(item)      #filter[Product Code]APPEND[New Vendor]

           #If a higher product rate has been found, then reset the value of the dict. 
           #And store new higher price, with it's corresponding vendor details.
           elif item[6] > filter[item[2]][6]:   
                   filter[item[2]] = item

        #Printing expensive price for products
        for item in filter.keys():
                    print filter[item]
    
#cheapest price for products with product code                    
def cheapest_prices_pc():
    import csv
    with open('products.csv', 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headers=next(filereader)
        data = []
        
        for row in filereader:
                data.append(row)
        
        filter = {}
        for item in data:
            
           if item[3] not in filter.keys():        #First check if dict already has an entry in dict     
                   filter[item[3]] = item          #if no entry ad entry, the dict value is a list.
           #Filter Dict Value Explaination:        
           #Index 3 stores the Product Code
           #Index 6 stores the Price of that Product        
           elif item[6] == filter[item[3]][6]:     #price is identical, add vendor details to dict  
                  filter[item[3]].append(item)     #filter[Product Code]APPEND[New Vendor] 

           #If a lower product rate has been found, then reset the value of the dict. 
           #And store new lower price, with it's corresponding vendor details.       
           elif item[6] > filter[item[3]][6]:   
                   filter[item[3]] = item
                   
        #Printing cheapest price for products with particular product code           
        for item in filter.keys():
                    if int(item) == 3736:
                        print filter[item]
                    if int(item) == 4356:
                        print filter[item]
                    if int(item) == 3732:
                        print filter[item]
                    if int(item) == 3746:
                        print filter[item]
                    if int(item) == 3759:
                        print filter[item]
                    if int(item) == 3719:
                        print filter[item]
                    if int(item) == 3740:
                        print filter[item]
                    if int(item) == 4341:
                        print filter[item]
                        
# take input from the user
print("1. Cheapest prices")
print("2. Expensive prices")
print("3. Cheapest prices for products [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]")

choice = input("Enter choice(1/2/3):")

if choice == 1:
    cheapest_prices()
    
elif choice == 2:
    expensive_prices()

elif choice == 3:
    cheapest_prices_pc()
    
else:
    print("Invalid Input")

raw_input("Press enter to exit")    

