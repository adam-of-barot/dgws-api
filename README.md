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

The example below demonstrates how to make structure based queries to the web service. I've found that you can send structure information in MDL Molfile or CHIME string formats. SMILES unfortunately don't seem to work.

```python
from dgws_api.functions import search_structure

molblock = """

  ACCLDraw05262119162D

  6  6  0  0  0  0  0  0  0  0999 V2000
    7.3069   -5.4019    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0
    6.3515   -4.7078    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.7164   -3.5846    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.8973   -3.5846    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    8.2622   -4.7078    0.0000 N   0  0  3  0  0  0  0  0  0  0  0  0
    9.4031   -5.0135    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  2  0  0  0  0
  2  3  1  0  0  0  0
  3  4  2  0  0  0  0
  4  5  1  0  0  0  0
  5  1  1  0  0  0  0
  5  6  1  0  0  0  0
M  END
"""
search_structure([molblock])
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
