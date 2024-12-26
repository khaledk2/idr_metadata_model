# Auto generated from study_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-24T14:27:25
# Schema: study_idr_schema
#
# id: idr.study.schema
# description: A LinkML schema translated from the idr key-value pairs for study
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
# from .types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = LINKML


# Types

# Class references
class StudyId(extended_int):
    pass


@dataclass
class Study(YAMLRoot):
    """
    A study entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Study"]
    class_class_curie: ClassVar[str] = "linkml:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = LINKML.Study

    id: Union[int, StudyId] = None
    name: str = None
    Imaging_Method: Optional[str] = None
    Study_Type: Optional[str] = None
    Data_Publisher: Optional[str] = None
    Sample_Type: Optional[str] = None
    Organism: Optional[str] = None
    Release_Date: Optional[str] = None
    license: Optional[Union[dict, "License"]] = None
    publication: Optional[Union[dict, "Publication"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.Imaging_Method is not None and not isinstance(self.Imaging_Method, str):
            self.Imaging_Method = str(self.Imaging_Method)

        if self.Study_Type is not None and not isinstance(self.Study_Type, str):
            self.Study_Type = str(self.Study_Type)

        if self.Data_Publisher is not None and not isinstance(self.Data_Publisher, str):
            self.Data_Publisher = str(self.Data_Publisher)

        if self.Sample_Type is not None and not isinstance(self.Sample_Type, str):
            self.Sample_Type = str(self.Sample_Type)

        if self.Organism is not None and not isinstance(self.Organism, str):
            self.Organism = str(self.Organism)

        if self.Release_Date is not None and not isinstance(self.Release_Date, str):
            self.Release_Date = str(self.Release_Date)

        if self.license is not None and not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        super().__post_init__(**kwargs)


@dataclass
class License(YAMLRoot):
    """
    The study license
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["License"]
    class_class_curie: ClassVar[str] = "linkml:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = LINKML.License

    License: Optional[str] = None
    Copyright: Optional[str] = None
    Data_Publisher: Optional[str] = None
    Data_DOI: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.License is not None and not isinstance(self.License, str):
            self.License = str(self.License)

        if self.Copyright is not None and not isinstance(self.Copyright, str):
            self.Copyright = str(self.Copyright)

        if self.Data_Publisher is not None and not isinstance(self.Data_Publisher, str):
            self.Data_Publisher = str(self.Data_Publisher)

        if self.Data_DOI is not None and not isinstance(self.Data_DOI, str):
            self.Data_DOI = str(self.Data_DOI)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    """
    A Publication entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["Publication"]
    class_class_curie: ClassVar[str] = "linkml:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = LINKML.Publication

    Publication_Title: Optional[str] = None
    Publication_Authors: Optional[str] = None
    Publication_DOI: Optional[str] = None
    Publication_DOI_URL: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Publication_Title is not None and not isinstance(self.Publication_Title, str):
            self.Publication_Title = str(self.Publication_Title)

        if self.Publication_Authors is not None and not isinstance(self.Publication_Authors, str):
            self.Publication_Authors = str(self.Publication_Authors)

        if self.Publication_DOI is not None and not isinstance(self.Publication_DOI, str):
            self.Publication_DOI = str(self.Publication_DOI)

        if self.Publication_DOI_URL is not None and not isinstance(self.Publication_DOI_URL, str):
            self.Publication_DOI_URL = str(self.Publication_DOI_URL)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.study__id = Slot(uri=LINKML.id, name="study__id", curie=LINKML.curie('id'),
                   model_uri=LINKML.study__id, domain=None, range=URIRef)

slots.study__name = Slot(uri=LINKML.name, name="study__name", curie=LINKML.curie('name'),
                   model_uri=LINKML.study__name, domain=None, range=str)

slots.study__Imaging_Method = Slot(uri=LINKML.Imaging_Method, name="study__Imaging_Method", curie=LINKML.curie('Imaging_Method'),
                   model_uri=LINKML.study__Imaging_Method, domain=None, range=Optional[str])

slots.study__Study_Type = Slot(uri=LINKML.Study_Type, name="study__Study_Type", curie=LINKML.curie('Study_Type'),
                   model_uri=LINKML.study__Study_Type, domain=None, range=Optional[str])

slots.study__Data_Publisher = Slot(uri=LINKML.Data_Publisher, name="study__Data_Publisher", curie=LINKML.curie('Data_Publisher'),
                   model_uri=LINKML.study__Data_Publisher, domain=None, range=Optional[str])

slots.study__Sample_Type = Slot(uri=LINKML.Sample_Type, name="study__Sample_Type", curie=LINKML.curie('Sample_Type'),
                   model_uri=LINKML.study__Sample_Type, domain=None, range=Optional[str])

slots.study__Organism = Slot(uri=LINKML.Organism, name="study__Organism", curie=LINKML.curie('Organism'),
                   model_uri=LINKML.study__Organism, domain=None, range=Optional[str])

slots.study__Release_Date = Slot(uri=LINKML.Release_Date, name="study__Release_Date", curie=LINKML.curie('Release_Date'),
                   model_uri=LINKML.study__Release_Date, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}$'))

slots.study__license = Slot(uri=LINKML.license, name="study__license", curie=LINKML.curie('license'),
                   model_uri=LINKML.study__license, domain=None, range=Optional[Union[dict, License]])

slots.study__publication = Slot(uri=LINKML.publication, name="study__publication", curie=LINKML.curie('publication'),
                   model_uri=LINKML.study__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.license__License = Slot(uri=LINKML.License, name="license__License", curie=LINKML.curie('License'),
                   model_uri=LINKML.license__License, domain=None, range=Optional[str])

slots.license__Copyright = Slot(uri=LINKML.Copyright, name="license__Copyright", curie=LINKML.curie('Copyright'),
                   model_uri=LINKML.license__Copyright, domain=None, range=Optional[str])

slots.license__Data_Publisher = Slot(uri=LINKML.Data_Publisher, name="license__Data_Publisher", curie=LINKML.curie('Data_Publisher'),
                   model_uri=LINKML.license__Data_Publisher, domain=None, range=Optional[str])

slots.license__Data_DOI = Slot(uri=LINKML.Data_DOI, name="license__Data_DOI", curie=LINKML.curie('Data_DOI'),
                   model_uri=LINKML.license__Data_DOI, domain=None, range=Optional[str])

slots.publication__Publication_Title = Slot(uri=LINKML.Publication_Title, name="publication__Publication_Title", curie=LINKML.curie('Publication_Title'),
                   model_uri=LINKML.publication__Publication_Title, domain=None, range=Optional[str])

slots.publication__Publication_Authors = Slot(uri=LINKML.Publication_Authors, name="publication__Publication_Authors", curie=LINKML.curie('Publication_Authors'),
                   model_uri=LINKML.publication__Publication_Authors, domain=None, range=Optional[str])

slots.publication__Publication_DOI = Slot(uri=LINKML.Publication_DOI, name="publication__Publication_DOI", curie=LINKML.curie('Publication_DOI'),
                   model_uri=LINKML.publication__Publication_DOI, domain=None, range=Optional[str])

slots.publication__Publication_DOI_URL = Slot(uri=LINKML.Publication_DOI_URL, name="publication__Publication_DOI_URL", curie=LINKML.curie('Publication_DOI_URL'),
                   model_uri=LINKML.publication__Publication_DOI_URL, domain=None, range=Optional[str])
