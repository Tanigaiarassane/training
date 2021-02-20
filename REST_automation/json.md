In this course, we are going to use Request and Response in JSON format, so if we are aware about JSON and JSON path, it will be very easy for us to process our request and response data

#json
During POST and GET request we need to send data in JSONf format.
JSON Format:
- Javascript object Notation
- Syntax for storing and exchanging data
- Data is placed in json in the format of key value pair
- value can be an array
- Value can be further key value




{
"Name":"Ramesh",
"salary": 23,
"departments":["Maths", "Physics", "Chemistry"],
"address":
        { "streetname":"III Cross",
           "Area":"Sankardas swamigal nagar"
        }

}


#json path:
We can navigate to the different element uniquely in the json file. 
if you want to check for specific value in a key, we can use jsoan path.

How to write json path:
Goto jsonpath.com
$.phoneNumbers

complex json path - accessing array and object

Accessing arrays:
$.departments[0]

Accessing key value object
$.address.streetname

#json parsing using python
- parse dictionary to json (in string)
import json
test = '{"name":"first"}'
v = json.loads(test)
print (v)  


- parse json to dictionary

