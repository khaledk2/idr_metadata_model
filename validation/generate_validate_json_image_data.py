#from linkml_runtime.linkml_model.types import Integer, String, Uri
''''
This script is used to extract a container (project or screen) images' meta data from the searchengine
It will handle the data and create the objects from the generated python code (generated from the image schema)
Then it will get the json from the objects and validate it using the schema model
This script is still in progress
'''

from models.image_schema import Image, OrganismPart, Organism, Pathology, Phenotype, Compound, CellLine

import sys
import logging
import json
from linkml_runtime.dumpers import json_dumper
from linkml.validator import validate
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from validation.idr_connector import get_results

muti_values=[""]
def convert_to_key_value(json_ob):
    objects={}
    for lst in json_ob.get("key_values"):
        if type(lst) is dict:

                objects[lst.get("name")]=lst.get("value")

    return objects

def get_image_data_inside_container(container):
    images_results = get_results(container)
    images_json=[]
    for image in images_results:
        image_=convert_to_key_value(image)
        organism=None
        pathology= None
        phenotype=None
        compound= None
        cellLine=None
        organismPart_=None

        if image_.get("Organism"):
            if image_.get("Organism Part"):
                organismPart_=OrganismPart(organism_part=image_.get("Organism Part"), organism_part_identifier=image_.get("Organism Part Identifier"))
            organism = Organism(organism=image_.get("Organism"), organism_part=[organismPart_])
            print (organism.organism_part)

        if image_.get("Phenotype"):
            phenotype=Phenotype(phenotype=image_.get("Phenotype"), phenotype_term_name=image_.get("Phenotype Term Name"),
                                phenotype_term_accession=image_.get("Phenotype Term Accession"),phenotype_term_accession_url=image_.get("Phenotype Term Accession URL"))

        if image_.get("Compound Name"):
            compound=Compound(compound_name=image_.get("Compound Name"), compound_name_url=image_.get("Compound Name URL"))

        image_obj=Image(id=image.get("id"), name=image.get("name"), organism=organism,pathology=pathology, phenotype=phenotype, compound=compound, cell_line=cellLine)

        #print (image_obj)
        img_dict=json.loads(json_dumper.dumps(image_obj))
        del img_dict['@type']
        images_json.append(img_dict)
    return images_json



def validate_data (images_json):
    for data in images_json:
        report = validate(data, "models/image_schema.yaml", "Image")
        if not report.results:
            print('The image data with id=%s is valid!'%(data.get("id")))
        else:
            for result in report.results:
                print(result.message)


images_json = get_image_data_inside_container("idr0051")
# "idr0044")
# ("idr0157"))
# ("idr0051))
# idr0090


print (json.dumps(images_json, indent=4))
validate_data(images_json)