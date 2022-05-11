# simple-market-making-algorithm
A simple market making algorithm based on a predictive fair value

•	Need to create a market making algorithm where we use a strategy along predictive fair value.
•	I don’t need to consider any fees and quantity must be constant.
•	I will need to extract data from the zip file containing JSON files.
•	I have trade data in CSV and orders data in JSON files for dates from 2020-07-17 to 
2020-07-30.
•	Need to create a data frame with all the orders data from all the dates in a single data frame.
•	Once I have trades and orders data ready, it is time for my strategy.
•	Strategy I want to use is simple, I want to calculate fair value, highest bid price and lowest ask price. My strategy would be for bid position to be somewhere between fair value and highest bid price and ask position to be somewhere between fair value and lowest ask price.
•	For this purpose, I will not need spread. I don’t need spread % too as I will not be adding fees.


Process Flow:

•	For this strategy, I will need the timestamp of orders to be greater than trades. This is because, if we assume otherwise, it will mean that trade has happened with a future time’s orderbook. Anyone can only trade with current orderbook.
•	From the order book, I will have to find out the highest bid and lowest ask for each row.
•	With highest bid and lowest ask available, I will find out fair value.
Fair Value = (Highest bid + Lowest Ask)/2
•	Next is the time for our strategy:
o	Our strategy is to have our bid price at halfway point from fair value to highest bid and ask price at halfway point from fair value to lowest ask
Bid Price = (Fair Value + Highest Bid)/2
Ask Price = (Fair Value + Lowest Ask)/2
•	Once our strategy is defined, it’s time for execution:
o	For the execution of our strategy, we will need last price data from trades.
o	Now for us to execute the bid order, we will need last price to match our bid order (Someone must fill our buy order for it to be executed).
o	For us to execute the ask order, we will need last price to match our ask order (Someone must fill our ask order for it to be executed).
o	This process will be repeated for all the rows and then our final output file will be generated where we have all the positions where our orders are filled.
