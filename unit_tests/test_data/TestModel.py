# Auto generated from TestModel.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-26T18:54:59
# Schema: testmodel_idr_schema
#
# id: testmodel.image.schema
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
class TestModel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["TestModel"]
    class_class_curie: ClassVar[str] = "linkml:TestModel"
    class_name: ClassVar[str] = "TestModel"
    class_model_uri: ClassVar[URIRef] = LINKML.TestModel

    Protein_Name: str = None
    Organism: Optional[str] = None
    Cell_Line: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Protein_Name):
            self.MissingRequiredField("Protein_Name")
        if not isinstance(self.Protein_Name, str):
            self.Protein_Name = str(self.Protein_Name)

        if self.Organism is not None and not isinstance(self.Organism, str):
            self.Organism = str(self.Organism)

        if self.Cell_Line is not None and not isinstance(self.Cell_Line, str):
            self.Cell_Line = str(self.Cell_Line)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.testModel__Protein_Name = Slot(uri=LINKML.Protein_Name, name="testModel__Protein_Name", curie=LINKML.curie('Protein_Name'),
                   model_uri=LINKML.testModel__Protein_Name, domain=None, range=str)

slots.testModel__Organism = Slot(uri=LINKML.Organism, name="testModel__Organism", curie=LINKML.curie('Organism'),
                   model_uri=LINKML.testModel__Organism, domain=None, range=Optional[str])

slots.testModel__Cell_Line = Slot(uri=LINKML.Cell_Line, name="testModel__Cell_Line", curie=LINKML.curie('Cell_Line'),
                   model_uri=LINKML.testModel__Cell_Line, domain=None, range=Optional[str])
