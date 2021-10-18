from unittest import TestCase
from src.dgws_api.functions import *
from src.dgws_api.functions import _service_request_dict


class Test(TestCase):

    # load test strings
    with open('./names.txt') as file:
        names = [el.strip() for el in file.readlines()]

    with open('./ids.txt') as file:
        ids = [el.strip() for el in file.readlines()]

    with open('./smiles.txt') as file:
        smiles = [el.strip() for el in file.readlines()]

    with open('./chimes.txt') as file:
        chimes = [el.strip() for el in file.readlines()]

    with open('./molfile.mol') as file:
        molfile = [file.read()]

    def test_service_request_function(self):
        # default return should be a basic ServiceRequest object as a dict with page=1 and count 200
        self.assertEqual(_service_request_dict(), ServiceRequest(page=1, count=200).__dict__)
        # if 'request' argument is given, return that ServiceRequest object as a dict
        self.assertEqual(_service_request_dict(ServiceRequest(page=2, count=100)), ServiceRequest(page=2, count=100).__dict__)

        # ---- Test PAGE argument ----

        # if 'page' arg is given, return a default ServiceRequest object as a dict with appropriate page
        self.assertEqual(_service_request_dict(page=2), ServiceRequest(page=2).__dict__)
        # if both arguments are given, return that ServiceRequest object as a dict with page adjusted
        self.assertEqual(_service_request_dict(ServiceRequest(page=2), page=3), ServiceRequest(page=3).__dict__)

        # ---- Test PAGE_SIZE argument ----

        # if 'page_size' arg is given, return a default ServiceRequest object as a dict with appropriate count
        self.assertEqual(_service_request_dict(page_size=100), ServiceRequest(count=100).__dict__)
        # if both arguments are given, return that ServiceRequest object as a dict with count adjusted
        self.assertEqual(_service_request_dict(ServiceRequest(count=100), page_size=300), ServiceRequest(count=300).__dict__)

        # ---- Test PAGE and PAGE_SIZE arguments together ----

        # if both page and page_size argument is given, return a ServiceRequest object as a dict with both set
        self.assertEqual(_service_request_dict(page=2, page_size=100), ServiceRequest(page=2, count=100).__dict__)
        # if 'request', 'page' and 'page_size' arguments are given,
        # return that ServiceRequest object as a dict with page and count adjusted
        self.assertEqual(_service_request_dict(ServiceRequest(page=2, count=100), page=3, page_size=1000), ServiceRequest(page=3, count=1000).__dict__)

    def test_search_name(self):
        try:
            search_names(self.names)
            print('Name search successful')
        except Exception as e:
            self.fail(e)

    def test_search_ids(self):
        try:
            search_ids(self.ids)
            print('ID search successful')
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
