# dgws-api
A convenience Python wrapper for the DiscoveryGate Web Service (DGWS).

What is this for?
-----------
The aim of the project is to create wrapping functions with few parameters for some of the most used services of DGWS that will allow us to call them easier.
The project does not aim to work with all available services, nor does it aim to allow complete customization of the service calls.

Important to know before use
------------
DGWS requires a **commercial license key** to access. Without a license key, the API refuses all calls.
The [Developer's guide](https://www.discoverygate.com/webservice_docs/1.2/docs/devguide/wwhelp/wwhimpl/js/html/wwhelp.htm#href=dgws-wiki-tutorial.html#3238859) has a trial license key in one of their tutorials for trying out the API, but it is limited in use, possibly (I haven't tried it out yet).

How to install
-----------
To be added

How to use
-----------
Main functionality is contained in functions. Simply import the functions you need, supply the parameters, and the function will return the server's response after being parsed by Zeep.

Other python modules used
------------
Zeep 4.0.0 - SOAP client

Further documentation
------------
- [DiscoveryGate Web Service docs](https://www.discoverygate.com/webservice_docs/1.2/)
- [Zeep docs](https://docs.python-zeep.org/en/master/index.html)
