# Auto generated from image_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-09T00:11:59
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
class ImageId(extended_int):
    pass


class OrganismOrganism(extended_str):
    pass


class GeneGeneSymbol(extended_str):
    pass


class PhenotypePhenotype(extended_str):
    pass


class CompoundCompoundName(extended_str):
    pass


class PathologyPathology(extended_str):
    pass


class AntibodyAntibody(extended_str):
    pass


class SiRNASiRNAIdentifier(extended_str):
    pass


class CellLineCellLines(extended_str):
    pass


class ProteinProtein(extended_str):
    pass


class OrganismPartOrganismPart(extended_str):
    pass


@dataclass
class Image(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Image"]
    class_class_curie: ClassVar[str] = "linkml:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = LINKML.Image

    id: Union[int, ImageId] = None
    name: str = None
    organism: Optional[Union[str, OrganismOrganism]] = None
    gene: Optional[Union[str, GeneGeneSymbol]] = None
    phenotype: Optional[Union[str, PhenotypePhenotype]] = None
    compound: Optional[Union[str, CompoundCompoundName]] = None
    pathology: Optional[Union[Union[str, PathologyPathology], List[Union[str, PathologyPathology]]]] = empty_list()
    antibody: Optional[Union[Union[str, AntibodyAntibody], List[Union[str, AntibodyAntibody]]]] = empty_list()
    siRNA: Optional[Union[Union[str, SiRNASiRNAIdentifier], List[Union[str, SiRNASiRNAIdentifier]]]] = empty_list()
    cell_line: Optional[Union[str, CellLineCellLines]] = None
    protein: Optional[Union[str, ProteinProtein]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageId):
            self.id = ImageId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.organism is not None and not isinstance(self.organism, OrganismOrganism):
            self.organism = OrganismOrganism(self.organism)

        if self.gene is not None and not isinstance(self.gene, GeneGeneSymbol):
            self.gene = GeneGeneSymbol(self.gene)

        if self.phenotype is not None and not isinstance(self.phenotype, PhenotypePhenotype):
            self.phenotype = PhenotypePhenotype(self.phenotype)

        if self.compound is not None and not isinstance(self.compound, CompoundCompoundName):
            self.compound = CompoundCompoundName(self.compound)

        if not isinstance(self.pathology, list):
            self.pathology = [self.pathology] if self.pathology is not None else []
        self.pathology = [v if isinstance(v, PathologyPathology) else PathologyPathology(v) for v in self.pathology]

        if not isinstance(self.antibody, list):
            self.antibody = [self.antibody] if self.antibody is not None else []
        self.antibody = [v if isinstance(v, AntibodyAntibody) else AntibodyAntibody(v) for v in self.antibody]

        if not isinstance(self.siRNA, list):
            self.siRNA = [self.siRNA] if self.siRNA is not None else []
        self.siRNA = [v if isinstance(v, SiRNASiRNAIdentifier) else SiRNASiRNAIdentifier(v) for v in self.siRNA]

        if self.cell_line is not None and not isinstance(self.cell_line, CellLineCellLines):
            self.cell_line = CellLineCellLines(self.cell_line)

        if self.protein is not None and not isinstance(self.protein, ProteinProtein):
            self.protein = ProteinProtein(self.protein)

        super().__post_init__(**kwargs)


@dataclass
class Organism(YAMLRoot):
    """
    An organism entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Organism"]
    class_class_curie: ClassVar[str] = "linkml:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = LINKML.Organism

    Organism: Union[str, OrganismOrganism] = None
    organism_part: Optional[Union[Union[str, OrganismPartOrganismPart], List[Union[str, OrganismPartOrganismPart]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Organism):
            self.MissingRequiredField("Organism")
        if not isinstance(self.Organism, OrganismOrganism):
            self.Organism = OrganismOrganism(self.Organism)

        if not isinstance(self.organism_part, list):
            self.organism_part = [self.organism_part] if self.organism_part is not None else []
        self.organism_part = [v if isinstance(v, OrganismPartOrganismPart) else OrganismPartOrganismPart(v) for v in self.organism_part]

        super().__post_init__(**kwargs)


@dataclass
class Gene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Gene"]
    class_class_curie: ClassVar[str] = "linkml:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = LINKML.Gene

    gene_symbol: Union[str, GeneGeneSymbol] = None
    gene_identifier: str = None
    gene_identifier_url: Union[str, URI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, GeneGeneSymbol):
            self.gene_symbol = GeneGeneSymbol(self.gene_symbol)

        if self._is_empty(self.gene_identifier):
            self.MissingRequiredField("gene_identifier")
        if not isinstance(self.gene_identifier, str):
            self.gene_identifier = str(self.gene_identifier)

        if self._is_empty(self.gene_identifier_url):
            self.MissingRequiredField("gene_identifier_url")
        if not isinstance(self.gene_identifier_url, URI):
            self.gene_identifier_url = URI(self.gene_identifier_url)

        super().__post_init__(**kwargs)


@dataclass
class Phenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Phenotype"]
    class_class_curie: ClassVar[str] = "linkml:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = LINKML.Phenotype

    Phenotype: Union[str, PhenotypePhenotype] = None
    Phenotype_Term_Name: str = None
    Phenotype_Term_Accession: Optional[str] = None
    Phenotype_Term_Accession_URL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Phenotype):
            self.MissingRequiredField("Phenotype")
        if not isinstance(self.Phenotype, PhenotypePhenotype):
            self.Phenotype = PhenotypePhenotype(self.Phenotype)

        if self._is_empty(self.Phenotype_Term_Name):
            self.MissingRequiredField("Phenotype_Term_Name")
        if not isinstance(self.Phenotype_Term_Name, str):
            self.Phenotype_Term_Name = str(self.Phenotype_Term_Name)

        if self.Phenotype_Term_Accession is not None and not isinstance(self.Phenotype_Term_Accession, str):
            self.Phenotype_Term_Accession = str(self.Phenotype_Term_Accession)

        if self.Phenotype_Term_Accession_URL is not None and not isinstance(self.Phenotype_Term_Accession_URL, URI):
            self.Phenotype_Term_Accession_URL = URI(self.Phenotype_Term_Accession_URL)

        super().__post_init__(**kwargs)


@dataclass
class Compound(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Compound"]
    class_class_curie: ClassVar[str] = "linkml:Compound"
    class_name: ClassVar[str] = "Compound"
    class_model_uri: ClassVar[URIRef] = LINKML.Compound

    compound_name: Union[str, CompoundCompoundName] = None
    Compound_Name_URL: Union[str, URI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.compound_name):
            self.MissingRequiredField("compound_name")
        if not isinstance(self.compound_name, CompoundCompoundName):
            self.compound_name = CompoundCompoundName(self.compound_name)

        if self._is_empty(self.Compound_Name_URL):
            self.MissingRequiredField("Compound_Name_URL")
        if not isinstance(self.Compound_Name_URL, URI):
            self.Compound_Name_URL = URI(self.Compound_Name_URL)

        super().__post_init__(**kwargs)


@dataclass
class Pathology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Pathology"]
    class_class_curie: ClassVar[str] = "linkml:Pathology"
    class_name: ClassVar[str] = "Pathology"
    class_model_uri: ClassVar[URIRef] = LINKML.Pathology

    Pathology: Union[str, PathologyPathology] = None
    Pathology_Identifier: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Pathology):
            self.MissingRequiredField("Pathology")
        if not isinstance(self.Pathology, PathologyPathology):
            self.Pathology = PathologyPathology(self.Pathology)

        if self._is_empty(self.Pathology_Identifier):
            self.MissingRequiredField("Pathology_Identifier")
        if not isinstance(self.Pathology_Identifier, str):
            self.Pathology_Identifier = str(self.Pathology_Identifier)

        super().__post_init__(**kwargs)


@dataclass
class Antibody(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Antibody"]
    class_class_curie: ClassVar[str] = "linkml:Antibody"
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = LINKML.Antibody

    Antibody: Union[str, AntibodyAntibody] = None
    Antibody_Identifier: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Antibody):
            self.MissingRequiredField("Antibody")
        if not isinstance(self.Antibody, AntibodyAntibody):
            self.Antibody = AntibodyAntibody(self.Antibody)

        if self._is_empty(self.Antibody_Identifier):
            self.MissingRequiredField("Antibody_Identifier")
        if not isinstance(self.Antibody_Identifier, str):
            self.Antibody_Identifier = str(self.Antibody_Identifier)

        super().__post_init__(**kwargs)


@dataclass
class SiRNA(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["SiRNA"]
    class_class_curie: ClassVar[str] = "linkml:SiRNA"
    class_name: ClassVar[str] = "siRNA"
    class_model_uri: ClassVar[URIRef] = LINKML.SiRNA

    siRNA_Identifier: Union[str, SiRNASiRNAIdentifier] = None
    siRNA_Pool_Identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.siRNA_Identifier):
            self.MissingRequiredField("siRNA_Identifier")
        if not isinstance(self.siRNA_Identifier, SiRNASiRNAIdentifier):
            self.siRNA_Identifier = SiRNASiRNAIdentifier(self.siRNA_Identifier)

        if self.siRNA_Pool_Identifier is not None and not isinstance(self.siRNA_Pool_Identifier, str):
            self.siRNA_Pool_Identifier = str(self.siRNA_Pool_Identifier)

        super().__post_init__(**kwargs)


@dataclass
class CellLine(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["CellLine"]
    class_class_curie: ClassVar[str] = "linkml:CellLine"
    class_name: ClassVar[str] = "Cell line"
    class_model_uri: ClassVar[URIRef] = LINKML.CellLine

    Cell_lines: Union[str, CellLineCellLines] = None
    Cell_Lines_Supplementary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Cell_lines):
            self.MissingRequiredField("Cell_lines")
        if not isinstance(self.Cell_lines, CellLineCellLines):
            self.Cell_lines = CellLineCellLines(self.Cell_lines)

        if self.Cell_Lines_Supplementary is not None and not isinstance(self.Cell_Lines_Supplementary, str):
            self.Cell_Lines_Supplementary = str(self.Cell_Lines_Supplementary)

        super().__post_init__(**kwargs)


@dataclass
class Protein(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Protein"]
    class_class_curie: ClassVar[str] = "linkml:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = LINKML.Protein

    Protein: Union[str, ProteinProtein] = None
    Protein_Name: Optional[str] = None
    Protein_URL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Protein):
            self.MissingRequiredField("Protein")
        if not isinstance(self.Protein, ProteinProtein):
            self.Protein = ProteinProtein(self.Protein)

        if self.Protein_Name is not None and not isinstance(self.Protein_Name, str):
            self.Protein_Name = str(self.Protein_Name)

        if self.Protein_URL is not None and not isinstance(self.Protein_URL, URI):
            self.Protein_URL = URI(self.Protein_URL)

        super().__post_init__(**kwargs)


@dataclass
class OrganismPart(YAMLRoot):
    """
    An organism part entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["OrganismPart"]
    class_class_curie: ClassVar[str] = "linkml:OrganismPart"
    class_name: ClassVar[str] = "Organism Part"
    class_model_uri: ClassVar[URIRef] = LINKML.OrganismPart

    Organism_Part: Union[str, OrganismPartOrganismPart] = None
    Organism_Part_Identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Organism_Part):
            self.MissingRequiredField("Organism_Part")
        if not isinstance(self.Organism_Part, OrganismPartOrganismPart):
            self.Organism_Part = OrganismPartOrganismPart(self.Organism_Part)

        if self.Organism_Part_Identifier is not None and not isinstance(self.Organism_Part_Identifier, str):
            self.Organism_Part_Identifier = str(self.Organism_Part_Identifier)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.image__id = Slot(uri=LINKML.id, name="image__id", curie=LINKML.curie('id'),
                   model_uri=LINKML.image__id, domain=None, range=URIRef)

