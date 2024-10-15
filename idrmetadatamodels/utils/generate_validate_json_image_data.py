#from linkml_runtime.linkml_model.types import Integer, String, Uri
''''
This script is used to extract a container (project or screen) images' meta data from the searchengine
It will handle the data and create the objects from the generated python code (generated from the image schema)
Then it will get the json from the objects and validate it using the schema model
This script is still in progress
'''

from idrmetadatamodels.models.image_schema import Image, OrganismPart, Organism, Phenotype, Compound, Protein, CellLine, SiRNA
from idrmetadatamodels.utils.get_schema_attributes import get_included_schema_classes

schema_classes={"Image":Image, "Organism Part":OrganismPart, "Organism":Organism, "Phenotype":Phenotype,
         "Compound":Compound, "Protein":Protein,"Cell line":CellLine,"siRNA":SiRNA}

from idrmetadatamodels.utils.get_schema_attributes import get_schema_attributes
import logging
import json

logger=logging.getLogger("idr-metadata-model")

logger.setLevel(logging.INFO)

from idrmetadatamodels.utils.idr_connector import get_results, get_query_results

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


def extract_schema_data(image, all_attributes, target_schema):
    records={}
    if target_schema in all_attributes:
        main_schema_attributes=all_attributes[target_schema]
    else:
        main_schema_attributes=get_schema_attributes((target_schema))
        all_attributes[target_schema]=main_schema_attributes
    for main_schema, atts in main_schema_attributes.items():
        for atr in atts:
            if atr.get("range") in ["string", "uri","integer"]:
                if image.get(atr.get("name")):
                    records[atr.get("name")]=image.get(atr.get("name"))
            else:
                records[atr.get("name")] = extract_schema_data(image, all_attributes, atr.get("range"))
    return records


def process_results(images_results, target_schema="Image"):
    images_json = []
    if target_schema.lower() == "all":
        target_schema = "Image"
    all_attributes={}
    print (target_schema)
    print ("########################")
    all_attributes[target_schema]=get_schema_attributes(target_schema)
    included_schema_classes = get_included_schema_classes(target_schema)
    for sub_schem in included_schema_classes:
        all_attributes[sub_schem]=get_schema_attributes(sub_schem)
    print (included_schema_classes)

    for image in images_results:
        image_ = convert_to_key_value(image)
        attrs=extract_schema_data(image_,all_attributes,target_schema)
        if target_schema!="Image":
            img_dict = {"id": image.get("id"), "name":image.get("name"),target_schema.lower(): attrs}
        else:
            img_dict = attrs
            img_dict["id"]=image.get("id")
            img_dict["name"]=image.get("name")


        #img_dict = json_dumper(json_dumper(image_obj))
        #del img_dict['@type']
        images_json.append(img_dict)
        ## clean the data
        to_be_deleted=[]
        for item, itev in img_dict.items():
            try:
                if len(itev)==0:
                    to_be_deleted.append(item)
            except:
                pass
        for it in to_be_deleted:
            del img_dict[it]

    return images_json




def validate_data(images_json, target_schema="Image"):
    for image_json in images_json:
        try:
            image = Image(**image_json)  # This will raise an error if validation fails
            logger.info('Valid data!, the image data with id=%s, and name %s is valid.' %(image_json.get("id"), image_json.get("name")))
        except Exception as e:
            print("Validation failed for image, id: %s, error message is: %s"%(image_json.get("id"),e))



def save_results_file(results, file_name="results.json"):
    with open(file_name, "w") as outfile:
        outfile.write(json.dumps(results, indent=4))