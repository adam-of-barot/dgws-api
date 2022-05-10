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
Installing via pip through the GitHub repo:
```commandline
python -m pip install git+https://github.com/adam-of-barot/dgws-api.git
```
Installing directly with pip & setup.py:
```commandline
pip install .
```

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
from dgws_api.enums import MoleculeSearchType

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
search_structure([molblock], MoleculeSearchType.EXACT)
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

In the case of large queries, the DGWS docs suggest using stateful queries to increase the efficiency of data retrieval.
In order to perform a stateful query, one needs to provide the service with a ServiceRequest that has the statefulQueryKey property set.
For convenience, the ServiceRequest class comes with a built-in stateful query key generator method, but the user can provide their own key as well.

When a query would return more records than the allowed page size, then response.queryCount will be -1.
To get the next page of the query, one would send the same request, but increase the page by 1.
Once the last page is reached, queryCount will become the total number of records returned.

```python
from dgws_api.functions import search_structure, close_stateful_query
from dgws_api.classes import ServiceRequest
from dgws_api.enums import MoleculeRetrievalFlags, MoleculeSearchType

molblock = """
  ACCLDraw10182116242D

  6  5  0  0  0  0  0  0  0  0999 V2000
   11.3438   -8.5313    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   12.3666   -7.9407    0.0000 B   0  0  0  0  0  0  0  0  0  0  0  0
   12.3666   -6.7592    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
   13.3898   -8.5314    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
   14.4130   -7.9407    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0
   11.3434   -6.1685    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  2  3  1  0  0  0  0
  2  4  1  0  0  0  0
  4  5  1  0  0  0  0
  3  6  1  0  0  0  0
M  END
"""

request = ServiceRequest(molecule_flags=MoleculeRetrievalFlags.ID_ONLY)
request.create_new_stateful_key()
page = 1
done = False
records = []

while not done:
    response = search_structure([molblock], MoleculeSearchType.SUBSTRUCTURE, request)
    if response.queryCount == -1 or response.containedCount == 0:
        done = True
        close_stateful_query(request)  # docs advise to close the query upon getting all the data
    else:
        page += 1
    records += response.records
```

Other python modules used
------------
Zeep 4.0.0 - SOAP client

Further documentation
------------
- [DiscoveryGate Web Service docs](https://www.discoverygate.com/webservice_docs/1.2/)
- [Zeep docs](https://docs.python-zeep.org/en/master/index.html)
