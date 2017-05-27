##Logging:

Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. 

Python provides logging facility to the modules and applications to log information to a destination.
The destination can be console, file system,


The basic classes defined by the module, together with their functions, are listed below.

	1. Loggers - It exposes the interface that application code use for logging.
	2. Handlers  - sends the log records (created by loggers) to the appropriate destination.
	3. Filters  - Provide a finer grained facility for determining which log records to output.
	4. Formatters specify the layout of log records in the final output.


###Logger object:

This is the primary interface between the application and the logging module. Logger is always instantiated through the module level function logging.getLogger(name)


It has three activities:

- Logger.setLevel()
	- specifies the lowest-severity log message a logger will handle, where debug is the lowest built-in severity level and critical is the highest built-in severity. For example, if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL messages and will ignore DEBUG messages.

- Logger.addHandler() and Logger.removeHandler() 
	- Add and remove handler objects from the logger object.

Logger.addFilter() and Logger.removeFilter() 
	- Add and remove filter objects from the logger object. Filters are covered in more detail in Filter Objects.

Multiple calls to getLogger() with the same name will always return a reference to the same Logger object.

	import  logging
	log = logging.getLogger("test")

###Handlers: 

- Handler objects are responsible for dispatching the appropriate log messages (based on the log messages’ severity) to the handler’s specified destination.
	 
-Logger objects can add zero or more handler objects to themselves with an addHandler() method. As an example scenario, an application may want to send all log messages to a log file, all log messages of error or higher to stdout, and all messages of critical to an email address. This scenario requires three individual handlers where each handler is responsible for sending messages of a specific severity to a specific location.

- The setLevel() method, just as in logger objects, specifies the lowest severity that will be dispatched to the appropriate destination. Why are there two setLevel() methods? The level set in the logger determines which severity of messages it will pass to its handlers. The level set in each handler determines which messages that handler will send on.
	
- setFormatter() selects a Formatter object for this handler to use.
	
- addFilter() and removeFilter() respectively configure and deconfigure filter objects on handlers.


##Formatters:
- Formatter objects define the final order, structure and content of the log messages. The Formatter class takes two arguments - message format string, date format string - both of them optional.

- If there is no message format string, the default is to use the raw message. If there is no date format string, the default date format is: %Y-%m-%d %H:%M:%S

Eg: 	'%(asctime)s - %(levelname)s - %(message)s' - logs in the format time, log level and the message.


## Filters:
 Logger.filter(record)
Applies this logger’s filters to the record and returns a true value if the record is to be processed. The filters are consulted in turn, until one of them returns a false value. If none of them return a false value, the record will be processed (passed to handlers). If one returns a false value, no further processing of the record occurs.


====

Example:

	#Step 1: Import logging module
 	import logging
	
	#Step 2: Create a logger object & Set the debug level to which log records will be generated
 	log = logging.getLogger("Test")
 	log.setLevel(logging.INFO)
	
	#Step 3: Create the handler & Set the debug level
 	fh = logging.FileHandler('spam.log')
 	fh.setLevel(logging.DEBUG)
 	ch = logging.StreamHandler()
 	ch.setLevel(logging.DEBUG)
	
	#Step 4 : Create the formatter object
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	
	#Step 5: Attach the formatter to the handler
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)
	
	# Step 6: Attach the handler to logger
	log.addHandler(fh)
	log.addHandler(ch)

	#Step 7: Start creating log records and send them to logger
	log.info("Testing the info message")
	log.info("testing log 1 ")
	log.debug("Testing debug")



###Log level:

 Level	Numeric value
 CRITICAL	50
 ERROR	40
 WARNING	30
 INFO	20
 DEBUG	10
 NOTSET	0

When a logging method is called on a logger, the logger compares its own level with the level associated with the method call. If the logger’s level is higher than the method call’s, no logging message is actually generated. This is the basic mechanism controlling the verbosity of logging output.

Logging messages are encoded as instances of the LogRecord class. When a logger decides to actually log an event, a LogRecord instance is created from the logging message.



References:
https://docs.python.org/2/howto/logging.html#logging-basic-tutorial