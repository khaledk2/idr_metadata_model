# Auto generated from no_screen_study_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-22T12:52:26
# Schema: no_screen_study_idr_schema
#
# id: idr.no_screen_study.schema
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
#from .types import Integer, String

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


class NoScreenStudyId(StudyId):
    pass


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

    license: str = None
    copyright: str = None
    data_publisher: str = None
    data_DOI: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, str):
            self.license = str(self.license)

        if self._is_empty(self.copyright):
            self.MissingRequiredField("copyright")
        if not isinstance(self.copyright, str):
            self.copyright = str(self.copyright)

        if self._is_empty(self.data_publisher):
            self.MissingRequiredField("data_publisher")
        if not isinstance(self.data_publisher, str):
            self.data_publisher = str(self.data_publisher)

        if self._is_empty(self.data_DOI):
            self.MissingRequiredField("data_DOI")
        if not isinstance(self.data_DOI, str):
            self.data_DOI = str(self.data_DOI)

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

    publication_title: Optional[str] = None
    publication_authors: Optional[str] = None
    publication_doi: Optional[str] = None
    publication_doi_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication_title is not None and not isinstance(self.publication_title, str):
            self.publication_title = str(self.publication_title)

        if self.publication_authors is not None and not isinstance(self.publication_authors, str):
            self.publication_authors = str(self.publication_authors)

        if self.publication_doi is not None and not isinstance(self.publication_doi, str):
            self.publication_doi = str(self.publication_doi)

        if self.publication_doi_url is not None and not isinstance(self.publication_doi_url, str):
            self.publication_doi_url = str(self.publication_doi_url)

        super().__post_init__(**kwargs)


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
    imaging_method: str = None
    study_type: str = None
    license: Union[dict, License] = None
    data_publisher: str = None
    release_date: str = None
    publication: Optional[Union[dict, Publication]] = None
    sample_type: Optional[str] = None
    organism: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.imaging_method):
            self.MissingRequiredField("imaging_method")
        if not isinstance(self.imaging_method, str):
            self.imaging_method = str(self.imaging_method)

        if self._is_empty(self.study_type):
            self.MissingRequiredField("study_type")
        if not isinstance(self.study_type, str):
            self.study_type = str(self.study_type)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        if self._is_empty(self.data_publisher):
            self.MissingRequiredField("data_publisher")
        if not isinstance(self.data_publisher, str):
            self.data_publisher = str(self.data_publisher)

        if self._is_empty(self.release_date):
            self.MissingRequiredField("release_date")
        if not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        super().__post_init__(**kwargs)


@dataclass
class NoScreenStudy(Study):
    """
    An experimental study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["NoScreenStudy"]
    class_class_curie: ClassVar[str] = "linkml:NoScreenStudy"
    class_name: ClassVar[str] = "No_screen_study"
    class_model_uri: ClassVar[URIRef] = LINKML.NoScreenStudy

    id: Union[int, NoScreenStudyId] = None
    imaging_method: str = None
    study_type: str = None
    license: Union[dict, License] = None
    data_publisher: str = None
    release_date: str = None
    experimental_description: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoScreenStudyId):
            self.id = NoScreenStudyId(self.id)

        if self._is_empty(self.experimental_description):
            self.MissingRequiredField("experimental_description")
        if not isinstance(self.experimental_description, str):
            self.experimental_description = str(self.experimental_description)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.noScreenStudy__experimental_description = Slot(uri=LINKML.experimental_description, name="noScreenStudy__experimental_description", curie=LINKML.curie('experimental_description'),
                   model_uri=LINKML.noScreenStudy__experimental_description, domain=None, range=str)

slots.license__license = Slot(uri=LINKML.license, name="license__license", curie=LINKML.curie('license'),
                   model_uri=LINKML.license__license, domain=None, range=str)

slots.license__copyright = Slot(uri=LINKML.copyright, name="license__copyright", curie=LINKML.curie('copyright'),
                   model_uri=LINKML.license__copyright, domain=None, range=str)

slots.license__data_publisher = Slot(uri=LINKML.data_publisher, name="license__data_publisher", curie=LINKML.curie('data_publisher'),
                   model_uri=LINKML.license__data_publisher, domain=None, range=str)

slots.license__data_DOI = Slot(uri=LINKML.data_DOI, name="license__data_DOI", curie=LINKML.curie('data_DOI'),
                   model_uri=LINKML.license__data_DOI, domain=None, range=str)

slots.publication__publication_title = Slot(uri=LINKML.publication_title, name="publication__publication_title", curie=LINKML.curie('publication_title'),
                   model_uri=LINKML.publication__publication_title, domain=None, range=Optional[str])

slots.publication__publication_authors = Slot(uri=LINKML.publication_authors, name="publication__publication_authors", curie=LINKML.curie('publication_authors'),
                   model_uri=LINKML.publication__publication_authors, domain=None, range=Optional[str])

slots.publication__publication_doi = Slot(uri=LINKML.publication_doi, name="publication__publication_doi", curie=LINKML.curie('publication_doi'),
                   model_uri=LINKML.publication__publication_doi, domain=None, range=Optional[str])

slots.publication__publication_doi_url = Slot(uri=LINKML.publication_doi_url, name="publication__publication_doi_url", curie=LINKML.curie('publication_doi_url'),
                   model_uri=LINKML.publication__publication_doi_url, domain=None, range=Optional[str])

slots.study__id = Slot(uri=LINKML.id, name="study__id", curie=LINKML.curie('id'),
                   model_uri=LINKML.study__id, domain=None, range=URIRef)

slots.study__imaging_method = Slot(uri=LINKML.imaging_method, name="study__imaging_method", curie=LINKML.curie('imaging_method'),
                   model_uri=LINKML.study__imaging_method, domain=None, range=str)

slots.study__publication = Slot(uri=LINKML.publication, name="study__publication", curie=LINKML.curie('publication'),
                   model_uri=LINKML.study__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.study__study_type = Slot(uri=LINKML.study_type, name="study__study_type", curie=LINKML.curie('study_type'),
                   model_uri=LINKML.study__study_type, domain=None, range=str)

slots.study__license = Slot(uri=LINKML.license, name="study__license", curie=LINKML.curie('license'),
                   model_uri=LINKML.study__license, domain=None, range=Union[dict, License])

slots.study__data_publisher = Slot(uri=LINKML.data_publisher, name="study__data_publisher", curie=LINKML.curie('data_publisher'),
                   model_uri=LINKML.study__data_publisher, domain=None, range=str)

slots.study__sample_type = Slot(uri=LINKML.sample_type, name="study__sample_type", curie=LINKML.curie('sample_type'),
                   model_uri=LINKML.study__sample_type, domain=None, range=Optional[str])

slots.study__organism = Slot(uri=LINKML.organism, name="study__organism", curie=LINKML.curie('organism'),
                   model_uri=LINKML.study__organism, domain=None, range=Optional[str])

slots.study__release_date = Slot(uri=LINKML.release_date, name="study__release_date", curie=LINKML.curie('release_date'),
                   model_uri=LINKML.study__release_date, domain=None, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}$'))