slots.image__name = Slot(uri=LINKML.name, name="image__name", curie=LINKML.curie('name'),
                   model_uri=LINKML.image__name, domain=None, range=str)

slots.image__organism = Slot(uri=LINKML.organism, name="image__organism", curie=LINKML.curie('organism'),
                   model_uri=LINKML.image__organism, domain=None, range=Optional[Union[str, OrganismOrganism]])

slots.image__gene = Slot(uri=LINKML.gene, name="image__gene", curie=LINKML.curie('gene'),
                   model_uri=LINKML.image__gene, domain=None, range=Optional[Union[str, GeneGeneSymbol]])

slots.image__phenotype = Slot(uri=LINKML.phenotype, name="image__phenotype", curie=LINKML.curie('phenotype'),
                   model_uri=LINKML.image__phenotype, domain=None, range=Optional[Union[str, PhenotypePhenotype]])

slots.image__compound = Slot(uri=LINKML.compound, name="image__compound", curie=LINKML.curie('compound'),
                   model_uri=LINKML.image__compound, domain=None, range=Optional[Union[str, CompoundCompoundName]])

slots.image__pathology = Slot(uri=LINKML.pathology, name="image__pathology", curie=LINKML.curie('pathology'),
                   model_uri=LINKML.image__pathology, domain=None, range=Optional[Union[Union[str, PathologyPathology], List[Union[str, PathologyPathology]]]])

