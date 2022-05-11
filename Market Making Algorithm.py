import pandas as pd
import json
import datetime
#Importing necessary libraries needed.

order_books = ['2020-07-'+str(x)+".json" for x in range(17,31,1)]
#Creating order books with names of .json files available in iota_btc file.

order_books

trades = pd.read_csv("trades.csv")
trades
#Reading in the trades data

for y in order_books:
    orders = pd.read_json("binance_iotabtc_orderbooks_json/"+y)
    for i in range(0,len(orders),1):
        orders["asks"][i] = json.loads(orders["asks"][i])
        orders["bids"][i] = json.loads(orders["bids"][i])
    if y =='2020-07-17.json':
        orders_final = pd.DataFrame(orders)
    else:
        orders_final = orders_final.append(orders, ignore_index = True)
        
#Read the json files into orders,
#converted asks and bids columns in to python objects from strings using json.loads,
#as we cannot use strings in later code to find out highest bid and lowest ask.
#Creating a dataframe of orders with 1st order book and storing it to orders_final,
#And then appending rest of the order books into orders_final

orders_final

Fills = pd.DataFrame(columns=['Bids','Asks','Price'])
#Creating an empty dataframe for our final fills data.

for index, rows in trades.iterrows():
    timestamp1 = rows['timestamp']
    lastprice = rows['price']
    
    #Getting timestamp and last price from trades for every row.
    
    for index, rows1 in orders_final.iterrows():
        timestamp2 = rows1['lastUpdated']
        
        #Getting timestamp from orders_final dataframa which is stored in lastUpdated column
        
        if datetime.datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S.%f'):
            break
            
        #timestamp of trades should be less than timestamp of orders. We cannot place a trade at future timestamp of an orderbook.  
            
        highestbid = max(orders_final["bids"][index])[0]
        
        #Calculating the highest bid from bids column of orders_final dataframe by taking the max price of the bids for every row.
        #Had to use index slicer in the end with [0] as there is also, I'm assuming quantity along with price.
        
        lowestask = min(orders_final["asks"][index])[0]
        
        #Calculating the lowest ask from asks column of orders_final dataframe by taking the min price of the asks for every row.
        #Had to use index slicer in the end with [0] as there is also, I'm assuming quantity along with price.
        
        fair_value = (highestbid + lowestask)/2
        
        #Calculating the fairvalue as per formula.
     
        bid = (fair_value + highestbid)/2
        ask = (fair_value + lowestask)/2
        
        #Our simple strategy is to have our bid and ask orders at halfway between fair value and highest bid/lowest ask.
        #Did not calculate spread as I do not need it for my strategy.
        
        if bid == lastprice:
            Fills = Fills.append({'Bids' : 1, 'Asks' : 0, 'Price' : lastprice}, 
                ignore_index = True)
            
            #If the last price matches our bid price, our bid order gets filled with quantity of 1.
            
        elif ask == lastprice:
            Fills = Fills.append({'Bids' : 0, 'Asks' : 1, 'Price' : lastprice}, 
                ignore_index = True)
            
            #If the last price matches our ask price, our ask order gets filled with quantity of 1
            
Fills

Fills.to_csv('Fills.csv')