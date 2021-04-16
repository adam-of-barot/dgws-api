# dgws-api
A convenience Python wrapper for the DiscoveryGate Web Service (DGWS).

What is this for?
-----------
The aim of the project is to create easy-to-use wrapping functions with few parameters for some of the most used services of DGWS.
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
Main functionality is contained in functions.
Simply import the functions, supply the parameters, and the function will return the server's response after being parsed by Zeep.
The example below returns basic identification information about the molecule aspirin.

```python
from dgws_api.functions import search_names

names = ['Aspirin']
search_names(names)
```

The example below demonstrates how to make structure based queries to the web service.

```python
from dgws_api.functions import search_structure

smiles = ['c1ccccc1']
search_structure(smiles)
```

The module is opinionated, and will load basic default configurations for underlying objects if the functions are not supplied with them.
If more customisation is needed (for example different information is needed from the web service), then we need to supply the functions with a custom _ServiceRequest_ object.
The example below demonstrated how to obtain availability information by setting the _molecule_flags_ argument on a _ServiceRequest_ object.

```python
from dgws_api.functions import search_names
from dgws_api.classes import ServiceRequest
from dgws_api.enums import MoleculeRetrievalFlags

request = ServiceRequest(molecule_flags=MoleculeRetrievalFlags.PROCUREMENT_PRICING)
names = ['Aspirin']
search_names(names, request)
```

Other python modules used
------------
Zeep 4.0.0 - SOAP client

Further documentation
------------
- [DiscoveryGate Web Service docs](https://www.discoverygate.com/webservice_docs/1.2/)
- [Zeep docs](https://docs.python-zeep.org/en/master/index.html)