slots.image__antibody = Slot(uri=LINKML.antibody, name="image__antibody", curie=LINKML.curie('antibody'),
                   model_uri=LINKML.image__antibody, domain=None, range=Optional[Union[Union[str, AntibodyAntibody], List[Union[str, AntibodyAntibody]]]])

slots.image__siRNA = Slot(uri=LINKML.siRNA, name="image__siRNA", curie=LINKML.curie('siRNA'),
                   model_uri=LINKML.image__siRNA, domain=None, range=Optional[Union[Union[str, SiRNASiRNAIdentifier], List[Union[str, SiRNASiRNAIdentifier]]]])

slots.image__cell_line = Slot(uri=LINKML.cell_line, name="image__cell_line", curie=LINKML.curie('cell_line'),
                   model_uri=LINKML.image__cell_line, domain=None, range=Optional[Union[str, CellLineCellLines]])

slots.image__protein = Slot(uri=LINKML.protein, name="image__protein", curie=LINKML.curie('protein'),
                   model_uri=LINKML.image__protein, domain=None, range=Optional[Union[str, ProteinProtein]])

slots.organism__Organism = Slot(uri=LINKML.Organism, name="organism__Organism", curie=LINKML.curie('Organism'),
                   model_uri=LINKML.organism__Organism, domain=None, range=URIRef)

