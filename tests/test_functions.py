from unittest import TestCase
from dgws_api.functions import *


class Test(TestCase):

    # load test strings
    with open('./names.txt') as file:
        names = [el.strip() for el in file.readlines()]

    with open('./smiles.txt') as file:
        smiles = [el.strip() for el in file.readlines()]

    with open('./chimes.txt') as file:
        chimes = [el.strip() for el in file.readlines()]

    with open('./molfile.mol') as file:
        molfile = [file.read()]

    def test_service_request_function(self):
        from dgws_api.functions import _service_request_dict
        # default return should be a basic ServiceRequest object as a dict with page=1
        self.assertEqual(_service_request_dict(), ServiceRequest(page=1).__dict__)
        # if 'page' arg is given, return a default ServiceRequest object as a dict with appropriate page
        self.assertEqual(_service_request_dict(page=2), ServiceRequest(page=2).__dict__)
        # if 'request' argument is given, return that ServiceRequest object as a dict
        self.assertEqual(_service_request_dict(ServiceRequest(page=2)), ServiceRequest(page=2).__dict__)
        # if both arguments are given, return that ServiceRequest object as a dict with page adjusted
        self.assertEqual(_service_request_dict(ServiceRequest(page=2), page=3), ServiceRequest(page=3).__dict__)

    def test_search_name(self):
        try:
            search_names(self.names)
            print('Name search successful')
        except Exception as e:
            self.fail(e)

    def test_search_exact(self):
        try:
            search_structure([self.chimes[0]], MoleculeSearchType.EXACT)
            print('Single CHIME search successful')
            search_structure(self.molfile, MoleculeSearchType.EXACT)
            print('Single molfile search successful')
            search_structure([self.smiles[0]], MoleculeSearchType.EXACT)  # does not seem to work with SMILES
            print('Single SMILES search successful')
        except Exception as e:
            self.fail(e)

    def test_search_multiple_structures(self):
        try:
            query = self.chimes
            res = search_structure(query, MoleculeSearchType.EXACT)
            self.assertEqual(res['containedCount'], len(query))
            print('Multiple CHIME string search successful')
        except Exception as e:
            self.fail(e)
