from typing import List, Dict, Union
from .classes import *

DEFAULT_PAGE_SIZE = 200


def _service_request_dict(request: ServiceRequest = None,
                          page: int = None, page_size: int = None) -> Dict:
    """
    Returns a ServiceRequest object as a dictionary.
    Use the output of this to feed the client services, as they only accept dictionaries.
    :param request: a ServiceRequest object
    :param page: an integer, defining the page the ServiceRequest object should be set to
    :param page_size: an integer, defining the page size the ServiceRequest object should be set to
    :return: dictionary representation of the ServiceRequest object
    """
    if not request:
        request = ServiceRequest()
    if page_size:
        request.set_count(page_size)
    if page:
        request.set_page(page)
    return request.as_dict()


def search_names(names: List[str], request: ServiceRequest = None,
                 page: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
    """
    Searches for compounds by their identifiers (chemical name, CAS number or MDL number)
    """
    request = _service_request_dict(request, page, page_size)
    return client.service.getMoleculesByNames(request, names)


def search_ids(ids: List[Union[int, str]], request: ServiceRequest = None,
               page: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
    """
    Searches for a compounds by their record ID
    """
    request = _service_request_dict(request, page, page_size)
    objects = [{'id': i} for i in ids]  # service expects a list of dictionaries
    return client.service.getMoleculesById(request, objects)


def search_structure(structures: List[str], search_type: MoleculeSearchType, request: ServiceRequest = None,
                     page: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
    """
    Searches for compounds by structure.
    Structures should be in one of the following formats: MDL Molfile, CHIME string
    """
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


def close_stateful_query(request: ServiceRequest):
    """
    Closes the stateful query that is attached to the given ServiceRequest
    """
    if not request.statefulQueryKey:
        raise KeyError('There is no stateful query key set on this request object.')
    request = _service_request_dict(request)
    return client.service.closeStatefulQuery(request)
