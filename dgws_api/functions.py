from typing import List
from dgws_api.classes import *

DEFAULT_PAGE_SIZE = 200


def _service_request_dict(request: ServiceRequest = None,
                          page: int = None, page_size: int = None):
    if not request:
        request = ServiceRequest()
    if page_size:
        request.set_count(page_size)
    if page:
        request.set_page(page)
    return request.as_dict()


def search_names(names: List[str], request: ServiceRequest = None,
                 page: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
    request = _service_request_dict(request, page, page_size)
    return client.service.getMoleculesByNames(request, names)


def search_ids(ids: List[int], request: ServiceRequest = None,
               page: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
    request = _service_request_dict(request, page, page_size)
    return client.service.getMoleculesById(request, ids)


def search_structure(structures: List[str], search_type: MoleculeSearchType, request: ServiceRequest = None,
                     page: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
    request = _service_request_dict(request, page, page_size)
    searches = []
    length = len(structures)
    for idx, structure in enumerate(structures):
        if idx == length:
            search_op = SearchOperator.NONE
        else:
            search_op = SearchOperator.OR
        searches.append(
            MoleculeSearch(
                structure=structure,
                search_type=search_type,
                search_op=search_op
            ).as_dict()
        )
    return client.service.getMoleculesByStructure(request, searches)
