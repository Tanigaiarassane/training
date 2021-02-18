==> SOAP and WebServices
  - SOAP is a protocol and used for exchanging message between applications.
  - Simple Object Access protocol. It used HTTP to transfer data
  - Supports XML for data exchange
  - Heavy weight / Slow : In XML, we use tags for creating data. So it becomes heavy. Due to this data webcomes heavy and it slows the transaction.
  - Uses WSDL. It will be in xml format and describes the webservice.

==> RESTful services
   - Representation State Transfer
   - Its not a protocol but guideline on how a client should interact with server.
   - RESTful services use HTTP protocol for data exhange between 2 application / machines.
   - Here we can use standard operatoins like GET, POST, PUT, DELETE
   - Light weight and fast
   - Data or funcationality that a client can access from server is called a RESOURCE.
   - Can support different types for request and response like XML,JSON,HTML, TXT, PDF
   - We can use WADL (Webapplication Definition language) or URI to access resource


==> Microservice
  - is it same as REST API? Yes
  - Initial REST services were monolithic - Business layer + Data interface -> Database
  - If we have to deploy, we have to stop the application and deploy it. If some error occurs, we have to recover it completely. High downtime.
   - Microservices - each module is considered as a seperate application and can be deployed sepeartely. Each module will be deployed seperately.
     - Eg: User management, booking module, vedor module. All of them sepearate.
