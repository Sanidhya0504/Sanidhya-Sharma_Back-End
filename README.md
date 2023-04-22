# Sanidhya Sharma - Back End Assignment - Steeleye
A REST API with endpoints serving Trade data from a mocked database.

### Link to FrontEnd Engineer Assignment
[https://github.com/Sanidhya0504/Sanidhya-Sharma-Front-End](https://github.com/Sanidhya0504/Sanidhya-Sharma-Front-End)
# API Developer Assessment
### Deployment: 
[https://backend-assignment-steeleye.onrender.com/docs](https://backend-assignment-steeleye.onrender.com/docs)
## Database
A json file has been used to store data and act as a mocked database. The file contains 14 trades generated according to the provided schema model.
The data.json file contains a list of trade objects, where each trade object represents a single trade. Each trade object has several fields that describe the trade: `assetClass`
`counterparty`
`instrumentId`
`instrumentName`
`tradeDateTime`
`tradeDetails`
`buySellIndicator`
`price`
`quantity`
`tradeId`
`trader`.

## Listing trades
Endpoint: `/all`

The `listing_trades()` function returns all the values fetched through the database.

## Single trade
Endpoint: `/trade/{trade_id}`

The `search_trade()` function takes path parameter `trade_id` and searches the database for matching id.

### Exception handling:

If passed value is not a number:

Status code `400` - detail="Bad Request, tradeId can only contain numbers"

If trade_id is not present in the database:

Status code `404` - detail="Id Not Found"

## Searching trades
Endpoint: `/searchTrades`

The `search_trade()` function takes a query parameter `search`, searches for its value in `counterparty`
`instrumentId`
`instrumentName`
`trader` and return any trades where the text exists in any of the listed fields.
### Exception handling:
Status code `404`, detail="Trades Not Found, check for typos or upper and lower case"


## Advanced filtering
Endpoint: `/filterTrades`

The `filter_trades()` function takes 6 optional query parameters, `assetclass` `end` `start` `minprice` `maxprice` `tradetype`. The function filters the data based on the query parameters received. 

Query parameters:

`assetclass` (optional): The asset class of the trade.

`end` (optional): The maximum date for the tradeDateTime field.

`maxprice` (optional): The maximum value for the tradeDetails.price field.

`minprice` (optional): The minimum value for the tradeDetails.price field.

`start` (optional): The minimum date for the tradeDateTime field.

`tradetype` (optional): The tradeDetails.buySellIndicator is a BUY or SELL.

## Bonus Task - Pagination and Sorting

Endpoint: `/pages`

The `paginate()` function takes 4 Optional query parameters. Sorting can be done using `tradeDetails.price` `tradeDetails.quantity` and `tradeDateTime`. Specified number of trades per page will be returned by the function.

`page_size` (optional, integer): The number of trades to return per page. Must be greater than 0. Default is 10.

`page_number` (optional, integer): The page number to return. Must be greater than 0. Default is 1.

`sort_by` (optional, string): The field to sort by (e.g. tradeDateTime, price, quantity).

`sort_order` (optional, string): The sort order (asc or desc).


## CORS middleware
To enable cross-origin resource sharing (CORS), the application uses the fastapi.middleware.cors.CORSMiddleware middleware. This middleware adds the necessary headers to the response to allow cross-origin requests. In this case, the middleware is configured to allow all origins, credentials, methods, and headers.
## Error handling
The application uses the HTTPException class from fastapi to handle errors. If an error occurs, such as an invalid request or a resource not found, the application raises an HTTPException with the appropriate status code and detail message.