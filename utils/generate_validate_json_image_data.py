#from linkml_runtime.linkml_model.types import Integer, String, Uri
''''
This script is used to extract a container (project or screen) images' meta data from the searchengine
It will handle the data and create the objects from the generated python code (generated from the image schema)
Then it will get the json from the objects and validate it using the schema model
This script is still in progress
'''

from models.image_schema import Image, OrganismPart, Organism, Phenotype, Compound

import sys
import logging
import json
import os
from linkml_runtime.dumpers import json_dumper
from linkml.validator import validate

logger=logging.getLogger("idr_metadata_model")

logger.setLevel(logging.INFO)

from utils.idr_connector import get_results, get_query_results


muti_values=[""]
def convert_to_key_value(json_ob):
    objects={}
    for lst in json_ob.get("key_values"):
        if type(lst) is dict:
                objects[lst.get("name")]=lst.get("value")
    return objects

def get_image_data_for_schema():
    pass

def get_image_from_single_attribute_qury(attr, value, target_schema="all", container_name=None):
    images_results=get_query_results(attr, value, container_name)
    return (process_results(images_results,target_schema))


def get_image_data_inside_container(container,target_schema="all"):
    images_results=get_results(container)
    return (process_results(images_results,target_schema))

def process_results(images_results, target_schema):
    images_json=[]
    for image in images_results:
        '''
        Now, it is only supports organism, pathology and phenotype
        Work is in progress to support other classes        
        '''
        image_=convert_to_key_value(image)
        organism=None
        pathology= None
        phenotype=None
        compound= None
        cellLine=None
        organismPart_=None
        if target_schema.lower()=="all" or target_schema.lower()=="organism":
            pass

        if (target_schema.lower()=="all" or target_schema.lower()=="organism") and image_.get("Organism"):
            if image_.get("Organism Part"):
                organismPart_=OrganismPart(organism_part=image_.get("Organism Part"), organism_part_identifier=image_.get("Organism Part Identifier"))
            organism = Organism(organism=image_.get("Organism"), organism_part=[organismPart_])

        if (target_schema.lower()=="all" or target_schema.lower()=="phenotype") and image_.get("Phenotype"):
            phenotype=Phenotype(phenotype=image_.get("Phenotype"), phenotype_term_name=image_.get("Phenotype Term Name"),
                                phenotype_term_accession=image_.get("Phenotype Term Accession"),phenotype_term_accession_url=image_.get("Phenotype Term Accession URL"))

        if (target_schema.lower()=="all" or target_schema.lower()=="compound name") and image_.get("Compound Name"):
            compound=Compound(compound_name=image_.get("Compound Name"), compound_name_url=image_.get("Compound Name URL"))

        image_obj=Image(id=image.get("id"), name=image.get("name"), organism=organism,pathology=pathology, phenotype=phenotype, compound=compound, cell_line=cellLine)

        img_dict=json.loads(json_dumper.dumps(image_obj))
        del img_dict['@type']
        images_json.append(img_dict)
    return images_json

def validate_data (images_json):
    schema_file = os.path.join(sys.path[1], "models/image_schema.yaml")
    os.chdir(os.path.join(sys.path[1], "models"))
    logger.info("Loading schema from %s" % schema_file)
    for data in images_json:
        report = validate(data, schema_file, "Image")
        if not report.results:
            logger.info('The image data with id=%s is valid!'%data.get("id"))
        else:
            for result in report.results:
                logger.error(result.message)



