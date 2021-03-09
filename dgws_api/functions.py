from typing import List

from .classes import *


def search_names(names: List[str], request: ServiceRequest = None, page: int = 1):
    if not request:
        request = ServiceRequest(page=page).__dict__
    return client.service.getMoleculesByNames(request, names)


def search_structure(structures: List[str], search_type: MoleculeSearchType, request: ServiceRequest = None, page: int = 1):
    if not request:
        request = ServiceRequest(page=page).__dict__
    searches = []
    for structure in structures:
        searches.append(MoleculeSearch(structure=structure, search_type=search_type).as_dict())
    return client.service.getMoleculesByStructure(request, searches)
