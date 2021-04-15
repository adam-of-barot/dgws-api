from unittest import TestCase
from dgws_api.functions import *


class Test(TestCase):
    names = ['Aspirin']
    # benzyl chloride
    smiles_string = "c1ccccc1"
    # aspirin
    chime_string = "CYAAFQwAYewQFPfJfx616ZLb6rNugDNdp8dA8cRIkKkpZ55HBpDGtTgMMRQ$XWYlh9ME^V9Z6IcS98biuRVPy8whVCDx5e6NILuAen5LsA$j1$6Gaty9$tJzeoTfv$o3GKH8tnf^NkJ^RCJYpzLUw2SgFDaACHDiRBxk4MgoaKDVGYlPxcfvpQ4aGC7Sph4SOgCzvxaR0g1olMiK2EqiyHkiKYgaN51qxOXSXrZeYQSdi$smMJDSxNy1lnA4iWYsbgF6oL3OMVZj2gSC05NNqWjqGXyIRyN0Y638ezmbK8luWXxoEMrto5FNnfB3x1kY4M1^nQUVlV4I7$iudF^Q^YNfeQLlPKuUUWqKSq2Z11Ob71ZRMnUfSwVvy92cm0aaqRdKSKuk0TryKb$NuSymq58OWEf1^1HY5w7Vwocufewm7e7MN8fTeTvjiA"
    # napthalene
    chime_string2 = "JYAu$j7AlAwQBfHAybSPhbKFN35N0aQLH2W6tjPQgXdVX6$^EVjYXsLoo^4EXRQSo5gcM5yG5V7UsxZaAavdCeJ7zBRMCit4FMxGGGw9b97vmybFNGK7v9YyArL8vwLvpP9neEA8dlQGwMA9A9QGV5wvHdRhHaGRIEW0r8i6pgswIoA2wqUrU87gjd0PJRRYC^cuvVImixhldW4tuovp1$vw05Ll4J7Wcolvz$eiHoAEQbZqdE7ZrjpnqLXjtiztYXe36PyfaLt^b3V18qM5y3iSl6VZWmsFshStivYW13olNZJwXazW1WGtWrBFLRt^lWWosbNFjD8E8Rz8OxWAyVK"
    molfile_string = """
ACCLDraw02112115172D

13 13  0  0  0  0  0  0  0  0999 V2000
13.7926   -8.0492    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
12.7706   -7.4573    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
11.7469   -8.0463    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
12.7706   -6.2762    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
11.7504   -5.6841    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
11.7504   -4.4968    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
10.7258   -3.8972    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
9.7012   -4.4968    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
9.7012   -5.6841    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
10.7258   -6.2717    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
12.7750   -3.9093    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
13.7960   -4.5029    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
12.7750   -2.7282    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
1  2  1  0  0  0  0
2  3  2  0  0  0  0
2  4  1  0  0  0  0
4  5  1  0  0  0  0
5  6  2  0  0  0  0
7  6  1  0  0  0  0
8  7  2  0  0  0  0
9  8  1  0  0  0  0
5 10  1  0  0  0  0
10  9  2  0  0  0  0
6 11  1  0  0  0  0
11 12  2  0  0  0  0
11 13  1  0  0  0  0
M  END
"""

    def test_service_request_function(self):
        from dgws_api.functions import _service_request_dict
        self.assertEqual(_service_request_dict(), ServiceRequest(page=1).__dict__)
        self.assertEqual(_service_request_dict(page=2), ServiceRequest(page=2).__dict__)
        self.assertEqual(_service_request_dict(ServiceRequest(page=2), page=3), ServiceRequest(page=3).__dict__)

    def test_search_name(self):
        try:
            search_names(self.names)
        except Exception as e:
            self.fail(e)

    def test_search_exact(self):
        try:
            search_structure([self.chime_string], MoleculeSearchType.EXACT)
            print('CHIME search successful')
            search_structure([self.smiles_string], MoleculeSearchType.EXACT)  # does not seem to work with SMILES
            print('SMILES search successful')
            search_structure([self.molfile_string], MoleculeSearchType.EXACT)  # molfile search broken too
            print('Molfile search successful')
        except Exception as e:
            self.fail(e)

    def test_search_multiple_structures(self):
        try:
            query = [self.chime_string, self.chime_string2]
            res = search_structure(query, MoleculeSearchType.EXACT)
            print(res)
            self.assertEqual(res['containerCount'], len(query))
        except Exception as e:
            self.fail(e)