slots.organism__organism_part = Slot(uri=LINKML.organism_part, name="organism__organism_part", curie=LINKML.curie('organism_part'),
                   model_uri=LINKML.organism__organism_part, domain=None, range=Optional[Union[Union[str, OrganismPartOrganismPart], List[Union[str, OrganismPartOrganismPart]]]])

slots.gene__gene_symbol = Slot(uri=LINKML.gene_symbol, name="gene__gene_symbol", curie=LINKML.curie('gene_symbol'),
                   model_uri=LINKML.gene__gene_symbol, domain=None, range=URIRef)

slots.gene__gene_identifier = Slot(uri=LINKML.gene_identifier, name="gene__gene_identifier", curie=LINKML.curie('gene_identifier'),
                   model_uri=LINKML.gene__gene_identifier, domain=None, range=str)

slots.gene__gene_identifier_url = Slot(uri=LINKML.gene_identifier_url, name="gene__gene_identifier_url", curie=LINKML.curie('gene_identifier_url'),
                   model_uri=LINKML.gene__gene_identifier_url, domain=None, range=Union[str, URI])

slots.phenotype__Phenotype = Slot(uri=LINKML.Phenotype, name="phenotype__Phenotype", curie=LINKML.curie('Phenotype'),
                   model_uri=LINKML.phenotype__Phenotype, domain=None, range=URIRef)

slots.phenotype__Phenotype_Term_Name = Slot(uri=LINKML.Phenotype_Term_Name, name="phenotype__Phenotype_Term_Name", curie=LINKML.curie('Phenotype_Term_Name'),
                   model_uri=LINKML.phenotype__Phenotype_Term_Name, domain=None, range=str)

slots.phenotype__Phenotype_Term_Accession = Slot(uri=LINKML.Phenotype_Term_Accession, name="phenotype__Phenotype_Term_Accession", curie=LINKML.curie('Phenotype_Term_Accession'),
                   model_uri=LINKML.phenotype__Phenotype_Term_Accession, domain=None, range=Optional[str])

slots.phenotype__Phenotype_Term_Accession_URL = Slot(uri=LINKML.Phenotype_Term_Accession_URL, name="phenotype__Phenotype_Term_Accession_URL", curie=LINKML.curie('Phenotype_Term_Accession_URL'),
                   model_uri=LINKML.phenotype__Phenotype_Term_Accession_URL, domain=None, range=Optional[Union[str, URI]])

