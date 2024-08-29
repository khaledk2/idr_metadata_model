# Auto generated from image_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-28T23:43:28
# Schema: image_idr_schema
#
# id: idr.image.schema
# description: A LinkML schema translated from the idr key-value pairs for image
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
#from .types import Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = LINKML


# Types

# Class references



@dataclass
class Image(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Image"]
    class_class_curie: ClassVar[str] = "linkml:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = LINKML.Image

    id: int = None
    name: str = None
    organism: Optional[Union[dict, "Organism"]] = None
    gene: Optional[Union[dict, "Gene"]] = None
    phenotype: Optional[Union[dict, "Phenotype"]] = None
    compound: Optional[Union[dict, "Compound"]] = None
    pathology: Optional[Union[Union[dict, "Pathology"], List[Union[dict, "Pathology"]]]] = empty_list()
    antibody: Optional[Union[Union[dict, "Antibody"], List[Union[dict, "Antibody"]]]] = empty_list()
    siRNA: Optional[Union[Union[dict, "SiRNA"], List[Union[dict, "SiRNA"]]]] = empty_list()
    cell_line: Optional[Union[dict, "CellLine"]] = None
    Protein: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, int):
            self.id = int(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.organism is not None and not isinstance(self.organism, Organism):
            self.organism = Organism(**as_dict(self.organism))

        if self.gene is not None and not isinstance(self.gene, Gene):
            self.gene = Gene(**as_dict(self.gene))

        if self.phenotype is not None and not isinstance(self.phenotype, Phenotype):
            self.phenotype = Phenotype(**as_dict(self.phenotype))

        if self.compound is not None and not isinstance(self.compound, Compound):
            self.compound = Compound(**as_dict(self.compound))

        self._normalize_inlined_as_dict(slot_name="pathology", slot_type=Pathology, key_name="pathology", keyed=False)

        self._normalize_inlined_as_dict(slot_name="antibody", slot_type=Antibody, key_name="antibody", keyed=False)

        self._normalize_inlined_as_dict(slot_name="siRNA", slot_type=SiRNA, key_name="siRNA_identifier", keyed=False)

        if self.cell_line is not None and not isinstance(self.cell_line, CellLine):
            self.cell_line = CellLine(**as_dict(self.cell_line))

        if self.Protein is not None and not isinstance(self.Protein, str):
            self.Protein = str(self.Protein)

        super().__post_init__(**kwargs)


@dataclass
class OrganismPart(YAMLRoot):
    """
    An organism part entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["OrganismPart"]
    class_class_curie: ClassVar[str] = "linkml:OrganismPart"
    class_name: ClassVar[str] = "Organism_part"
    class_model_uri: ClassVar[URIRef] = LINKML.OrganismPart

    organism_part: str = None
    organism_part_identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.organism_part):
            self.MissingRequiredField("organism_part")
        if not isinstance(self.organism_part, str):
            self.organism_part = str(self.organism_part)

        if self.organism_part_identifier is not None and not isinstance(self.organism_part_identifier, str):
            self.organism_part_identifier = str(self.organism_part_identifier)

        super().__post_init__(**kwargs)


@dataclass
class Organism(YAMLRoot):
    """
    An organism part entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Organism"]
    class_class_curie: ClassVar[str] = "linkml:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = LINKML.Organism

    organism: str = None
    organism_part: Optional[Union[Union[dict, OrganismPart], List[Union[dict, OrganismPart]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.organism):
            self.MissingRequiredField("organism")
        if not isinstance(self.organism, str):
            self.organism = str(self.organism)

        #self._normalize_inlined_as_dict(slot_name="organism_part", slot_type=OrganismPart, key_name="organism part", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Gene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Gene"]
    class_class_curie: ClassVar[str] = "linkml:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = LINKML.Gene

    gene_symbol: str = None
    gene_identifier: str = None
    gene_identifier_url: Union[str, URI] = None
    organism: Optional[Union[dict, Organism]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self._is_empty(self.gene_identifier):
            self.MissingRequiredField("gene_identifier")
        if not isinstance(self.gene_identifier, str):
            self.gene_identifier = str(self.gene_identifier)

        if self._is_empty(self.gene_identifier_url):
            self.MissingRequiredField("gene_identifier_url")
        if not isinstance(self.gene_identifier_url, URI):
            self.gene_identifier_url = URI(self.gene_identifier_url)

        if self.organism is not None and not isinstance(self.organism, Organism):
            self.organism = Organism(**as_dict(self.organism))

        super().__post_init__(**kwargs)


@dataclass
class Phenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Phenotype"]
    class_class_curie: ClassVar[str] = "linkml:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = LINKML.Phenotype

    phenotype: str = None
    phenotype_term_name: str = None
    phenotype_term_accession: Optional[str] = None
    phenotype_term_accession_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        if self._is_empty(self.phenotype_term_name):
            self.MissingRequiredField("phenotype_term_name")
        if not isinstance(self.phenotype_term_name, str):
            self.phenotype_term_name = str(self.phenotype_term_name)

        if self.phenotype_term_accession is not None and not isinstance(self.phenotype_term_accession, str):
            self.phenotype_term_accession = str(self.phenotype_term_accession)

        if self.phenotype_term_accession_url is not None and not isinstance(self.phenotype_term_accession_url, URI):
            self.phenotype_term_accession_url = URI(self.phenotype_term_accession_url)

        super().__post_init__(**kwargs)


@dataclass
class Compound(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Compound"]
    class_class_curie: ClassVar[str] = "linkml:Compound"
    class_name: ClassVar[str] = "Compound"
    class_model_uri: ClassVar[URIRef] = LINKML.Compound

    compound_name: str = None
    compound_name_url: Union[str, URI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.compound_name):
            self.MissingRequiredField("compound_name")
        if not isinstance(self.compound_name, str):
            self.compound_name = str(self.compound_name)

        if self._is_empty(self.compound_name_url):
            self.MissingRequiredField("compound_name_url")
        if not isinstance(self.compound_name_url, URI):
            self.compound_name_url = URI(self.compound_name_url)

        super().__post_init__(**kwargs)


@dataclass
class Pathology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Pathology"]
    class_class_curie: ClassVar[str] = "linkml:Pathology"
    class_name: ClassVar[str] = "Pathology"
    class_model_uri: ClassVar[URIRef] = LINKML.Pathology

    pathology: str = None
    pathology_identifier: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.pathology):
            self.MissingRequiredField("pathology")
        if not isinstance(self.pathology, str):
            self.pathology = str(self.pathology)

        if self._is_empty(self.pathology_identifier):
            self.MissingRequiredField("pathology_identifier")
        if not isinstance(self.pathology_identifier, str):
            self.pathology_identifier = str(self.pathology_identifier)

        super().__post_init__(**kwargs)


@dataclass
class Antibody(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Antibody"]
    class_class_curie: ClassVar[str] = "linkml:Antibody"
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = LINKML.Antibody

    antibody: str = None
    antibody_identifier: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.antibody):
            self.MissingRequiredField("antibody")
        if not isinstance(self.antibody, str):
            self.antibody = str(self.antibody)

        if self._is_empty(self.antibody_identifier):
            self.MissingRequiredField("antibody_identifier")
        if not isinstance(self.antibody_identifier, str):
            self.antibody_identifier = str(self.antibody_identifier)

        super().__post_init__(**kwargs)


@dataclass
class SiRNA(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["SiRNA"]
    class_class_curie: ClassVar[str] = "linkml:SiRNA"
    class_name: ClassVar[str] = "siRNA"
    class_model_uri: ClassVar[URIRef] = LINKML.SiRNA

    siRNA_identifier: str = None
    siRNA_pool_identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.siRNA_identifier):
            self.MissingRequiredField("siRNA_identifier")
        if not isinstance(self.siRNA_identifier, str):
            self.siRNA_identifier = str(self.siRNA_identifier)

        if self.siRNA_pool_identifier is not None and not isinstance(self.siRNA_pool_identifier, str):
            self.siRNA_pool_identifier = str(self.siRNA_pool_identifier)

        super().__post_init__(**kwargs)


@dataclass
class CellLine(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["CellLine"]
    class_class_curie: ClassVar[str] = "linkml:CellLine"
    class_name: ClassVar[str] = "Cell_line"
    class_model_uri: ClassVar[URIRef] = LINKML.CellLine

    cell_lines: str = None
    cell_lines_supplementary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_lines):
            self.MissingRequiredField("cell_lines")
        if not isinstance(self.cell_lines, str):
            self.cell_lines = str(self.cell_lines)

        if self.cell_lines_supplementary is not None and not isinstance(self.cell_lines_supplementary, str):
            self.cell_lines_supplementary = str(self.cell_lines_supplementary)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.image__id = Slot(uri=LINKML.id, name="image__id", curie=LINKML.curie('id'),
                   model_uri=LINKML.image__id, domain=None, range=int)

slots.image__name = Slot(uri=LINKML.name, name="image__name", curie=LINKML.curie('name'),
                   model_uri=LINKML.image__name, domain=None, range=str)

slots.image__organism = Slot(uri=LINKML.organism, name="image__organism", curie=LINKML.curie('organism'),
                   model_uri=LINKML.image__organism, domain=None, range=Optional[Union[dict, Organism]])

slots.image__gene = Slot(uri=LINKML.gene, name="image__gene", curie=LINKML.curie('gene'),
                   model_uri=LINKML.image__gene, domain=None, range=Optional[Union[dict, Gene]])

slots.image__phenotype = Slot(uri=LINKML.phenotype, name="image__phenotype", curie=LINKML.curie('phenotype'),
                   model_uri=LINKML.image__phenotype, domain=None, range=Optional[Union[dict, Phenotype]])

slots.image__compound = Slot(uri=LINKML.compound, name="image__compound", curie=LINKML.curie('compound'),
                   model_uri=LINKML.image__compound, domain=None, range=Optional[Union[dict, Compound]])

slots.image__pathology = Slot(uri=LINKML.pathology, name="image__pathology", curie=LINKML.curie('pathology'),
                   model_uri=LINKML.image__pathology, domain=None, range=Optional[Union[Union[dict, Pathology], List[Union[dict, Pathology]]]])

slots.image__antibody = Slot(uri=LINKML.antibody, name="image__antibody", curie=LINKML.curie('antibody'),
                   model_uri=LINKML.image__antibody, domain=None, range=Optional[Union[Union[dict, Antibody], List[Union[dict, Antibody]]]])

slots.image__siRNA = Slot(uri=LINKML.siRNA, name="image__siRNA", curie=LINKML.curie('siRNA'),
                   model_uri=LINKML.image__siRNA, domain=None, range=Optional[Union[Union[dict, SiRNA], List[Union[dict, SiRNA]]]])

slots.image__cell_line = Slot(uri=LINKML.cell_line, name="image__cell_line", curie=LINKML.curie('cell_line'),
                   model_uri=LINKML.image__cell_line, domain=None, range=Optional[Union[dict, CellLine]])

slots.image__Protein = Slot(uri=LINKML.Protein, name="image__Protein", curie=LINKML.curie('Protein'),
                   model_uri=LINKML.image__Protein, domain=None, range=Optional[str])

slots.organismPart__organism_part = Slot(uri=LINKML.organism_part, name="organismPart__organism_part", curie=LINKML.curie('organism_part'),
                   model_uri=LINKML.organismPart__organism_part, domain=None, range=str)

slots.organismPart__organism_part_identifier = Slot(uri=LINKML.organism_part_identifier, name="organismPart__organism_part_identifier", curie=LINKML.curie('organism_part_identifier'),
                   model_uri=LINKML.organismPart__organism_part_identifier, domain=None, range=Optional[str])

slots.organism__organism = Slot(uri=LINKML.organism, name="organism__organism", curie=LINKML.curie('organism'),
                   model_uri=LINKML.organism__organism, domain=None, range=str)

slots.organism__organism_part = Slot(uri=LINKML.organism_part, name="organism__organism_part", curie=LINKML.curie('organism_part'),
                   model_uri=LINKML.organism__organism_part, domain=None, range=Optional[Union[Union[dict, OrganismPart], List[Union[dict, OrganismPart]]]])

slots.gene__gene_symbol = Slot(uri=LINKML.gene_symbol, name="gene__gene_symbol", curie=LINKML.curie('gene_symbol'),
                   model_uri=LINKML.gene__gene_symbol, domain=None, range=str)

slots.gene__gene_identifier = Slot(uri=LINKML.gene_identifier, name="gene__gene_identifier", curie=LINKML.curie('gene_identifier'),
                   model_uri=LINKML.gene__gene_identifier, domain=None, range=str)

slots.gene__gene_identifier_url = Slot(uri=LINKML.gene_identifier_url, name="gene__gene_identifier_url", curie=LINKML.curie('gene_identifier_url'),
                   model_uri=LINKML.gene__gene_identifier_url, domain=None, range=Union[str, URI])

slots.gene__organism = Slot(uri=LINKML.organism, name="gene__organism", curie=LINKML.curie('organism'),
                   model_uri=LINKML.gene__organism, domain=None, range=Optional[Union[dict, Organism]])

slots.phenotype__phenotype = Slot(uri=LINKML.phenotype, name="phenotype__phenotype", curie=LINKML.curie('phenotype'),
                   model_uri=LINKML.phenotype__phenotype, domain=None, range=str)

slots.phenotype__phenotype_term_name = Slot(uri=LINKML.phenotype_term_name, name="phenotype__phenotype_term_name", curie=LINKML.curie('phenotype_term_name'),
                   model_uri=LINKML.phenotype__phenotype_term_name, domain=None, range=str)

slots.phenotype__phenotype_term_accession = Slot(uri=LINKML.phenotype_term_accession, name="phenotype__phenotype_term_accession", curie=LINKML.curie('phenotype_term_accession'),
                   model_uri=LINKML.phenotype__phenotype_term_accession, domain=None, range=Optional[str])

slots.phenotype__phenotype_term_accession_url = Slot(uri=LINKML.phenotype_term_accession_url, name="phenotype__phenotype_term_accession_url", curie=LINKML.curie('phenotype_term_accession_url'),
                   model_uri=LINKML.phenotype__phenotype_term_accession_url, domain=None, range=Optional[Union[str, URI]])

slots.compound__compound_name = Slot(uri=LINKML.compound_name, name="compound__compound_name", curie=LINKML.curie('compound_name'),
                   model_uri=LINKML.compound__compound_name, domain=None, range=str)

slots.compound__compound_name_url = Slot(uri=LINKML.compound_name_url, name="compound__compound_name_url", curie=LINKML.curie('compound_name_url'),
                   model_uri=LINKML.compound__compound_name_url, domain=None, range=Union[str, URI])

slots.pathology__pathology = Slot(uri=LINKML.pathology, name="pathology__pathology", curie=LINKML.curie('pathology'),
                   model_uri=LINKML.pathology__pathology, domain=None, range=str)

slots.pathology__pathology_identifier = Slot(uri=LINKML.pathology_identifier, name="pathology__pathology_identifier", curie=LINKML.curie('pathology_identifier'),
                   model_uri=LINKML.pathology__pathology_identifier, domain=None, range=str)

slots.antibody__antibody = Slot(uri=LINKML.antibody, name="antibody__antibody", curie=LINKML.curie('antibody'),
                   model_uri=LINKML.antibody__antibody, domain=None, range=str)

slots.antibody__antibody_identifier = Slot(uri=LINKML.antibody_identifier, name="antibody__antibody_identifier", curie=LINKML.curie('antibody_identifier'),
                   model_uri=LINKML.antibody__antibody_identifier, domain=None, range=str)

slots.siRNA__siRNA_identifier = Slot(uri=LINKML.siRNA_identifier, name="siRNA__siRNA_identifier", curie=LINKML.curie('siRNA_identifier'),
                   model_uri=LINKML.siRNA__siRNA_identifier, domain=None, range=str)

slots.siRNA__siRNA_pool_identifier = Slot(uri=LINKML.siRNA_pool_identifier, name="siRNA__siRNA_pool_identifier", curie=LINKML.curie('siRNA_pool_identifier'),
                   model_uri=LINKML.siRNA__siRNA_pool_identifier, domain=None, range=Optional[str])

slots.cellLine__cell_lines = Slot(uri=LINKML.cell_lines, name="cellLine__cell_lines", curie=LINKML.curie('cell_lines'),
                   model_uri=LINKML.cellLine__cell_lines, domain=None, range=str)

slots.cellLine__cell_lines_supplementary = Slot(uri=LINKML.cell_lines_supplementary, name="cellLine__cell_lines_supplementary", curie=LINKML.curie('cell_lines_supplementary'),
                   model_uri=LINKML.cellLine__cell_lines_supplementary, domain=None, range=Optional[str])
