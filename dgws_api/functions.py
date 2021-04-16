from typing import List
from .classes import *


def _service_request_dict(request: ServiceRequest = None, page: int = None):
    if not request:
        request = ServiceRequest()
    if page:
        request.set_page(page)
    return request.as_dict()


def search_names(names: List[str], request: ServiceRequest = None, page: int = 1):
    request = _service_request_dict(request, page)
    return client.service.getMoleculesByNames(request, names)


def search_structure(structures: List[str], search_type: MoleculeSearchType, request: ServiceRequest = None, page: int = 1):
    request = _service_request_dict(request, page)
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
