from enum import Enum

# Static string types taken from the DGWS API reference:
# https://www.discoverygate.com/webservice_docs/1.2/docs/api-reference/com/discoverygate/webservice/DGWS.html
# Created enums here avoid having to lookup the API reference each time I want to see a type's possible values
# and to avoid type errors


class BaseEnum(Enum):

    def __str__(self):
        return str(self.name)


class MoleculeRetrievalFlags(BaseEnum):
    CARCINOGENIC = 1
    CLASSIFICATION = 2
    DRUG = 3
    ID_ONLY = 4
    IDENTIFICATION = 5
    LITERATURE = 6
    NO_STRUCTURE = 7
    PROCUREMENT_PRICING = 8
    PROCUREMENT_PRODUCT = 9
    PROCUREMENT_SUPPLIER = 10
    PROPERTIES = 11
    REACTION_PRODUCT = 12
    REACTION_REACTANT = 13
    SOURCE_3D = 14
    SOURCE_PROPERTIES = 15
    SOURCE_SUMMARY = 16
    TOXIC_CHEMICAL = 17
    TOXIC_EFFECT = 18


class ReactionRetrievalFlags(BaseEnum):
    CITATION = 1
    DISCRETE_CLASS_CODES = 2
    ID_ONLY = 3
    MOLECULE = 4
    NO_STRUCTURE = 5
    PATHS_AND_STEPS = 6
    SCHEME = 7
    STEP_CONDITIONS = 8


class DataSource(BaseEnum):
    ACD = 1
    CCR = 2
    CHEMSEEK = 3
    CINDEX = 4
    CIRX = 5
    CMC = 6
    DJSM = 7
    DWPI = 8
    IC = 9
    MDDR = 10
    MetaCore = 11
    MetaDrug = 12
    NCI = 13
    OHSPURE = 14
    ORGSYN = 15
    PharmaPendium = 16
    PUBCHEM = 17
    REFLIB = 18
    SCD = 19
    SPORE = 20
    SPRESI = 21
    TOX = 22
    XFPAT = 23
    XFRAE = 24


class SearchOperator(BaseEnum):
    AND = 1
    NONE = 2
    OR = 3


class Parenthesis(BaseEnum):
    CLOSED = 1
    NONE = 2
    OPEN = 3
    OPEN_INSIDE_NOT = 4


class MoleculeSearchType(BaseEnum):
    EXACT = 1
    EXACT_CUSTOM = 2
    EXACT_ISOMERS = 3
    EXACT_SALTS = 4
    EXACT_TAUTOMERS = 5
    SIMILARITY_60 = 6
    SIMILARITY_70 = 7
    SIMILARITY_80 = 8
    SIMILARITY_90 = 9
    SIMILARITY_95 = 10
    SIMILARITY_CUSTOM = 11
    SUBSTRUCTURE = 12
    SUBSTRUCTURE_HIGHLIGHT = 13