slots.compound__compound_name = Slot(uri=LINKML.compound_name, name="compound__compound_name", curie=LINKML.curie('compound_name'),
                   model_uri=LINKML.compound__compound_name, domain=None, range=URIRef)

slots.compound__Compound_Name_URL = Slot(uri=LINKML.Compound_Name_URL, name="compound__Compound_Name_URL", curie=LINKML.curie('Compound_Name_URL'),
                   model_uri=LINKML.compound__Compound_Name_URL, domain=None, range=Union[str, URI])

slots.pathology__Pathology = Slot(uri=LINKML.Pathology, name="pathology__Pathology", curie=LINKML.curie('Pathology'),
                   model_uri=LINKML.pathology__Pathology, domain=None, range=URIRef)

slots.pathology__Pathology_Identifier = Slot(uri=LINKML.Pathology_Identifier, name="pathology__Pathology_Identifier", curie=LINKML.curie('Pathology_Identifier'),
                   model_uri=LINKML.pathology__Pathology_Identifier, domain=None, range=str)

slots.antibody__Antibody = Slot(uri=LINKML.Antibody, name="antibody__Antibody", curie=LINKML.curie('Antibody'),
                   model_uri=LINKML.antibody__Antibody, domain=None, range=URIRef)

slots.antibody__Antibody_Identifier = Slot(uri=LINKML.Antibody_Identifier, name="antibody__Antibody_Identifier", curie=LINKML.curie('Antibody_Identifier'),
                   model_uri=LINKML.antibody__Antibody_Identifier, domain=None, range=str)

slots.siRNA__siRNA_Identifier = Slot(uri=LINKML.siRNA_Identifier, name="siRNA__siRNA_Identifier", curie=LINKML.curie('siRNA_Identifier'),
                   model_uri=LINKML.siRNA__siRNA_Identifier, domain=None, range=URIRef)

slots.siRNA__siRNA_Pool_Identifier = Slot(uri=LINKML.siRNA_Pool_Identifier, name="siRNA__siRNA_Pool_Identifier", curie=LINKML.curie('siRNA_Pool_Identifier'),
                   model_uri=LINKML.siRNA__siRNA_Pool_Identifier, domain=None, range=Optional[str])

slots.cellLine__Cell_lines = Slot(uri=LINKML.Cell_lines, name="cellLine__Cell_lines", curie=LINKML.curie('Cell_lines'),
                   model_uri=LINKML.cellLine__Cell_lines, domain=None, range=URIRef)

slots.cellLine__Cell_Lines_Supplementary = Slot(uri=LINKML.Cell_Lines_Supplementary, name="cellLine__Cell_Lines_Supplementary", curie=LINKML.curie('Cell_Lines_Supplementary'),
                   model_uri=LINKML.cellLine__Cell_Lines_Supplementary, domain=None, range=Optional[str])

slots.protein__Protein = Slot(uri=LINKML.Protein, name="protein__Protein", curie=LINKML.curie('Protein'),
                   model_uri=LINKML.protein__Protein, domain=None, range=URIRef)

slots.protein__Protein_Name = Slot(uri=LINKML.Protein_Name, name="protein__Protein_Name", curie=LINKML.curie('Protein_Name'),
                   model_uri=LINKML.protein__Protein_Name, domain=None, range=Optional[str])

slots.protein__Protein_URL = Slot(uri=LINKML.Protein_URL, name="protein__Protein_URL", curie=LINKML.curie('Protein_URL'),
                   model_uri=LINKML.protein__Protein_URL, domain=None, range=Optional[Union[str, URI]])

slots.organismPart__Organism_Part = Slot(uri=LINKML.Organism_Part, name="organismPart__Organism_Part", curie=LINKML.curie('Organism_Part'),
                   model_uri=LINKML.organismPart__Organism_Part, domain=None, range=URIRef)

slots.organismPart__Organism_Part_Identifier = Slot(uri=LINKML.Organism_Part_Identifier, name="organismPart__Organism_Part_Identifier", curie=LINKML.curie('Organism_Part_Identifier'),
                   model_uri=LINKML.organismPart__Organism_Part_Identifier, domain=None, range=Optional[str])
