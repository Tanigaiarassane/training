REQUEST API methods:

The methods define what type of request we send to server
1. GET - Fetch data from webservice/API
2. POST - Add new data/resource to application
3. PUT - Update data into application
4. DELETE - Delete data in application
5. PATCH - Similar to PUT, but will require only the updated data to be sent.

Other methods
Request will get header ad body as the response.

If you want to get only the header, use
6. HEAD - Fetch only header data from the application
7. OPTIONS - To find out which request method a server supports. ( Allow: OPTIONS, GET, HEAD, POST)
8. TRACE - Used for debugging. This method performs a message look back; meaning sender will return message content as Response.


REST API with parameters:
htttp://googleaps.cpm/?name=cybermentors&year=2020

Data will be attached as parameters and send to server/
