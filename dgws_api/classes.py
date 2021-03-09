from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
import json
from .enums import *

with open("./config.json") as config_file:
    config = json.load(config_file)

history = HistoryPlugin()
client = Client(config['WSDL'], plugins=[history])

"""
IMPORTANT
Data types (even if empty) must be defined and must match the types in the API reference.
Otherwise, the server will return no XML data, and zeep will throw a zeep.exceptions.TransportError
"""


class ServiceRequest:
    """
    Defines what kind of data to return from the service
    """
    def __init__(self,
                 page: int = 1,
                 molecule_flags: MoleculeRetrievalFlags = MoleculeRetrievalFlags.IDENTIFICATION,
                 reaction_flags: ReactionRetrievalFlags = ReactionRetrievalFlags.NO_STRUCTURE,
                 source_filter: DataSource = DataSource.CINDEX,
                 stateful_query_key: str = '',
                 exclusive_flag_hits: bool = True):
        self.licenseKey = config['LicenseKey']
        self.count = 10
        self.page = {
            'offset': (page - 1) * self.count,
            'count': self.count
        }
        self.moleculeFlags = molecule_flags
        self.reactionFlags = reaction_flags
        self.sourceFilter = source_filter
        self.statefulQueryKey = stateful_query_key
        self.exclusiveFlagHits = exclusive_flag_hits


class MoleculeSearch:
    """
    Defines a molecular structure based query
    """
    def __init__(self,
                 structure: str,  # can be MOL file string or CHIME string
                 search_type: MoleculeSearchType = MoleculeSearchType.EXACT,
                 negate: bool = False,
                 search_op: SearchOperator = SearchOperator.NONE,
                 parenthesis: Parenthesis = Parenthesis.NONE,
                 custom_flags: str = '',
                 similarity: int = 0,
                 parenthesis_count: int = 0):
        self.structure = structure
        self.negate = negate
        self.booleanOperator = search_op
        self.searchType = search_type
        self.customSimilarity = similarity
        self.parenthesis = parenthesis
        self.parenthesisCount = parenthesis_count
        self.customFlags = custom_flags

    def as_dict(self):
        """
        Replaces the 'negate' key with 'not' in the class' __dict__ method,
        because the API expects the latter keyword, and 'not' is a reserved keyword in Python
        """
        d = self.__dict__.copy()
        d['not'] = self.negate
        del d['negate']
        return d
